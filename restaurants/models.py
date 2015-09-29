from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import moneyed
from djmoney.models.fields import MoneyField
from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField()

    def __str__(self):
        return '%s' % self.phone_number


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='NGN')
    description = models.TextField()
    image = models.ImageField(upload_to='menu_item')

    def __str__(self):
        return '%s - %s' % (self.name, self.cost)


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    cuisines = models.ManyToManyField(Cuisine)
    description = models.TextField()
    phone_number = models.ManyToManyField(PhoneNumber)
    email_address = models.EmailField()
    menu = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name

    def cuisine_text(self):
        return ", ".join([cuisine.name for cuisine in self.cuisines.all()])

    def phone_num(self):
        return ", ".join(['%s' % telephone_number.phone_number for telephone_number in self.phone_number.all()])
