"""
Prepare data for Serializer.
"""
import base64
import json


def prepare_data(request):
    envelope = request.data
    payload = base64.b64decode(envelope['message']['data'])
    data = json.loads(payload.decode('UTF-8'))
    return data
