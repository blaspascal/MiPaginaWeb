from django import forms
from .models import mifotos

class mifotosForm(forms.ModelForm):
    class Meta:
        model = mifotos
        fields = '__all__'

