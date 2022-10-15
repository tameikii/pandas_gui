from django.urls import path
from . import views

app_name = 'fileupload'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_file', views.new_file, name='new_file'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
