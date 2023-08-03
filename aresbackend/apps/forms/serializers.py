# No arquivo serializers.py do seu aplicativo

from rest_framework import serializers
from .models import BudgetForm

class BudgetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetForm
        fields = '__all__'
