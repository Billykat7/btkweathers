
from django.shortcuts                                   import render
from django.views.generic                               import View
from django.contrib                                     import messages

from .lib.input                                         import input_get_input
from .lib                                               import climate as climate_lib


# Create your views here.
class WeathersListView(View):
    template_name = 'apps/climate/weather_list.html'

    def get(self, request, **kwargs):

        context = {}

        i = input_get_input(request)

        if request.GET:

            weathers = climate_lib.get_weathers(i)

        else:

            weathers = climate_lib.get_weathers(i)

        context['weathers'] = weathers

        return render(request, self.template_name, context)
