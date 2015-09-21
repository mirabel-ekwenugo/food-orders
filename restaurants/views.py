from django.shortcuts import render
from django.views.generic.list import ListView
from restaurants import models as restaurants_models


class RestaurantListView(ListView):
    model = restaurants_models.Restaurant

    def get_context_data(self, **kwargs):
        context = super(RestaurantListView, self).get_context_data(**kwargs)
        context['cuisine_list'] = restaurants_models.Cuisine.objects.all()
        context['cuisine_name'] = self.request.GET.get('cuisine')
        return context

    def get_queryset(self):
        queryset = super(RestaurantListView, self).get_queryset()
        cuisine_name = self.request.GET.get('cuisine')
        if cuisine_name:
            queryset = queryset.filter(cuisines__name=cuisine_name)
        return queryset