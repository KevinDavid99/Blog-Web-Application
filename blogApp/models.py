from django.db import models
from django.contrib.auth.models import User
import cloudinary
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='BlogPictures')
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ['-updated']
    

    def __str__(self):
        return f'{self.title} By {self.author}'
    



