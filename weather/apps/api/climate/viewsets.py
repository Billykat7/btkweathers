
import requests
from datetime                                               import datetime

from django.conf                                            import settings
from rest_framework.decorators                              import api_view
from rest_framework.reverse                                 import reverse

from rest_framework.response                                import Response

from weather.apps.web.climate.models                        import Climate
from weather.apps.api.climate.serializer                    import ClimateSerializer
from .lib.input                                             import input_get_input


# RETRIEVE VIEW
@api_view()
def weather_home(request):
	"""
	Welcome page of city weather API. Acceptable requests are in the following formats:

	 - city name: e.g. Paris
	 - period_start (start of time range): e.g. 07:00.
	 - period_end (end of time range): e.g. 16:00

	And the response is weather forcast for the chosen date time range.

	On the web, it would display the first results with the icon and the remaining in a table.
	"""
	return Response({
	'city_weather': reverse('city_weather:list', request=request),
	})


# class ClimateListAPIView(APIView):
@api_view()
def city_weather(request):

    user = request.user

    i = input_get_input(request)

    if user.is_authenticated:
        user = request.user.username

    api_key         = settings.OPENWEATHER_API_KEY
    city_req        = i['city']
    period_start    = i['period_start']
    period_end      = i['period_end']

    try:

        # url         = 'http://api.openweathermap.org/data/2.5/weather'
        url             = 'http://api.openweathermap.org/data/2.5/forecast'
        full_url        = f'{url}?q={city_req}&units=metric&APPID={api_key}'

        now     = datetime.now()
        today   = datetime.today().strftime('%Y-%m-%d')

        if city_req and period_start and period_end:

            period_start_lst = period_start.split(':')
            period_end_lst   = period_end.split(':')

            period_start     = f"{today}T{period_start}"
            period_end       = f"{today}T{period_end}"

            period_start_hrs = int(period_start_lst[0])
            period_start_min = int(period_start_lst[1])
            period_end_hrs   = int(period_end_lst[0])
            period_end_min   = int(period_end_lst[1])

            if period_start_hrs >= 24 or period_end_hrs >= 24:
                return Response({"bad_request": "Hour value must be less than 24"})
            if period_start_min >= 60 or period_end_min >= 60:
                return Response({"bad_request": "Minute value must be less than 60"})

            period_start = datetime.strptime(period_start, "%Y-%m-%dT%H:%M")
            period_end = datetime.strptime(period_end, "%Y-%m-%dT%H:%M")

            if period_start < period_end and period_start > now:

                res = requests.get(full_url)
                res_json = res.json()

                if res_json["cod"] == '200':

                    weather_dict = {}
                    weather_list = []

                    sunrise_ts  = res_json['city']['sunrise']
                    sunset_ts   = res_json['city']['sunset']
                    sunrise     = datetime.utcfromtimestamp(int(sunrise_ts)).strftime('%Y-%m-%d %H:%M:%S')
                    sunset      = datetime.utcfromtimestamp(int(sunset_ts)).strftime('%Y-%m-%d %H:%M:%S')

                    weather_dict['city']        = res_json['city']['name']
                    weather_dict['lat']         = res_json['city']['coord']['lat']
                    weather_dict['lng']         = res_json['city']['coord']['lon']
                    weather_dict['sunrise']     = sunrise
                    weather_dict['sunset']      = sunset
                    weather_dict['population']  = res_json['city']['population']
                    weather_dict['country']     = res_json['city']['country']

                    min_temp_list = []
                    max_temp_list = []
                    avg_temp_list = []
                    med_temp_list = []
                    humidity_list = []

                    for result in res_json['list']:

                        weather_time = datetime.strptime(result['dt_txt'], "%Y-%m-%d %H:%M:%S")

                        if period_start <= weather_time <= period_end:

                            dt = result['dt']
                            w_dict = {}

                            w_dict['avg_temp']    = result['main']['temp']
                            w_dict['feels_like']  = result['main']['feels_like']
                            w_dict['temp_min']    = result['main']['temp_min']
                            w_dict['temp_max']    = result['main']['temp_max']
                            w_dict['pressure']    = result['main']['pressure']
                            w_dict['description'] = result['weather'][0]['description']
                            w_dict['icon']        = result['weather'][0]['icon']
                            w_dict['wind_speed']  = result['wind']['speed']
                            w_dict['list_txt']    = weather_time
                            w_dict['humidity']    = result['main']['humidity']

                            weather_list.append(w_dict)

                            min_temp = w_dict['temp_min']
                            max_temp = w_dict['temp_max']
                            avg_temp = w_dict['avg_temp']
                            med_temp = (w_dict['temp_min'] + w_dict['temp_max'])/2
                            humidity = w_dict['humidity']

                            min_temp_list.append(min_temp)
                            max_temp_list.append(max_temp)
                            avg_temp_list.append(avg_temp)
                            med_temp_list.append(med_temp)
                            humidity_list.append(humidity)

                            city_weather, created = Climate.objects.get_or_create(
                                city            = weather_dict['city'],
                                country         = weather_dict['country'],
                                lat             = weather_dict['lat'],
                                lng             = weather_dict['lng'],
                                weather_time    = weather_time,
                                period_start    = period_start,
                                period_end      = period_end,
                                min_temp        = w_dict['temp_min'],
                                max_temp        = w_dict['temp_max'],
                                avg_temp        = w_dict['avg_temp'],
                                med_temp        = med_temp,
                                humidity        = w_dict['humidity'],
                                description     = w_dict['description'],
                                icon            = w_dict['icon'],
                                sunrise         = weather_dict['sunrise'],
                                sunset          = weather_dict['sunset'],
                                last_updated_by = user,

                                defaults        = {
                                    'city'          : weather_dict['city'],
                                    # 'avg_temp'      : w_dict['avg_temp'],
                                    'weather_time'  : weather_time
                                }

                            )

                    weather_dict['list'] = weather_list

                    if len(min_temp_list) > 0:
                        weather_dict['avg_min_temp'] = sum(min_temp_list)/len(min_temp_list)
                    if len(max_temp_list) > 0:
                        weather_dict['avg_max_temp'] = sum(max_temp_list)/len(max_temp_list)
                    if len(avg_temp_list) > 0:
                        weather_dict['avg_avg_temp'] = sum(avg_temp_list)/len(avg_temp_list)
                    if len(med_temp_list) > 0:
                        weather_dict['avg_med_temp'] = sum(med_temp_list)/len(med_temp_list)
                    if len(humidity_list) > 0:
                        weather_dict['avg_humidity'] = sum(humidity_list)/len(humidity_list)

                    print("weather_dict = ", weather_dict)

                    return Response(weather_dict)

                else:

                    return Response(res_json)

            elif period_start < now:

                return Response({"bad_request": "'Period Start' cannot be in the past."})

            else:

                return Response({"bad_request": "'Period Start' must be less than 'Period End'"})

        else:

            return Response({"waiting": "waiting on data to be submitted or some fields are missing"})


    except Exception as e:

        return Response({"error": "error occurred. Pls, check values and try again"})
