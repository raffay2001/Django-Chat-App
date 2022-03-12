from tempfile import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.frontpage, name = 'frontpage'),
    path('signup/', views.sigunp, name = 'signup'),
    path('login/', views.signin, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
]