import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Boat(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    built = models.IntegerField()
    length = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    boat_image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/no_image.jpg')

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/images/no_image.jpg"

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


