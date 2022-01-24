from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Position, Department, Employee
from .forms import *


def index(request):
    return render(request, 'embase/base.html')


class Professions(ListView):
    paginate_by = 13
    model = Position
    context_object_name = 'professions'
    template_name = 'embase/professions.html'


class Employees(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'embase/employee.html'
    slug_url_kwarg = 'empl_slug'


class Departments(ListView):
    paginate_by = 13
    model = Department
    context_object_name = 'departments'
    template_name = 'embase/departments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class AddDepartment(CreateView):
    form_class = AddDepartmentForm
    template_name = 'embase/add_department.html'
    success_url = reverse_lazy('departments')


class DeleteDepartment(DeleteView):
    model = Department
    success_url = reverse_lazy('departments')
    template_name = 'embase/delete_depart.html'


