from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import SignUpViewset, ListUsersViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

router = DefaultRouter()
router.register(r"signup", SignUpViewset, basename="signup")
router.register(r"snoop", ListUsersViewSet, basename="snoopy")

urlpatterns += router.urls