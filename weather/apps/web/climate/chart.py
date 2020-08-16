
from django.shortcuts                                   import render
from django.views.generic                               import View
from django.contrib                                     import messages
from django.http                                        import JsonResponse

from .lib.input                                         import input_get_input
from .lib                                               import climate as climate_lib


# Create your views here.
class WeatherChartView(View):
    template_name = 'apps/climate/chart.html'

    def get(self, request, **kwargs):

        context = {}

        return render(request, self.template_name, context)
