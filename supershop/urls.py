from django.urls import path

from .views import ProductView, CatalogueView, CategoryView, LogView, RegView, CartView, PictureView, CommentView

app_name = "supershop"

urlpatterns = [
    path('catalogue/<int:category>', CatalogueView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('users/log/', LogView.as_view()),
    path('users/reg/', RegView.as_view()),
    path('cart/create/', CartView.as_view()),
    path('cart/<int:productid>', CartView.as_view()),
    path('cart/<int:pk>', CartView.as_view()),
    path('pictures/<int:productid>', PictureView.as_view()),
    path('comments/create/', CommentView.as_view()),
    path('comments/<int:postid>', CommentView.as_view()),
    path('comments/<int:pk>', CommentView.as_view())
]