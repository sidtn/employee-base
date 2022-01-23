from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название отдела')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания отдела')
    description = models.TextField(blank=True, verbose_name='Дополнительная информация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ['-date_create', 'name']


class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name='Должность')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name', ]


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО сотрудника')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Отдел')
    employment_date = models.DateField(auto_now_add=True, verbose_name='Дата приема на работу')

    def __str__(self):
        return f'{self.name} - {self.employment_date}'

    def get_absolute_url(self):
        return reverse('employee', kwargs={'empl_slug': self.slug})

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['-employment_date']




