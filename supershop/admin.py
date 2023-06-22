from django.contrib import admin

from .models import Category, Product, User, Cart, Picture, Comment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Picture)
admin.site.register(Comment)