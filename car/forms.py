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

        def __init__(self, *args, **kwargs):
            car_color = kwargs.pop('CarColor', '')
            self.fields['color'] = forms.ModelChoiceField(
                queryset=CarColor.objects.filter(id=2))
# class CarForm(forms.Form):
#     name = CharField(
#         required=True,
#         label="Car Name",
#         widget=TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#         # labels = {
#         #     'name': _('Car Name'),
#         # }
        