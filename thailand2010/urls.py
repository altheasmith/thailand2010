"""thailand2010 URL Configuration

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
from django.views.generic.base import RedirectView
from story import views as story_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/people')),
    path('people', story_views.all_people, name='people'),
    path('institutions', story_views.all_institutions, name='institutions'),
    path('events', story_views.all_events, name='events'),
    path('person/<int:person_id>', story_views.person, name='person'),
    path('person-detail/<int:person_detail_id>', story_views.person_detail, name='person-detail'),
    path('institution/<int:institution_id>', story_views.institution, name='institution'),
    path('institution-detail/<int:institution_detail_id>', story_views.institution_detail, name='institution-detail'),
    path('event/<int:event_id>', story_views.event, name='event'),
]
