
import requests
from datetime                                               import datetime

from django.conf                                            import settings
from rest_framework.views                                   import APIView
from rest_framework.reverse                                 import reverse

from rest_framework.response                                import Response

from weather.apps.web.climate.models                        import Climate
from weather.apps.api.climate.serializer                    import ClimateSerializer
from .lib                                                   import climate as climate_lib


class WeatherChartView(APIView):

    def get(self, request, format=None):

        data_dict = climate_lib.get_weather_data()

        data = {
            'labels'    :   data_dict['city_labels'],
            'data'      :   data_dict['avg_temp_list'],
        }

        return Response(data)
