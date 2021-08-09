from django.urls import path
from .views import *

urlpatterns = [
path('',home, name='home'),
path('add-todo',addtodo, name='addtodo'),
path('update-todo',updatetodo, name='updatetodo'),
path('delete-todo',deletetodo, name='deletetodo'),
path('Todo',Todoview.as_view()),

]
