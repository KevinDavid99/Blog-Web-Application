from django.db import models
from django.contrib.auth.models import User
import cloudinary.uploader


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_rfdkcc', upload_to='ProfilePics')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user}'s Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

