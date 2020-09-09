from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'sunyong'

urlpatterns = [
    path('',views.index, name='index'),
    path('mystorage/', auth_views.LoginView.as_view(template_name='sunyong/mystorage.html'), name='mystorage'),
]