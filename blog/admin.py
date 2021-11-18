from django.contrib import admin

# Register your models here.
from blog.models import Boat, Rent

admin.site.register(Boat)
admin.site.register(Rent)