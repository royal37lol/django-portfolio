from django.shortcuts import render
from .models import MyProject

def home(request):
    my_projects = MyProject.objects.all()
    return render(request, 'myPortfolio/Home.html', {'my_projects': my_projects})
