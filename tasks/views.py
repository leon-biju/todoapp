from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
# Create your views here.

from .models import *

def index(request):
  tasks = Task.objects.all()
  form = TaskForm()

  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('/')

  return render(request, "tasks/list.html", {"tasks": tasks, "form": form})