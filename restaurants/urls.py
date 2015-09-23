from django.conf.urls import url
from restaurants import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home-page'),
    url(r'^list/$', views.RestaurantListView.as_view(), name='restaurant-list'),
    url(r'^(?P<pk>[-\w]+)/$', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
]
