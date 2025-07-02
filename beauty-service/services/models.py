from django.db import models
from employees.models import EmployeeModel


class ServiceModel(models.Model):
    name = models.CharField(verbose_name='Название процедуры')
    price = models.FloatField(verbose_name='Цена')
    Employees = models.ManyToManyField(EmployeeModel)