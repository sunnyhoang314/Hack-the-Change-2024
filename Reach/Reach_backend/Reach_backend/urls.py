"""
URL configuration for Reach_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ask/<int:ask_id>/distance', views.get_distance_from_user, name='get_distance_from_user'),
    path('user/<int:user_id>/rank/', views.get_user_rank, name='get_user_rank'),
    path('leaderboard/', views.get_user_leaderboard, name='get_user_leaderboard'),
    path('global-leaderboard/', views.get_global_leaderboard, name='get_global_leaderboard'),
    path('create_task_request/', views.create_task_request, name='create_task_request'),]
