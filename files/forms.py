from django import forms
from .models import ResponseSettings


class ResponseSettingsForm(forms.ModelForm):
    class Meta:
        model = ResponseSettings
        fields = '__all__'
