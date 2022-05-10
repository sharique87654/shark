from django.db import models

# Create your models here.

# class Login(models.Model):
#     email = models.CharField(max_length=122)
#     password = models.CharField(max_length=122)
#     date = models.DateField()

#     def __str__(self):
#         return self.email
    

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    comment = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name





