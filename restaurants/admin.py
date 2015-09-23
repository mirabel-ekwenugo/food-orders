from django.contrib import admin
from restaurants import models


admin.site.register(models.Cuisine)
admin.site.register(models.PhoneNumber)
admin.site.register(models.Restaurant)
admin.site.register(models.MenuItem)
