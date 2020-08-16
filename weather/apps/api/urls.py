
from django.urls                                        import path, include


urlpatterns = [

    path('climate/',                    include('weather.apps.api.climate.urls')),

]
