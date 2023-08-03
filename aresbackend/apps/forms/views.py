from django.shortcuts import render
from aresbackend.apps.apiconfigs import BaseApiView

from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import BudgetForm
from .serializers import BudgetFormSerializer

class BudgetFormApiView(BaseApiView, viewsets.ModelViewSet):
    queryset = BudgetForm.objects.all()
    serializer_class = BudgetFormSerializer

    def destroy(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para deletar esses dados."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def update(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para alterar esses dados."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def retrieve(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para visualizar esses dados."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def list(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para visualizar esses dados."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)