
from django.urls                                        import path

from weather.apps.web.climate.views                     import ClimateListView
from weather.apps.web.climate.weather                   import WeathersListView
from weather.apps.web.climate.chart                     import WeatherChartView


app_name = 'climate'

urlpatterns = [

    path('',                ClimateListView.as_view(),              name='home'),
    path('chart/',          WeatherChartView.as_view(),             name='chart'),
    path('list/',           WeathersListView.as_view(),             name='weather_list'),

]
