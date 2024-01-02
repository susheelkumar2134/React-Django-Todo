from django.urls import path
from todoapp import views

urlpatterns = [
    path("todos/",views.TodoView),
    path("todos/<int:pk>",views.TodoDetail)
]

# urls:
    # http://127.0.0.1:8000/todos
    # http://127.0.0.1:8000/todos/id