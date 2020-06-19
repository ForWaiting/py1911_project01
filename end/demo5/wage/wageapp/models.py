from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=10,verbose_name='部门名')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=10,verbose_name='职工名')
    salary = models.PositiveIntegerField(default=0,verbose_name='工资')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name='部门',related_name='employees')

    def __str__(self):
        return self.name