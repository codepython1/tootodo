from django.urls import path
from .views import *


urlpatterns = [
    path('',todos.as_view(),name='todo'),
    path('edit/<int:pk>/',edit.as_view(),name='edit'),
    path('delete/<int:pk>/',delete.as_view(),name='delete'),
    path('todocreate/',todocreate.as_view(),name='todo-create')

]