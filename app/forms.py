from django import forms
from app.models import Config


class ConfigForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Config
        fields = '__all__'
