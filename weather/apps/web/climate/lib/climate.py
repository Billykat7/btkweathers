from datetime                                           import datetime

from django.db.models                                   import Q, Sum

from weather.apps.web.climate.models                    import Climate


def get_weathers(i):

    city_req        = i['city']
    period_start    = i['period_start']
    period_end      = i['period_end']

    now     = datetime.now()
    today   = datetime.today().strftime('%Y-%m-%d')

    period_start    = f"{today}T{period_start}"
    period_end      = f"{today}T{period_end}"

    weathers = Climate.objects \
                        .values(
                            'city', 'weather_time', 'period_start', 'period_end', 'min_temp',
                            'max_temp', 'avg_temp', 'med_temp', 'humidity', 'description', 'icon'
                        ) \
                        .order_by('city')

    if city_req and period_start and period_end:
        period_start    = datetime.strptime(period_start, "%Y-%m-%dT%H:%M")
        period_end      = datetime.strptime(period_end, "%Y-%m-%dT%H:%M")

        weathers = weathers \
                        .filter(
                            Q(city=i['city']) &
                            Q(period_end__gte=period_end)
                        ) \
                        .values_list(
                            'city', 'weather_time', 'period_start', 'period_end', 'min_temp',
                            'max_temp', 'avg_temp', 'med_temp', 'humidity', 'description', 'icon',
                        ) \
                        .order_by('city')

    return weathers


def get_weather_sum(weathers):

    city_labels   = []
    min_temp_list = []
    max_temp_list = []
    avg_temp_list = []
    humidity_list = []

    data_dict = {}

    # if city_req and period_start and period_end:
    #     period_start = datetime.strptime(period_start, "%Y-%m-%dT%H:%M")
    #     period_end = datetime.strptime(period_end, "%Y-%m-%dT%H:%M")

    weathers = weathers \
                .values(
                    'city', 'weather_time', 'period_start', 'period_end', 'min_temp',
                    'max_temp', 'avg_temp', 'med_temp', 'humidity', 'description', 'icon',
                ) \
                .order_by(
                    'city'
                )

    for weather in weathers:
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

    print("data_dict = ", data_dict)

    return data_dict
