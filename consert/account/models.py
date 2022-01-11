from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to="avatars/", height_field=None, width_field=None, max_length=None, null=True)
    credit = models.IntegerField(default=0)
    location=models.CharField( max_length=50,null=True,default='tehran')
