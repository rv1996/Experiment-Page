from django import forms
from .models import Experiment


class AddNewForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = [
            "title",
            "content",
            "image",
        ]
