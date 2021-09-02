from django import forms
from .models import Car
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


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


class CarForm(forms.ModelForm):
	car_maker 		= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Car Maker'}), max_length= 80)
	car_model		= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Car Model'}), max_length = 80)
	header_image 	= forms.FileField(widget=forms.ClearableFileInput())
	image2 			= forms.FileField(widget=forms.ClearableFileInput())
	image3 			= forms.FileField(widget=forms.ClearableFileInput())
	class Meta:
		model 	= Car
		fields 	= [
		'car_maker',
		'car_model', 
		'description',
		'eng_size',
		'year',
		'transmission',
		'kilometers',
		'fuel_type',
		'price',
		'header_image',
		'image2',
		'image3'
		]

class ContactForm(forms.Form):
	first_name 		= forms.CharField(max_length=100)
	last_name 		= forms.CharField(max_length=100)
	email_address 	= forms.EmailField(max_length=150)
	message 		= forms.CharField(widget = forms.Textarea, max_length=2000)


class RawCarForm(forms.Form):
	car_maker 		= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Car Maker'}), max_length= 80)
	car_model		= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Car Model'}), max_length = 80)
	description 	= forms.CharField(widget=forms.Textarea)
	eng_size		= forms.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(550)])
	year 			= forms.IntegerField(validators=[MaxValueValidator(now.year), MinValueValidator(1976)])
	transmission 	= forms.ChoiceField(choices=transmission_choices)
	fuel_type 		= forms.ChoiceField(choices=fuel_choices)
	price 			= forms.IntegerField(validators=[MinValueValidator(0)])
	header_image 	= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
	image2 			= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
	image3 			= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))