from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serilizers import CompanySerializer,EmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
# Create your views here.
