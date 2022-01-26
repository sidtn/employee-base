from django.urls import path
from .views import *


urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('professions/', Professions.as_view(), name='professions'),
    path('departments/', Departments.as_view(), name='departments'),
    path('employees/', Employees.as_view(), name='employees'),
    path('add_employee/', AddEmployee.as_view(), name='add_employee'),
    path('employees/delete/<slug:empl_slug>/', DeleteEmployee.as_view()),
    path('employees/edit/<slug:empl_slug>/', UpdateEmployee.as_view()),
    path('employees/<slug:empl_slug>/', EmployeeCard.as_view(), name='employee'),
    path('add_department/', AddDepartment.as_view(), name='add_department'),
    path('departments/delete/<int:pk>/', DeleteDepartment.as_view()),
]
