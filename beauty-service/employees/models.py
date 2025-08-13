from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(
        verbose_name='имя сотрудника',
        max_length=255
    )
    photo = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name