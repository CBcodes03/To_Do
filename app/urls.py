from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('add-task/', views.add_task, name='add_task'),  # Route for adding a task
    path('delete-task/<str:task>/', views.delete_task, name='delete_task'), #route to delete a task
]