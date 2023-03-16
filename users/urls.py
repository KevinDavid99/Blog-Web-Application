from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.registerForm, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('profile/', views.profilePage, name='profile')
]