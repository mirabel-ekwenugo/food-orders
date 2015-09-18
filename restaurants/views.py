from django.shortcuts import render
from django.views.generic.list import ListView
from restaurants import models as restaurants_models


class RestaurantListView(ListView):
    model = restaurants_models.Restaurant

    def get_context_data(self, **kwargs):
        context = super(RestaurantListView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context