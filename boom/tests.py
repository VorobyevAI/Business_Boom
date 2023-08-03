import uuid

import pytest
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import CustomUser
from rest_framework.test import APIRequestFactory
import json
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .views import UserAPIView

TEST_USER_NAME = "Jane Doe"
TEST_USER_EMAIL = "jane@example.org"
TEST_USER_PASSWORD = "123123asdad413242341daad"

class SimpleTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret" )
        return user



    def test_details(self):
        factory = APIRequestFactory()
        request = factory.post("/signup/",{"username": "jacob", "password": "top_secret"})


        assert request.status_code == 200



@pytest.mark.django_db
@require_http_methods(["POST"])
def login_view(request):
    body = json.loads(request.body.decode())
    user = authenticate(request, name=body["email"], password=body["password"])

    if user:
        login(request, user)
        return HttpResponse("OK")
    else:
        return HttpResponse("Unauthorized", status=401)



@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user(TEST_USER_NAME, TEST_USER_EMAIL, TEST_USER_PASSWORD)
    assert CustomUser.objects.count() == 1

@pytest.fixture
def sample_user():
    user = CustomUser.objects.create_user(TEST_USER_NAME, TEST_USER_EMAIL, TEST_USER_PASSWORD)
    return user


@pytest.mark.django_db
def test_login_fails_with_invalid_credentials(sample_user):
    client = Client()
    response = client.post(
        "/session/auth/login/",
        {"username": TEST_USER_NAME, "password": '12312312311233133123'},
        content_type="application/json",
    )
    assert response.status_code == 404
    assert "sessionid" not in client.cookies