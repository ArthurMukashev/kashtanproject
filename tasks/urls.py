from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.index, name='index'),
    path('abort/', views.abort, name='abort'),
    path('excel/', views.excel, name='excel'),
    path('glossary/', views.glossary, name='glossary'),
    path('profile/', views.profile, name='profile'),
    path('tasks_argue/<int:task_id>/', views.tasks_argue, name='tasks_argue'),
    path('tasks_auto_check/', views.tasks_auto_check, name='auto_check'),
    path('tasks_verify/<int:task_id>/<int:price>/<int:user_id>', views.tasks_verify, name='tasks_verify'),
    path('variant/<int:pk>/', views.variant, name='variant')
]
