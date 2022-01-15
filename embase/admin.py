from django.contrib import admin
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_create')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'department', 'employment_date')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
