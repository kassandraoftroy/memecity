"""memecity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from memesite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^newsfeed/$', views.newsfeed, name='newsfeed'),
    url(r'^engage/$', views.engage, name='engage'),
    url(r'^review/$', views.enter_chat, name='enter_chat'),
    url(r'^timer/$', views.update_time, name='update_time'),
    url(r'^update-chatroom/$', views.update_chat, name='update_chat'),
    url(r'^new-message/$', views.add_chat, name='add_chat'),
    url(r'^dev/$', views.dev, name='dev'),
    url(r'^finale/$', views.finale, name='finale'),
]
