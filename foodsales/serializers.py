from rest_framework import serializers
from .models import restItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=restItem
        fields='__all__'