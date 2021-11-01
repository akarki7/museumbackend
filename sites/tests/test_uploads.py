from django.conf import settings
from django.http import request
from django.test import TestCase, Client
from sites.models import Photos, Site, Videos
from sites.views import SitesViewSet
from users.models import User
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from datetime import datetime
from unittest import TestCase as unit_testcase
import os

# Create your tests here.


class TestFrontendDataTransfer(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email = "testuser@gmail.com")
        self.user.set_password("12345")
        self.user.save()
        self.preexisting_site = Site.objects.create(
            serial_number=1,
            title="BurgerPark",
            file_name="Keine Ahnung",
            file_type=".docx",
            original_scan="false",
            time_period="G1",
            origin_date="2021-01-11",
            author="Dr Frank",
            size=10,
            description="Dummy_file",
            source="The Brains",
            signature="IDK",
            copyright_status="present",
            current_location="Muenchen",
            found_by="Herr Mueller",
            found_date="2000-01-01",
            production_date="2005-05-05",
            additional_info="Nothing more to add"
        )
        self.number_of_sites = Site.objects.count()
        self.client = APIClient()
        url = "/auth/token/"
        response = self.client.post(url , {"email": "testuser@gmail.com", "password":"12345"})
        token = response.data.get("access", None)
        self.assertIsNotNone(token)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+token)
    
    def test_site_creation(self):
        with open('./sites/tests/media_files_for_test/test_preview.txt', 'rb') as preview_file:
            pre_request = APIRequestFactory()
            request_url = "api/sites/"
            view = SitesViewSet.as_view({"post": "create"})
            site_data={
                    "serial_number": "0",
                    "title": "JUB",
                    "file_name": "Hello World",
                    "file_type": "txt",
                    "original_scan": "true",
                    "time_period" : "FL",
                    "origin_date": "2021-01-08",
                    "preview": preview_file,
                    "author": "Prof Frankenstein",
                    "size": 20,
                    "description": "Testing file",
                    "source": "The Brains",
                    "signature": "IDK",
                    "copyright_status": "present",
                    "current_location" : "Bremen Kunsthalle",
                    "found_by": "Mr Bones",
                    "found_date": "2000-01-01",
                    "production_date": "2005-05-05",
                    "additional_info": "Nothing more to add"
                }
            request = pre_request.post(
                request_url,
                data=site_data,
            )
            force_authenticate(request, user=self.user)
            response = view(request)
            self.assertEqual(response.status_code, 201)

            fields_not_being_checked = [
                "preview",
                "photos",
                "videos"
            ]

            date_fields = [
                "origin_date",
                "found_date",
                "production_date"
            ]

            for key, value in response.data.items():
                if key in date_fields:
                    self.assertEqual(datetime.strptime(value, "%Y-%m-%d"), datetime.strptime(site_data[key], "%Y-%m-%d"))
                elif key not in fields_not_being_checked:
                    self.assertEqual(value, site_data[key])

            self.assertEqual(self.number_of_sites + 1, Site.objects.count())
            file_url = response.data["preview"]
            user = Client()
            user.login(email="testuser@gmail.com", password="12345")
            response = user.get(file_url)
            self.assertEqual(response.status_code, 200)

    def test_photo_attachment_detachment(self):

        with open("./sites/tests/media_files_for_test/jasmine.jpeg", "rb") as jasmine:
            response = self.client.post(f"/api/sites/{self.preexisting_site.serial_number}/photos/", data={"file": jasmine, "name":"jasmine"})
            self.assertEqual(201, response.status_code)
            self.assertEqual("Photo attached", response.data.get("detail"))
        
        self.assertEqual(self.preexisting_site.photos.count(), 1)
        id = self.preexisting_site.photos.first().id
        response = self.client.delete(f"/api/sites/{self.preexisting_site.serial_number}/photos/", data={"photo_id":id})
        self.assertEqual(204, response.status_code)
        self.assertEqual(0, self.preexisting_site.photos.count())

    
    def test_video_attachment_detachment(self):

        with open("./sites/tests/media_files_for_test/1_screaming_sheep.mp4", "rb") as sheep:
            response = self.client.post(f"/api/sites/{self.preexisting_site.serial_number}/videos/", data={"file": sheep, "name":"sheep1"})
            self.assertEqual(201, response.status_code)
            self.assertEqual("Video attached", response.data.get("detail"))

        with open("./sites/tests/media_files_for_test/2_screaming_sheeps.mp4", "rb") as sheep:
            response = self.client.post(f"/api/sites/{self.preexisting_site.serial_number}/videos/", data={"file": sheep, "name":"sheep2"})
            self.assertEqual(201, response.status_code)
            self.assertEqual("Video attached", response.data.get("detail"))

        self.assertEqual(self.preexisting_site.videos.count(), 2)
        id = self.preexisting_site.videos.first().id
        response = self.client.delete(f"/api/sites/{self.preexisting_site.serial_number}/videos/", data={"video_id":id})
        self.assertEqual(1, self.preexisting_site.videos.count())

    def tearDown(self) -> None:
        self.preexisting_site.delete()