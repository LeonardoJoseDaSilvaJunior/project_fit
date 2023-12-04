from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.LoginPage,name='login'),
    path('signout/',views.SignOutPage, name='signout'),
    path('signup/',views.SignUpPage, name='signup'),
]