"""
Tests for models.
"""
from django.test import TestCase
from core import models
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""
    def test_create_user__successful(self):
        """Testing creating a user with email is successful"""
        username = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_create_device(self):
        """Test creating a Device is successful."""

        device = models.Device.objects.create(
            serial_number='000000001'
        )

        self.assertEqual(str(device), device.serial_number)

    def test_create_data(self):
        """Test creating a Device data."""

        data = models.SensorData.objects.create(
            v0='100013',
            v18='2.72',
            Time='2022-11-08 4:00:04'
        )
        self.assertEqual(str(data), data.v0)
