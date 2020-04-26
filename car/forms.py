from django import forms

from .models import Car
from django.utils.translation import gettext_lazy as _


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = ['name', 'color]
        fields = '__all__'
        labels = {
            'name': _('Car Name'),
        }
        