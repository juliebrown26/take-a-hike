from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register_page),
    url(r'^login$', views.login_page),
    url(r'^register$', views.register),
    url(r'^login_user$', views.login),
    url(r'^trailhead$', views.main),
    url(r'^newtrip$', views.new_trip),
    url(r'^create_trip$', views.create_trip),
    url(r'^trip/(?P<id>\d+)$', views.trip),
    url(r'^cancel_trip/(?P<id>\d+)$', views.cancel_trip),
    url(r'^add_hiker$', views.add_hiker),
    url(r'^trips$', views.trips),
    url(r'^add_bucket$', views.add_bucket),
    url(r'^logout$', views.logout),
]