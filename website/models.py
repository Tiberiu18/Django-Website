from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django_resized import ResizedImageField
from djmoney.models.fields import MoneyField
import datetime 

# Create your models here.

now = datetime.datetime.now()

transmission_choices = [
	("manual", "manual"),
	("automatic", "automatic"),
]

fuel_choices = [
("diesel", "diesel"),
("petrol", "petrol"),
("electric", "electric"),
("hybrid", "hybrid"),
]

class Car(models.Model):
		car_maker 		= models.CharField(max_length	= 120)
		car_model		= models.CharField(max_length	= 120)
		header_image 	= models.ImageField(blank=False, upload_to="images/", default='images/default-img.jpg' )
		description		= models.TextField()
		eng_size		= models.PositiveIntegerField(validators=[MaxValueValidator(10000), MinValueValidator(300)]) 					# size of the engine
		year 			= models.PositiveIntegerField(validators=[MaxValueValidator(now.year), MinValueValidator(1960)]) 		# year of production
		transmission 	= models.CharField(choices=transmission_choices, max_length = 50)
		fuel_type 		= models.CharField(choices=fuel_choices, max_length = 50)
		image2 			= models.ImageField(blank=False, upload_to="images/", default='images/default-img.jpg' )
		image3 			= models.ImageField(blank=False, upload_to="images/", default='images/default-img.jpg' )
		price 			= MoneyField(
			decimal_places=2,
			default=0, 
			max_digits=11,
			default_currency='EUR',
			)
		kilometers		= models.PositiveIntegerField(validators=[MaxValueValidator(1000000), MinValueValidator(1000)], default=1000)
		def get_absolute_url(self):
			return reverse('website:car-detail', kwargs={'id':self.id})