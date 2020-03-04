from django.shortcuts import render
from rest_framework import serializers
from .models import *
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
