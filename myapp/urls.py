from django.urls import path
from .views import user_register, user_login, user_logout
from .views import ad_or_list_tasks,edit_task,completed_tasks,pending_tasks

urlpatterns = [
    path('register/', user_register, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('tasks/', ad_or_list_tasks, name='task-list'),
    path('edit_tasks/<int:pk>/', edit_task, name='task-detail'),
    path('tasks/completed/', completed_tasks, name='completed-tasks'),
    path('tasks/pending/', pending_tasks, name='pending-tasks'),
]
