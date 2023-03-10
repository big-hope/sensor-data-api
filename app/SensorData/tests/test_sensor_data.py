"""
Tests for SensorData APIs.
"""
import base64
import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Device, SensorData


SENSOR_DATA_URL = reverse('sensor-data')

EXAMPLE_DATA = {
    "message": {
        "attributes": {
            "key": "value"
            },
        "data": "ewoJInNlcmlhbCI6ICIxMDAwMDAxMDAiLAoJInYw \
        IjogMTAwMDEzLAoJInYxOCI6IDIuNzIsCgkiVGltZSI6ICIyMD \
        IyLTExLTA4IDQ6MDA6MDQiCn0=",
        "messageId": "2070443601311540",
        "message_id": "2070443601311540",
        "publishTime": "2021-02-26T19:13:55.749Z",
        "publish_time": "2021-02-26T19:13:55.749Z"
    },
    "subscription": "projects/myproject/subscriptions/mysubscription"
}


def dict2b64(payload: dict) -> str:
    "Convert dict to base64"
    payload_bytes = json.dumps(payload).encode('utf-8')
    payload_b64_bytes = base64.b64encode(payload_bytes)
    return payload_b64_bytes.decode('utf-8')


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

        payload = {"serial": device.serial_number,
                   "v0": "100013",
                   "v18": "2.72",
                   "Time": "2022-11-08 4:00:04"
                   }

        payload_b64 = dict2b64(payload)
        EXAMPLE_DATA["message"]["data"] = payload_b64
        res = self.client.post(SENSOR_DATA_URL, EXAMPLE_DATA, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_data_with_not_exist_serial_number(self):
        """Test creating data with not-existing S/N."""

        not_existsing_sn = '00000001'
        payload = {
            "serial": not_existsing_sn,
            "v0": "100013",
            "v18": "2.72",
            "Time": "2022-11-08 4:00:04"
        }
        payload_b64 = dict2b64(payload)
        EXAMPLE_DATA["message"]["data"] = payload_b64

        res = self.client.post(SENSOR_DATA_URL, EXAMPLE_DATA, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data(self):
        """Test get data."""
        res = self.client.get(SENSOR_DATA_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
