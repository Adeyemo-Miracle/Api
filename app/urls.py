from django.urls import path
from app import views

urlpatterns = [
    path('', views.createtodo, name='createtodo'),
    path('alltodo/', views.alltodo, name='alltodo'),
    path('delete/<int:id>', views.deletetodo, name='deletetodo'),
    path('details/<int:id>', views.tododetails, name='tododetails'),
    path('edit/<int:id>', views.todoedit, name='edit'),
]