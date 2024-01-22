from django.db import models
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    ID = models.IntegerField(primary_key=True, validators=[MaxValueValidator(5)])
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    BookingDate = models.DateField()
    
    def __str__(self):
        return self.Name  

class Menu(models.Model):
    ID = models.IntegerField(primary_key=True, validators=[MaxValueValidator(5)])
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.Title
