from django.contrib import admin
from .models import Project, Comments,Rating,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Comments)
admin.site.register(Rating)