"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import demo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/',demo.views.landing_view,name='landing'),

    path('fir/',demo.views.home_view,name='home'),
    path('update/',demo.views.home_view,name='home'),
    path('crime_report/',demo.views.home_view,name='home'),
    path('records/',demo.views.home_view,name='home'),
    path('contact/',demo.views.contact,name='contact'),
    path('developer/',demo.views.developer,name='developer'),
    path('profile/',demo.views.profile,name='profile'),
    path('notification/',demo.views.notification,name='notification'),
    path('language/',demo.views.language,name='language'),
    path('settings/',demo.views.settings,name='settings'),
    path('more/',demo.views.more,name='more'),
    path('firRegistration/',demo.views.firRegistration,name='firRegistration'),
    path('showupdate/',demo.views.showupdate,name='showupdate'),
    path('addinfo/',demo.views.addinfo,name='addinfo'),
    path('crimeRecord/',demo.views.crimeRecord,name='crimeRecord'),
    path('emergencyContact/',demo.views.emergencyContact,name='emergencyContact'),
    path('policeStation/',demo.views.policeStation,name='policeStation'),
    path('hospital/',demo.views.hospital,name='hospital'),
    path('fireService/',demo.views.fireService,name='fireService'),
    path('login/',demo.views.login,name='login'),
    path('signup/',demo.views.signup,name='signup'),
    path('about/',demo.views.about,name='about'),
    path('instructor/',demo.views.instructor,name='instructor'),
]
