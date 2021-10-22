from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload='images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    information = models.TextField(max_length=500)

    def __str__(self):
        return self.user
    
    def save_profile(self):
        return self.save()

    def delete_profile(self):
        return self.delete()

class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def save_project(self):
        return self.save()
    
    @classmethod
    def all_projects(cls):
        all_projects = cls.objects.all()
        return all_projects

    @classmethod
    def single_project(cls, id):
        single_project= cls.objects.filter(id=id)
        return single_project

    @classmethod
    def search_project(cls, search_term):
        search_project = cls.objects.filter(title=search_term)
        return search_project

