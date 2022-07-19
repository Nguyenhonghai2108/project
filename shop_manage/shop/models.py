from django.db import models
from account.models import User

# Create your models here.
class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.shop_name

    def __str__(self):
        return self.email
