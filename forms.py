from django import forms
from beach_management.models import EmpModel

class Empforms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields="__all__"