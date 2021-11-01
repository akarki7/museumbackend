from djano_filters import rest_framework as filters
from sites.models import Site, Videos, Photos

class SiteFilter(filters.FilterSet):
    file_name=filters.CharFilter(field_name="file_name")
    origin_date=filters.DateFilter(field_name="origin_date")
    serial_numer=filters.CharFilter(field_name="serial_numer")
    title =filters.CharFilter(field_name="title")
    
#file_name, origin_date, current_location, serial_number, time_period, title