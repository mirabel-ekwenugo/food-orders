from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cuisine(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class PhoneNumber(models.Model):
	phone_number = PhoneNumberField()

	def __str__(self):
		return self.phone_number


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    cuisines = models.ManyToManyField(Cuisine)
    description = models.TextField()
    phone_number = models.ManyToManyField(PhoneNumber)
    email_address = models.EmailField()

    def __str__(self):
		return self.name