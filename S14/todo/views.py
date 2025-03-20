from django.shortcuts import render
from todo.models import Task
from django.views.generic import ListView


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request,"todo/index.html", {"foo":"cenas", "tasks":tasks})

class IndexView(ListView):
    model = Task
    