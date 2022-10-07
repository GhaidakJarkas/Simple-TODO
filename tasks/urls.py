from django.urls import path
from tasks import views


urlpatterns = [
    path('', views.index, name="index"),
    path('update_task/<int:pk>/', views.update_task, name="update_task"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]