"""
Tests for SensorData APIs.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Device, SensorData


SENSOR_DATA_URL = reverse('sensor-data')


def create_device():
    """Create device with S/N."""
    device = Device.objects.create(
        serial_number='100000100'
    )
    return device


def create_data():
    """Create and return a sample sensor data."""
    defaults = {
        'serial': '100000100',
        'v0': 100013,
        'v18': 2.72,
        'Time': "2022-11-08 4:00:04",
    }

    sensor_data = SensorData.objects.create(**defaults)
    return sensor_data


class SensorDataAPITests(TestCase):
    """Test API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_create_data_with_exist_serial_number(self):
        """Test post data."""
        device = create_device()

        payload = {
            "serial": device.serial_number,
            "v0": "100013",
            "v18": "2.72",
            "Time": "2022-11-08 4:00:04"
        }
        res = self.client.post(SENSOR_DATA_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
