from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name='main'

urlpatterns = [
    # ex: /main/
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    # ex: /polls/login
    path('login/', LoginView.as_view(template_name='main/login.html'), name="login"),
    # ex:/polls/logout
    path('logout/',LogoutView.as_view(template_name='main/logout.html'),name="logout"),

    # ex: /polls/register
    path('register/', views.register,name='register')
]