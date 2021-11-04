from django_filters import rest_framework as filters
from sites.models import Site, TimePeriod
from rest_framework.permissions import IsAuthenticated

class SiteFilter(filters.FilterSet):

    permission_classes = [IsAuthenticated]

    file_name=filters.CharFilter(field_name="file_name")
    origin_date=filters.DateFilter(field_name="origin_date")
    serial_number=filters.CharFilter(field_name="serial_number")
    title =filters.CharFilter(field_name="title")
    time_period = filters.ChoiceFilter(field_name="time_period", choices=TimePeriod.choices)

    class Meta:
        model= Site
        fields=(
            "file_name",
            "origin_date",
            "serial_number",
            "title",
            "time_period",
        )