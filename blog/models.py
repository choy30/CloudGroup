import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Boat(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    built = models.IntegerField()
    length = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.CharField(max_length=250)



class Rent(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=1))

    def total_days(self):
        day = self.end_date - self.start_date
        return day.days
    def total_price(self):
        return self.total_days() * self.boat.price