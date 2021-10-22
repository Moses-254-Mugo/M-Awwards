from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, EditProfileForm, 

from Appward.models import Project



# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def index(request):
    all_projects = Project.all_projects()
    return render(request, 'index.html', {'all_projects':all_projects})


@login_required(login_url='/accounts/login/')
def profile(request):
    profiles= Project.objects.filter(user = request.user)
    return render(request,'profile.hmtl', {'profiles':profiles})

@login_required(login_url='/accounts/login/')
def search_reslts(request):
    
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_project =Project.search_project(search_term)
        message = f'{search_term}'

        return render(request,'search.html', {'message':message,'projects':searched_project})
    
    else:
        message = 'You have not entered anything to search '
        return render(request, 'search.html', {'message':message})

@login_required(login_url='/accounts/login/')
def project_new(request):
    if request.method=='POST':
        