
from django.urls                                            import path

from weather.apps.api.climate.viewsets                      import weather_home, city_weather
from weather.apps.api.climate.chart                         import WeatherChartView


app_name = 'city_weather'

urlpatterns = [

    path('',                    weather_home,                   name = 'api_home'),
    path('chart/',              WeatherChartView.as_view(),     name='chart'),
    path('list/',               city_weather,                   name = 'list'),

]
