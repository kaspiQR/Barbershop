from django.shortcuts import render
from .models import (
    Position,
    Barber,
    Testimonial,
    Contact,
    Service,
    Subscribe,
    Appointment)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def appointment(request):
    return render(request, 'appointment.html')


def barbers(request):
    return render(request, 'barbers.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    service_list = Service.objects.all()
    context = {
        'services': service_list
    }
    return render(request, 'services.html', context=context)
