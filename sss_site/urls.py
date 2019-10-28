"""sss_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include,path,re_path
from django.views.generic.base import RedirectView
from login import views

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    re_path(r'^user/(?P<pk>\d+)/pwd_change/$', views.pwd_change, name='pwd_change'),
    re_path(r"^logout/$", views.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('repo/', include(('repo.urls', 'repo'), namespace='repo')),
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('rank/', include(('rank.urls', 'rank'), namespace='rank')),
    path('', RedirectView.as_view(url='home/')),
]
