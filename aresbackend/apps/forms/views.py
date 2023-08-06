from django.shortcuts import render
import re
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import BudgetForm
from .serializers import BudgetFormSerializer

class BudgetFormApiView(viewsets.ModelViewSet):
    queryset = BudgetForm.objects.all()
    serializer_class = BudgetFormSerializer

    def remove_punctuation(self, text):
        return re.sub(r'[^\d]', '', text)

    def create(self, request, *args, **kwargs):
        cpf = request.data.get('cpf')
        if cpf:
            request.data['cpf'] = self.remove_punctuation(cpf)

        phone = request.data.get('phone')
        if phone:
            request.data['phone'] = self.remove_punctuation(phone)

        print(request.data)

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para deletar esses dados."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def update(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para alterar esses dados."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    # def retrieve(self, request, *args, **kwargs):
    #     data = {"detail": "Você não possui permissão para visualizar esses dados."}
    #     return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def list(self, request, *args, **kwargs):
        data = {"detail": "Você não possui permissão para visualizar esses dados 123."}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)