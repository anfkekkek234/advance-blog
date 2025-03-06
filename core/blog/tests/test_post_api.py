from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def commen_user():
    user = User.objects.create_user(
        email="admin@gmail.com", password="jcjdjr2132@", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, commen_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        api_client.force_authenticate(user=commen_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(
        self, api_client, commen_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
        }
        api_client.force_authenticate(user=commen_user)
        response = api_client.post(url, data)
        assert response.status_code == 400
