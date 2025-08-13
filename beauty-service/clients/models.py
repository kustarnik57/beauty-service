from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ClientModel(models.Model):
    usr = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='пользователь', null=True)
    phone = models.CharField(max_length=255)