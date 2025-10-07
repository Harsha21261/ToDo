from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def home(request):
    task= Task.objects.filter(completed=False).order_by('-updated_at')
    context = {
        'tasks': task,
    }
    return render(request, 'home.html', context)