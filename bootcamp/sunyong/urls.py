from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'sunyong'

urlpatterns = [
    path('',views.index, name='index'),
    path('upload/',views.upload_video, name='upload_video'),
    path('list/',views.video_list, name='video_list'),
    path('mystorage/', auth_views.LoginView.as_view(template_name='sunyong/mystorage.html'), name='mystorage'),
    path('videopage/', auth_views.LoginView.as_view(template_name='sunyong/videopage.html'), name='videopage'),
]