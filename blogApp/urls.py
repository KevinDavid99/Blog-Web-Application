from django.urls import path
from blogApp import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('post/<int:id>/', views.postDetail, name='post-detail'),
    path('post-create/', views.postCreate, name='post-create'),
    path('post-update/<int:id>/', views.postUpdate, name='post-update'),
    path('post-delete/<int:id>/', views.postDelete, name='post-delete')
]