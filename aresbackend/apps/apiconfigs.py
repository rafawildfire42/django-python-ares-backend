from rest_framework import generics
from rest_framework.response import Response
import re

class BaseApiView(generics.GenericAPIView):
  def camel_to_snake(self, data):
    """
    Converte os nomes de campo de camelCase para snake_case.
    """
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            new_key = re.sub(r'(?<!^)(?=[A-Z])', '_', key).lower()
            new_data[new_key] = self.camel_to_snake(value)
        return new_data
    elif isinstance(data, list):
        return [self.camel_to_snake(item) for item in data]
    else:
        return data

  def snake_to_camel(self, data):
    """
    Converte os nomes de campo de snake_case para camelCase.
    """
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            new_key = ''.join([part.capitalize() for part in key.split('_')])
            new_data[new_key] = self.snake_to_camel(value)
        return new_data
    elif isinstance(data, list):
        return [self.snake_to_camel(item) for item in data]
    else:
        return data

  def from_frontend(self, data):
    """
    Converte os nomes de campo do frontend (camelCase) para o backend (snake_case).
    """
    return self.camel_to_snake(data)

  def to_frontend(self, data):
    """
    Converte os nomes de campo do backend (snake_case) para o frontend (camelCase).
    """
    return self.snake_to_camel(data)

  def get_response(self, data, status=200):
    """
    Retorna uma resposta JSON formatada para o frontend.
    """
    return Response(self.to_frontend(data), status=status)
