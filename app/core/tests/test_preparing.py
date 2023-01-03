"""
Tests for preparing data.
"""
from django.test import TestCase
from core.services import preparing
from rest_framework.request import Request


EXAMPLE_DATA = {
    "message": {
        "attributes": {
            "key": "value"
        },
        "data": "eyJtZXNzYWdlIjoidGVzdCBtZXNzYWdlIn0=",
        "messageId": "2070443601311540",
        "message_id": "2070443601311540",
        "publishTime": "2021-02-26T19:13:55.749Z",
        "publish_time": "2021-02-26T19:13:55.749Z"
    },
    "subscription": "projects/myproject/subscriptions/mysubscription"
}


class PreparingModuleTests(TestCase):
    """Tests for preparing data module."""
    def setUp(self):
        self.request = Request
        self.request.data = EXAMPLE_DATA

    def test_prepare_data(self):
        data = preparing.prepare_data(self.request)
        expected_data = {"message": "test message"}
        self.assertEqual(data, expected_data)
