# import re
# from rest_framework import generics, parsers
# from rest_framework.response import Response

# class CamelCaseToSnakeCaseParser(parsers.JSONParser):
#     def parse(self, stream, media_type=None, parser_context=None):
#         data = super().parse(stream, media_type, parser_context)
#         return self.camel_to_snake(data)

# class BaseApiView(generics.GenericAPIView):
#     parser_classes = [CamelCaseToSnakeCaseParser]

#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#         if isinstance(response, Response) and response.data:
#             if request.method == 'GET':
#                 response.data = self.to_frontend(response.data)  # Convert data from snake_case to camelCase
#             elif request.method == 'POST' and response.status_code >= 400:
#                 response.data = self.to_frontend(response.data)  # Convert error response from snake_case to camelCase
#         return response

#     def camel_to_snake(self, data):
#         if isinstance(data, dict):
#             new_data = {}
#             for key, value in data.items():
#                 new_key = re.sub(r'(?<!^)(?=[A-Z])', '_', key).lower()
#                 new_data[new_key] = self.camel_to_snake(value)
#             return new_data
#         elif isinstance(data, list):
#             return [self.camel_to_snake(item) for item in data]
#         else:
#             return data

#     def snake_to_camel(self, data):
#         if isinstance(data, dict):
#             new_data = {}
#             for key, value in data.items():
#                 parts = key.split('_')
#                 new_key = parts[0] + ''.join(part.capitalize() for part in parts[1:])
#                 new_data[new_key] = self.snake_to_camel(value)
#             return new_data
#         elif isinstance(data, list):
#             return [self.snake_to_camel(item) for item in data]
#         else:
#             return data

#     def from_frontend(self, data):
#         """
#         Converte os nomes de campo do frontend (camelCase) para o backend (snake_case).
#         """
#         return self.camel_to_snake(data)

#     def to_frontend(self, data):
#         """
#         Converte os nomes de campo do backend (snake_case) para o frontend (camelCase).
#         """
#         return self.snake_to_camel(data)
