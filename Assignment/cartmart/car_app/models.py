from django.db import models
from car_brand_app.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, blank = True, null = True)
    image = models.ImageField(upload_to= 'car_app/media/uploads/')

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self) -> str:
        return f'comment by {self.name}'
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.car.name
    