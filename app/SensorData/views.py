from SensorData.serializers import DataSerializer
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Device, SensorData


from core.services.preparing import prepare_data


class SensorDataAPI(APIView):
    """
    Sensor Data.
    """
    def post(self, request):
        """ Post data."""
        try:
            data = prepare_data(request)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = DataSerializer(data=data)
        serial_n = data.get('serial', None)

        if not Device.objects.filter(pk=serial_n).exists():
            raise serializers.ValidationError(
                'The serial number doesn`t exist.')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Get data."""
        sensordata = SensorData.objects.all()
        serializer = DataSerializer(sensordata, many=True)
        return Response(serializer.data)
