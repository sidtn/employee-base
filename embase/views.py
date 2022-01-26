from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from datetime import date
from.models import Employee as EmployeeObj


class Professions(LoginRequiredMixin, ListView):
    login_url = 'login'
    paginate_by = 13
    model = Position
    context_object_name = 'professions'
    template_name = 'embase/professions.html'


class Employees(LoginRequiredMixin, ListView):
    login_url = 'login'
    paginate_by = 13
    model = Employee
    context_object_name = 'employees'
    template_name = 'embase/employees.html'


class EmployeeCard(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Employee
    template_name = 'embase/employee_card.html'
    slug_url_kwarg = 'empl_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        how_long_works = date.today().year - self.get_object().employment_date.year
        context['years'] = how_long_works
        return context


class AddEmployee(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = AddEmployeeForm
    template_name = 'embase/add_employee.html'
    success_url = reverse_lazy('employees')


class UpdateEmployee(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Employee
    template_name = 'embase/edit_employee.html'
    fields = '__all__'
    slug_url_kwarg = 'empl_slug'
    success_url = reverse_lazy('employees')


class DeleteEmployee(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Employee
    success_url = reverse_lazy('employees')
    template_name = 'embase/delete_employee.html'
    slug_url_kwarg = 'empl_slug'


class Departments(LoginRequiredMixin, ListView):
    login_url = 'login'
    paginate_by = 13
    model = Department
    context_object_name = 'departments'
    template_name = 'embase/departments.html'


class AddDepartment(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = AddDepartmentForm
    template_name = 'embase/add_department.html'
    success_url = reverse_lazy('departments')


class DeleteDepartment(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Department
    success_url = reverse_lazy('departments')
    template_name = 'embase/delete_depart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_set_employees_of_department = EmployeeObj.objects.filter(department=self.object.pk)
        len_of_employees_query = len(query_set_employees_of_department)
        context['empls_of_depart'] = query_set_employees_of_department
        context['len_empl'] = len_of_employees_query
        print(context['len_empl'])
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'embase/login.html'

    def get_success_url(self):
        return reverse_lazy('employees')


def logout_user(request):
    logout(request)
    return redirect('login')

