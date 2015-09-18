from django.conf.urls import url
from django.views.generic.list import ListView
from . import views 


urlpatterns = [
    url(r'^$', views.RestaurantListView.as_view(), name='restaurant-list'),
]