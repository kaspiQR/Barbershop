from django.contrib import admin
from .models import (
    Position,
    Barber,
    Testimonial,
    Contact,
    Service,
    Subscribe,
    Appointment)


admin.site.register(Position)
admin.site.register(Barber)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Subscribe)
admin.site.register(Appointment)
