from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    photo_profile = models.ImageField(default='fallback.png', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"