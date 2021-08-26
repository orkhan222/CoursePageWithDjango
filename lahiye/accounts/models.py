from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    

    email = models.EmailField('Email',unique=True)
    image = models.ImageField("Image",upload_to='profile_images',null=True, default='profile.jpg')
    fullname = models.CharField('FullName',null=True, max_length=127)
    


    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']