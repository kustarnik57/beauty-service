from django import forms
from services.models import Record

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'service': forms.HiddenInput(),
        }