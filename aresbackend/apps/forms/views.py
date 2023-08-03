from django.shortcuts import render
from aresbackend.apps.apiconfigs import BaseApiView

from rest_framework import status, viewsets
from .models import BudgetForm
from .serializers import BudgetFormSerializer

class BudgetFormApiView(viewsets.ModelViewSet, BaseApiView):
    queryset = BudgetForm.objects.all()
    serializer_class = BudgetFormSerializer