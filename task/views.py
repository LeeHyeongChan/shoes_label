from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def task(request):
    return render(request, 'taskapp/task.html')
