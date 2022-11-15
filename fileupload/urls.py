from django.urls import path
from . import views

app_name = 'fileupload'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_file', views.new_file, name='new_file'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('write_dataframe/<int:pk>', views.write_dataframe, name='write_dataframe'),
    path('df-info/<int:pk>', views.show_df_infomation, name="df-info"),
    path('df-describe/<int:pk>', views.show_df_describe, name="df-describe"),
]
