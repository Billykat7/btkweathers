
from django.urls                                        import path, include


urlpatterns = [

    path('',                    include('weather.apps.web.urls')),
    path('api/',                include('weather.apps.api.urls')),

]
