from django.contrib import admin

from cars.models import Brand, Car, Rental


# Register your models here.
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Rental)

