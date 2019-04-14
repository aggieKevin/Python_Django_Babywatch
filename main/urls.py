from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name='main'

urlpatterns = [
    # ex: /main/
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/',views.about,name='about'),

    # ex: /polls/login
    path('login/', LoginView.as_view(template_name='main/login.html'), name="login"),
    # ex:/polls/logout
    path('logout/',LogoutView.as_view(template_name='main/logout.html'),name="logout"),

    # ex: /polls/register
    path('register/', views.register,name='register'),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('updateprofile/',views.updateprofile, name='updateprofile'),
    path('updateguardian/',views.updateguardian,name='updateguardian'),
    path('updatechild/',views.updatechild,name='updatechild'),
    path('search/',views.search,name='search'),
    path('detail/<int:household_id>',views.detail,name='detail'),
]