from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
  path('', views.todo_list, name='todo_list'),
  path('add/', views.add_todo, name='add_todo'),
  path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
  path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
  path('toggle_complete/<int:todo_id>/', views.toggle_complete, name='toggle_complete'),
  path('api/', include(router.urls))
]
