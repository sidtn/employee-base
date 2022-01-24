from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('professions/', Professions.as_view(), name='professions'),
    path('departments/', Departments.as_view(), name='departments'),
    path('employees/<slug:empl_slug>/', Employees.as_view(), name='employees'),
    path('add_department/', AddDepartment.as_view(), name='add_department'),
    path('departments/<pk>/delete/', DeleteDepartment.as_view(), name='delete_depart'),

]