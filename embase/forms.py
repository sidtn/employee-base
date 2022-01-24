from django import forms
from .models import *


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

