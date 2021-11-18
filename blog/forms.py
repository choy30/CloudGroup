from django import forms
from django.forms import DateInput

from blog.models import Boat, Rent

class DateInput(forms.DateInput):
    input_type = 'date'
class BoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        fields = ('name', 'owner', 'description', 'built', 'length', 'price', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'owner': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'built': forms.NumberInput(attrs={'class':'form-control'}),
            'length': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }
class UpdateBoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        fields = ('description', 'built', 'length', 'price', 'address')
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'built': forms.NumberInput(attrs={'class':'form-control'}),
            'length': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('renter', 'boat', 'start_date', 'end_date')
        widgets = {
            'renter': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'renter', 'type':'hidden'}),
            'boat': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'boat', 'type':'hidden'}),
            'start_date': DateInput(),
            'end_date': DateInput(),
        }