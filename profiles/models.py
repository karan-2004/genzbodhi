from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profiles(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profileImage = models.ImageField(upload_to='profile', default='profile/default.jpeg')
