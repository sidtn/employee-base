from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


def index(request):
    return render(request, 'embase/base.html')


class Professions(ListView):
    model = Position
    template_name = 'embase/embase.html'


class Employee(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'embase/employee.html'
    slug_url_kwarg = 'empl_slug'

