from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serilizers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
# Create your views here.
