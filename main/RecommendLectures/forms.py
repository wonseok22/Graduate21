from django import forms
from .models import *

class LecturesForm(forms.ModelForm):
    class Meta:
        model = models