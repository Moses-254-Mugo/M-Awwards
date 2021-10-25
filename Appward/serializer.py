from django.db.models import fields
from rest_framework import serializers
from .models import Profile, Project

class ProlfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'info')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ('title','description','link', 'user')

