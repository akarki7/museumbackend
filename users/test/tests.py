from django.http import response
from django.test import TestCase
from users.models import User
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Create your tests here.

class TestUserCanSignIn(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(email = "testuser@gmail.com")
        self.user.set_password("12345")
        self.user.save()

    def test_sign_in(self):
        pre_request = APIRequestFactory()
        url = "/auth/token/"
        data = {
            "email" : "testuser@gmail.com",
            "password": "12345"
        }
        request = pre_request.post(url, data)
        response = TokenObtainPairView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(None, response.data.get("refresh", None))
        self.assertNotEqual(None, response.data.get("access", None))

    def test_token_refresh(self):
        pre_request = APIRequestFactory()
        url = "/auth/token/"
        data = {
            "email" : "testuser@gmail.com",
            "password": "12345"
        }
        request = pre_request.post(url, data)
        response = TokenObtainPairView.as_view()(request)
        refresh_token = response.data.get("refresh", None)
        self.assertNotEqual(refresh_token, None)
        url = "/auth/refresh/"
        data = {
            "refresh": refresh_token
        }
        request = pre_request.post(url, data)
        response = TokenRefreshView.as_view()(request)
        self.assertNotEqual(None, response.data.get("access", None))