from django import forms
from django.db import models
from django.forms import fields
from .models import Forma

class FormationForm(forms.ModelForm):
    class Meta:
        model = Forma
        fields = "__all__"