"""JusticeCalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from events.views import OneWeek, Updates


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', OneWeek.as_view(), name="homepage"),
    url(r'^week/(?P<firstDay>[0-9]{4}-[0-9]{2}-[0-9]{2})', OneWeek.as_view(), name="week"),
    url(r'^updates$', Updates.as_view(), name="updates"),
    url(r'^releases', TemplateView.as_view(template_name="events/releases.html"), name="releases"),
    url(r'^transition/', include('transition.urls')),
    url(r'^organizations/', include('organizations.urls'), name="organizations"),
    url(r'^tdor/', include('tdor.urls'), name="tdor"),
]
