import os
import pytest
import django
from django.conf import settings
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

@pytest.fixture
def api_client():
    """
    This is API Client used to call API during unit tests
    :return:
    """
    return APIClient()
