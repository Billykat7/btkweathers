from datetime                                           import datetime

from django.db.models                                   import Q

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
                        )

    return weathers
