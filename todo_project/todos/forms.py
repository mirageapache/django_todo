from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo   # 根據 Todo model 自動產生表單欄位
    fields = ['title', 'description']   # 這裡指定表單中要包含的欄位