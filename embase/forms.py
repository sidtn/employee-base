from django import forms
from .models import *


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
