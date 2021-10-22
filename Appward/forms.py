from django import forms
from .models import Comments, Profile, Project, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'project_id']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']