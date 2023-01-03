"""
Tests for models.
"""
from django.test import TestCase
# from core import models
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
