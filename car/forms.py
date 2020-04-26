from django import forms
from django.forms import CharField, TextInput, Textarea, ModelChoiceField

from .models import Car, CarColor
from django.utils.translation import gettext_lazy as _


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'color']
        # fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': _('Car Name'),
        }