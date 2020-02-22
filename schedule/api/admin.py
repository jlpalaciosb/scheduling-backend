from django.contrib import admin
from schedule.api.models import Service, Client, Professional, Appointment

# Register your models here.
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Professional)
admin.site.register(Appointment)
