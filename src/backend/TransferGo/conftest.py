import pytest

import json
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()
