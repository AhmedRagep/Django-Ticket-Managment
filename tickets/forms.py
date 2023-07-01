from django import forms
from .models import Tiecket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Tiecket
        fields = ['title','description']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Tiecket
        fields = ['title','description']