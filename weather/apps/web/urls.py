
from django.urls                                        import path, include


urlpatterns = [

    path('',                    include('weather.apps.web.climate.urls')),

]
