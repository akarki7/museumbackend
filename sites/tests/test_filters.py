from django.test.testcases import TestCase
import pytest
from datetime import date,datetime,timedelta
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from sites.models import Site, Videos, Photos, TimePeriod
from sites.views import SitesViewSet
from users.models import User

@pytest.mark.django_db
class TestSiteFilter(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email = "testuser@gmail.com")
        self.user.set_password("12345")
        self.user.save()

        self.preexisting_site_1 = Site.objects.create(
            serial_number=1,
            title="BurgerPark",
            file_name="VGS",
            file_type=".docx",
            original_scan="false",
            time_period=TimePeriod.FL,
            origin_date=date.today(),
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
        self.preexisting_site_2 = Site.objects.create(
            serial_number=2,
            title="Vegesack",
            file_name="LAX",
            file_type=".docx",
            original_scan="false",
            time_period=TimePeriod.FL,
            origin_date=date.today(),
            author="Dr Khan",
            size=10,
            description="Dummy_test",
            source="The Eternals",
            signature="IDK",
            copyright_status="present",
            current_location="Bremen",
            found_by="Herr Mueller",
            found_date="2002-10-06",
            production_date="2005-05-05",
            additional_info="Nothing more to add"
        )
        self.preexisting_site_3 = Site.objects.create(
            serial_number=3,
            title="Vegesack",
            file_name="LAX",
            file_type=".docx",
            original_scan="false",
            time_period=TimePeriod.G1,
            origin_date=date.today() + timedelta(days=10),
            author="Dr Khan",
            size=10,
            description="Dummy_test",
            source="The Eternals",
            signature="IDK",
            copyright_status="present",
            current_location="Bremen",
            found_by="Herr Mueller",
            found_date="2002-10-06",
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
    
    def test_filter_title_yields_no_results(self):
        fake_title="Holalala"
        response= self.client.get(f"/api/sites/?title={fake_title}")
        assert response.status_code == 200
        assert len(response.data)==0

    def test_filter_title_yields_one_results(self):
        fake_title="BurgerPark"
        response= self.client.get(f"/api/sites/?title={fake_title}")
        assert response.status_code == 200
        assert len(response.data)==1
            
    def test_filter_title_yields_two_results(self):
        fake_title="Vegesack"
        response= self.client.get(f"/api/sites/?title={fake_title}")
        assert response.status_code == 200
        assert len(response.data)==2

    def test_filter_file_name_yields_no_results(self):
        fake_name="Holalala"
        response= self.client.get(f"/api/sites/?file_name={fake_name}")
        assert response.status_code == 200
        assert len(response.data)==0

    def test_filter_file_name_yields_one_results(self):
        fake_name="VGS"
        response= self.client.get(f"/api/sites/?file_name={fake_name}")
        assert response.status_code == 200
        assert len(response.data)==1
            
    def test_filter_file_name_yields_two_results(self):
        fake_name="LAX"
        response= self.client.get(f"/api/sites/?file_name={fake_name}")
        assert response.status_code == 200
        assert len(response.data)==2

    def test_filter_origin_date_yields_no_results(self):
        fake_date=date.today() + timedelta(days=2)
        response= self.client.get(f"/api/sites/?origin_date={fake_date}")
        assert response.status_code == 200
        assert len(response.data)==0

    def test_filter_origin_date_yields_one_results(self):
        fake_date=date.today() + timedelta(days=10)
        response= self.client.get(f"/api/sites/?origin_date={fake_date}")
        assert response.status_code == 200
        assert len(response.data)==1
            
    def test_filter_origin_date_yields_two_results(self):
        fake_date=date.today()
        response= self.client.get(f"/api/sites/?origin_date={fake_date}")
        assert response.status_code == 200
        assert len(response.data)==2

    def test_filter_serial_number_yields_no_results(self):
        fake_num=65
        response= self.client.get(f"/api/sites/?serial_number={fake_num}")
        assert response.status_code == 200
        assert len(response.data)==0

    def test_filter_serial_number_yields_one_results(self):
        fake_num=2
        response= self.client.get(f"/api/sites/?serial_number={fake_num}")
        assert response.status_code == 200
        assert len(response.data)==1

    def test_filter_time_period_yields_no_results(self):
        fake_period=TimePeriod.DP
        response= self.client.get(f"/api/sites/?time_period={fake_period}")
        assert response.status_code == 200
        assert len(response.data)==0

    def test_filter_time_period_yields_one_results(self):
        fake_period=TimePeriod.G1
        response= self.client.get(f"/api/sites/?time_period={fake_period}")
        assert response.status_code == 200
        assert len(response.data)==1
            
    def test_filter_time_period_yields_two_results(self):
        fake_period=TimePeriod.FL
        response= self.client.get(f"/api/sites/?time_period={fake_period}")
        assert response.status_code == 200
        assert len(response.data)==2


    