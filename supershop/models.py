from django.db import models

def img_upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.TextField()
    image_url = models.ImageField(upload_to=img_upload_to)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.TextField()
    password = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.pk
    
class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image_url = models.ImageField(upload_to=img_upload_to)

    def __str__(self):
        return self.pk
    
class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.body