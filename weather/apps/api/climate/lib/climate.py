
from datetime                                           import datetime

from weather.apps.web.climate.models                    import Climate


def get_weather_data():

    city_labels   = []
    min_temp_list = []
    max_temp_list = []
    avg_temp_list = []
    humidity_list = []

    data_dict = {}

    weathers = Climate.objects \
                .values(
                    'city', 'weather_time', 'period_start', 'period_end', 'min_temp',
                    'max_temp', 'avg_temp', 'med_temp', 'humidity', 'description', 'icon',
                ) \
                .order_by(
                    'city'
                )

    for weather in weathers:

        if weather['city'] not in city_labels:
            city_labels.append(weather['city'])
            min_temp_list.append(weather['min_temp'])
            max_temp_list.append(weather['max_temp'])
            avg_temp_list.append(weather['avg_temp'])
            humidity_list.append(weather['humidity'])

    data_dict['city_labels']    = city_labels
    data_dict['min_temp_list']  = min_temp_list
    data_dict['max_temp_list']  = max_temp_list
    data_dict['avg_temp_list']  = avg_temp_list
    data_dict['humidity_list']  = humidity_list

    return data_dict
