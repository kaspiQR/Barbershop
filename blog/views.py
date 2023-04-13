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
