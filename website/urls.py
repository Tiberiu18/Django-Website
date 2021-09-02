from django.urls import path
from . import views 

app_name = 'website'
urlpatterns = [
	# path('', views.CarsListView.as_view(), name='CarsList'),
	path('car/<int:id>', views.CarDetailView.as_view(), name='car-detail'),
	path('contact/', views.contact, name='contact'),
	path('create-listing/', views.CreateListing.as_view(), name="CreateListing"),
	path('search/', views.search, name='search'),
	path('about/', views.about, name='about'),
	#path('create-listing/', views.car_create_view, name="CreateListing"),
	path('', views.CarList, name='CarsList'),
	path('<int:id>/edit/', views.CarUpdateView.as_view(), name="EditView"),
	path('<int:id>/delete/', views.delete_car, name="delete-car"),
]