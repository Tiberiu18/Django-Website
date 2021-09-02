from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, DetailView, CreateView, )
from .models import Car
from .forms import ContactForm, RawCarForm, CarForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.views.generic import (
    UpdateView,
)
from django.views import View

# Import pagination stuff
from django.core.paginator import Paginator


# Create your views here.


class CarsListView(ListView):
    template_name = "website/index.html"
    model = Car


def CarList(request):
    # car_list = Car.objects.all().order_by('?') Order cars random
    car_list = Car.objects.all()

    # Set up Pagination
    p = Paginator(car_list, 6)  # 6 Cars per Page
    page = request.GET.get('page')  
    cars = p.get_page(page)

    context = {
        "car_list": car_list,
        "cars": cars,
    }
    return render(request, 'website/index.html', context )
                  


def search(request):
    # car_list = Car.objects.all().order_by('?') Order cars random
    if not request.method == "POST": # For other pages except first page
        if 'searched' in request.session: # Transform searched to POST request
            request.POST = request.session['searched']
            request.method = "POST"

    if request.method == "POST":
        request.session['searched'] = request.POST
        searched = request.POST['searched']
        if " " in searched: # Case 1: when we have 2 words, one for car maker, one for car model, such as: Peugeot 508
            car_maker, car_model = searched.split(' ', 1) # Split the initial search in two words
            car_list = Car.objects.filter(car_maker__contains=car_maker, car_model__contains=car_model)
            if not car_list: # If no results, we move on to Case 2: When the order is inversed, like: 508 Peugeot
                car_model, car_maker = searched.split(' ', 1)
                car_list = Car.objects.filter(car_maker__contains=car_maker, car_model__contains=car_model)
                if not car_list: # If still no results, we assume Case 3: When we searched only for 2 words car model, like: Astra H
                    car_list = Car.objects.filter(car_model__contains=searched)
        else: # Case 4: When we have one word, we first make the search based on car maker, such as: Peugeot
            car_list = Car.objects.filter(car_maker__contains=searched)
            if not car_list: # Case 5: If no results, we search based on model, such as: 508
                car_list = Car.objects.filter(car_model__contains=searched)

        # Set up Pagination
        p = Paginator(car_list, 2)  # 6 Cars per Page
        page = request.GET.get('page')  # request basically
        cars = p.get_page(page)
        context = {
        "searched":searched,
        "car_list": car_list,
        "cars": cars,
    }
        return render(request, 'website/search.html', context)
    else:
        return render(request,'website/search.html', {})




class CarDetailView(DetailView):
    template_name = "website/car-detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Car, id=id_)


class CreateListing(CreateView):
    template_name = "website/create-listing.html"
    permission_required = ''
    model = Car
    fields = [
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


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Blabla"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
        try:
            send_mail(subject, message, 'ttiberiu48@yahoo.com',
                      ['ttiberiu48@yahoo.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header')
        return redirect("website:CarsList")

    form = ContactForm()
    return render(request, "website/contact.html", {'form': form})


def car_create_view(request):
    my_form = CarForm()
    if request.method == "POST":
        my_form = CarForm(request.POST, request.FILES)
        if my_form.is_valid():
            instance = my_form.save()
    context = {
        "form": my_form
    }

    return render(request, "website/create-listing.html", context)


def about(request):
    context = {}
    return render(request, "website/about.html", context)


class CarObjectMixin(object):
    model = Car

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CarUpdateView(CarObjectMixin, View):
    template_name = "website/car-update.html"

    def get(self, request, id=None, *args, **kwargs):  # function based view, render a template
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CarForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):  
        obj = self.get_object()
        if obj is not None:
            form = CarForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)


def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == "POST":
        car.delete()
        return redirect('../../')

    context = {
        "car": car
    }
    return render(request, "website/car-delete.html", context)
