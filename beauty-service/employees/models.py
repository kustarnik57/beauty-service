from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(
        verbose_name='имя сотрудника'
    )
    photo = models.ImageField(null=True, blank=True)