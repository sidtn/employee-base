from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('professions/', Professions.as_view(), name='professions'),
    path('employee/<slug:empl_slug>/', Employee.as_view(), name='employee'),

]