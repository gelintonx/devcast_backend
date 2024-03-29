"""devcast_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from authentication.views import *
from podcast.views import *
from follow.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('register/', register),

    path('upload/', upload_podcast),
    path('podcasts/',podcasts),
    path('podcast-by-user/<str:user>/', get_podcasts_by_user),
    path('delete-audio/<str:podcast_name>', delete_audio),

    path('like/<str:podcast_name>', like),
    path('unlike/<str:podcast_name>', unlike),

    path('follow/<str:username>/',follow),
    path('unfollow/<str:username>/',unfollow),
    path('me/followers/',me_followers)
]
