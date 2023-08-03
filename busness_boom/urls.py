"""busness_boom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from boom.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserAPIView.as_view(template_name='home.html'), name='home'),
    path('session/auth/', include("rest_framework.urls")),
    path('user_list/', UserAPIView.as_view()),
    path('signup/', RegistationUser.as_view()),
    path('user/<int:user_id>/post_add', PostAdd.as_view()),
    path('user/<int:user_id>/post_list/', PostAPIView.as_view(), name='post_list'),
    path('user/<int:user_id>/post_list/update/<int:pk>', PostAPIUpdate.as_view()),
    path('user/<int:user_id>/post_list/delete/<int:pk>', PostAPIDelete.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
