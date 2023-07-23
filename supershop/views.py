import hashlib

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, User, Cart, Picture, Comment
from .serializers import CategorySerializer, ProductSerializer, CatalogueSerializer, UserSerializer, CartSerializer, PictureSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

def h(pw):
    result = hashlib.md5(pw.encode())
    return result.hexdigest()

class ProductView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request, pk):
        req = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(req)
        return Response(serializer.data)
    
class CatalogueView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request, category):
        q = Product.objects.filter(category=category)
        serializer = CatalogueSerializer(q, many=True)
        return Response(serializer.data)
    
class CategoryView(APIView):
    def get(self, request):
        q = Category.objects.all()
        serializer = CategorySerializer(q, many=True)
        return Response(serializer.data)
    
class LogView(APIView):
    def post(self, request):
        user = request.data.get('user')
        user["password"] = h(user["password"])
        if User.objects.filter(email = user["email"]).exists():
            usercheck = get_object_or_404(User, email=user["email"])
            if (usercheck.password == user["password"]):
                return Response(True)
        return Response(False)

class RegView(APIView):
    def post(self, request):
        user = request.data.get('user')
        user["password"] = h(user["password"])
        serializer = UserSerializer(data=user)
        if User.objects.filter(email = user["email"]).exists():
            return Response(False)
        else:
            if serializer.is_valid(raise_exception=True):
                user_saved = serializer.save()
            return Response(True)
        
class CartView(APIView):
    def get(self, request, userid):
        cart = Cart.objects.filter(user=userid).order_by('-pk')
        serializer = CartSerializer(cart, many=True)
        return Response({"cart": serializer.data})
    
    def post(self, request):
        cart = request.data.get('cart')
        serializer = CartSerializer(data=cart)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
            return Response({"success": True})
        return Response({"success": False})
    
    def delete(self, request, pk):
        cart = get_object_or_404(Cart.objects.all(), pk=pk)
        cart.delete()
        return Response({
            "message": "Cart order with id `{}` has been deleted".format(pk)
        }, status=204)
    
class PictureView(APIView):
    def get(self, recuest, productid):
        pictures = Picture.objects.filter(product=productid).order_by('pk')
        serializer = PictureSerializer(pictures, many=True)
        return Response({"pictures": serializer.data})
    
class CommentView(APIView):
    def get(self, request, productid):
        comments = Comment.objects.filter(product=productid).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data})

    def post(self, request):
        comment = request.data.get('comment_add')
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
            return Response({"success": True})
        return Response({"success": False})
        
    def delete(self, request, pk):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()
        return Response({
            "message": "Comment with id `{}` has been deleted".format(pk)
        }, status=204)