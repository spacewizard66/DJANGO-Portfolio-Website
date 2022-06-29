from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project


# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse("<h1>Django Home Page</h1>") # string of HTML
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'homepage.html', context)
