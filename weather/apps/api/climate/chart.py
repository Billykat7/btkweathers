
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

        data_list = climate_lib.get_weather_data()

        min_temp_labels = list(data_list[0].keys())
        max_temp_labels = list(data_list[1].keys())
        avg_temp_labels = list(data_list[2].keys())
        humidity_labels = list(data_list[3].keys())

        min_temp_data   = list(data_list[0].values())
        max_temp_data   = list(data_list[1].values())
        avg_temp_data   = list(data_list[2].values())
        humidity_data   = list(data_list[3].values())

        data = {
            'min_temp_labels'       :   min_temp_labels,
            'min_temp_data'         :   min_temp_data,

            'max_temp_labels'       :   max_temp_labels,
            'max_temp_data'         :   max_temp_data,

            'avg_temp_labels'       :   avg_temp_labels,
            'avg_temp_data'         :   avg_temp_data,

            'humidity_labels'       :   humidity_labels,
            'humidity_data'         :   humidity_data,
        }

        print("data = ", data)

        return Response(data)
