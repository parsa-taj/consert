from django import forms
from .models import *


class SearchForm(forms.Form):
    consert_name = forms.CharField(
        label='consert name', max_length=100, required=False)


class ConsertForm(forms.ModelForm):
    class Meta:
        model = Consert
        fields = ['name', 'singer_name', 'length', 'poster', ]
        # we can use excludes insted
        # excludes=['']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class TimeConsertForm(forms.ModelForm):
    class Meta:
        model = TimeConsert
        fields = ['start_time', 'seats']

class ConsertsInUserLocationForm(forms.Form):
    location = forms.CharField(label="your location", max_length=50, required=True)
    
