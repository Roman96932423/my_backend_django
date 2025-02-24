from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateField, ForeignKey, IntegerField, CASCADE


class Brand(Model):
    name = CharField(max_length=15)
    date_of_founding = DateField()

    def __str__(self):
        return f'{self.name}'


class Car(Model):
    brand = ForeignKey(Brand, on_delete=CASCADE)
    model = CharField(max_length=15)
    year_build = DateField()
    VIN = CharField(max_length=100)
    mileage = IntegerField()

    def __str__(self):
        return f'{self.brand} | {self.model} | {self.year_build}'


class Rental(Model):
    car = ForeignKey(Car, on_delete=CASCADE)
    # user = ForeignKey(User, on_delete=CASCADE)
    date_rented = DateField()
    date_returned = DateField()
    price_per_day = IntegerField()
