from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name + " " + self.last_name