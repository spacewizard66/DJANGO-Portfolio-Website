from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project


# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse("<h1>Django Home Page</h1>") # string of HTML
    return render(request, 'homepage.html')

def what_view2(request, *args, **kwargs):
    return HttpResponse("")

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfoliopage.html', context)