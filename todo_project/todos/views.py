from django.shortcuts import render
from .models import Todo

def todo_list(request):
  todos = Todo.objects.all().order_by('-created_at')
  return render(request, 'todos/index.html', {'todos': todos})
