from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('index', views.index, name='index'),
    path('other', views.other, name='other'),
    path('register', views.register, name='register'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_login/', views.user_login, name='user_login'),
]
