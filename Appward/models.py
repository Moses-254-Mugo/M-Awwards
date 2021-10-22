from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload='images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.user
    
    def save_profile(self):
        return self.save()

    def delete_profile(self):
        return self.delete()

