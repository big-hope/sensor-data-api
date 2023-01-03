from rest_framework import serializers
from core.models import SensorData


class DataSerializer(serializers.ModelSerializer):
    """Serializer for data."""
    class Meta:
        model = SensorData
        fields = '__all__'
