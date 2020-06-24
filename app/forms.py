from django import forms
from app.models import Config


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'
