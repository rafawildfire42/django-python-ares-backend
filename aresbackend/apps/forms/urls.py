# apps/forms/urls.py

from django.urls import path, include
from aresbackend.apps.forms.views import BudgetFormApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'budget-form', BudgetFormApiView, basename='budget_form')

urlpatterns = [
    path('', include(router.urls)),
]