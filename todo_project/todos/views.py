from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm

def todo_list(request):
  todos = Todo.objects.all().order_by('-created_at')
  return render(request, 'todos/index.html', {'todos': todos})

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