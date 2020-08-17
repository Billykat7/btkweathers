
from collections                                        import Counter

from weather.apps.web.climate.models                    import Climate


def get_weather_data():

    min_temp_list_ = []
    max_temp_list_ = []
    avg_temp_list_ = []
    humidity_list_ = []

    labels         = []
    data_list      = []

    weathers = Climate.objects \
                .values(
                    'city', 'weather_time', 'period_start', 'period_end', 'min_temp',
                    'max_temp', 'avg_temp', 'med_temp', 'humidity', 'description', 'icon',
                ) \
                .order_by(
                    'city'
                )

    for weather in weathers:

        labels.append(weather['city'])
        min_temp_list_.append(weather['min_temp'])
        max_temp_list_.append(weather['max_temp'])
        avg_temp_list_.append(weather['avg_temp'])
        humidity_list_.append(weather['humidity'])

    min_temp_dict = {}
    max_temp_dict = {}
    avg_temp_dict = {}
    humidity_dict = {}
    labels_count = Counter(labels)
    for city in labels:
        for (min_temp, max_temp, avg_temp, humidity) in zip(min_temp_list_, max_temp_list_, avg_temp_list_, humidity_list_):

            if city not in min_temp_dict:
                min_temp_dict[city] = min_temp
            else:
                min_temp_dict[city] = min_temp_dict[city] + min_temp

            if city not in max_temp_dict:
                max_temp_dict[city] = max_temp
            else:
                max_temp_dict[city] = max_temp_dict[city] + max_temp

            if city not in avg_temp_dict:
                avg_temp_dict[city] = avg_temp
            else:
                avg_temp_dict[city] = avg_temp_dict[city] + avg_temp

            if city not in humidity_dict:
                humidity_dict[city] = int(humidity)
            else:
                humidity_dict[city] = humidity_dict[city] + int(humidity)

            min_temp_list_.remove(min_temp)
            max_temp_list_.remove(max_temp)
            avg_temp_list_.remove(avg_temp)
            humidity_list_.remove(humidity)
            break

        min_temp_dict[city] = float(min_temp_dict[city])/int(labels_count[city])
        max_temp_dict[city] = float(max_temp_dict[city])/int(labels_count[city])
        avg_temp_dict[city] = float(avg_temp_dict[city])/int(labels_count[city])
        humidity_dict[city] = float(humidity_dict[city])/int(labels_count[city])

    data_list.append(min_temp_dict)
    data_list.append(max_temp_dict)
    data_list.append(avg_temp_dict)
    data_list.append(humidity_dict)

    return data_list
