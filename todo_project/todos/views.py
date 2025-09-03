from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import TodoSerializer

# 待辦清單
def todo_list(request):
  todos = Todo.objects.all().order_by('-created_at')
  return render(request, 'todos/index.html', {'todos': todos})

# 新增待辦事項
def add_todo(request):
  # POST 請求 => 驗證表單並儲存
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()  # 直接存進資料庫
      return redirect('todo_list')  # 新增成功後回到清單頁
  # GET 請求 => 顯示空白表單
  else:
    form = TodoForm()
  return render(request, 'todos/add_todo.html', {'form': form})

# 編輯待辦事項
def edit_todo(request, todo_id):
  todo = get_object_or_404(Todo, id=todo_id)   # 找不到指定的todo，回傳404
  if request.method == 'POST':
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
      form.save()
      return redirect('todo_list')
  else:
    form = TodoForm(instance=todo)   # 把現有資料帶入表單(編輯模式)
  return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})

# 刪除待辦事項
def delete_todo(request, todo_id):
  todo = get_object_or_404(Todo, id=todo_id)
  if request.method == 'POST':
    todo.delete()
    return redirect('todo_list')
  return render(request, 'todos/delete_todo.html', {'todo': todo})

# 標記待辦事項為完成或未完成
def toggle_complete(request, todo_id):
  todo = get_object_or_404(Todo, id=todo_id)
  todo.is_completed = not todo.is_completed
  todo.save()
  return redirect('todo_list')

class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all().order_by('-created_at')
  serializer_class = TodoSerializer
