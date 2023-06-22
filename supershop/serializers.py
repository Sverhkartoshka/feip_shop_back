from rest_framework import serializers
from .models import Category, Product, User, Cart, Picture, Comment

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'category', 'price', 'description']

class CatalogueSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'email']

class CartSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.id')
    user = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Cart
        fields = ['product', 'user', 'date']

class PictureSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Picture
        fields = ['id', 'product', 'image_url']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    product = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = Comment
        fields = ['body', 'user', 'product', 'created']