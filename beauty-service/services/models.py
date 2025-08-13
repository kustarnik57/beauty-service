from django.db import models
from employees.models import EmployeeModel


class ServiceModel(models.Model):
    name = models.CharField(
        verbose_name='Название процедуры',
        max_length=255
        )
    price = models.FloatField(verbose_name='Цена')
    employees = models.ManyToManyField(EmployeeModel)

    def __str__(self):
        return self.name
    

class Record(models.Model):
    phone = models.CharField(max_length=25)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)