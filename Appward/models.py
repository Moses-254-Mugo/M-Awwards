from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    info = models.TextField(max_length=500)

    def __str__(self):
        return self.user
    
    def save_profile(self):
        return self.save()

    def delete_profile(self):
        return self.delete()

class Project(models.Model):
    title = models.CharField(max_length=250)
    image = CloudinaryField('image')
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


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    text = models.CharField(max_length=200)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.user
    
    def save_comments(self):
        self.save()
    
    def delete_comments(self):
        self.delete()


    @classmethod 
    def all_comments(cls, id):
        comments = cls.objects.filter(project_id = id)
        return comments
    
class Rating(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.IntegerField(default=1)
    usability = models.IntegerField(default=1)
    content = models.IntegerField(default=1)