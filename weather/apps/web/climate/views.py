
import requests
from datetime                                           import datetime

from django.contrib                                     import messages
from django.shortcuts                                   import render
from django.views.generic                               import View

from weather.apps.web.climate.forms                     import ClimateForm
from weather.apps.web.climate.lib.input                 import input_get_input


# Create your views here.
class ClimateListView(View):
    template_name = 'apps/climate/index.html'

    def get(self, request, **kwargs):

        form = ClimateForm

        context = {}

        if request.GET:

            i = input_get_input(request)

            hostname = request.get_host()

            btk_api = f'http://{hostname}/api/climate/list/'

            city_req        = i['city']
            period_start    = i['period_start']
            period_end      = i['period_end']

            full_url = f"{btk_api}?city={city_req}&period_start={period_start}&period_end={period_end}"

            res         = requests.get(full_url)
            res_json    = res.json()

            if 'list' in res_json:
                if len(res_json['list']) > 0:
                    time = datetime.strptime(res_json['list'][0]['list_txt'], "%Y-%m-%dT%H:%M:%S")

                    weather = {
                        'city'          : res_json['city'],
                        'temperature'   : res_json['list'][0]['avg_temp'],
                        'description'   : res_json['list'][0]['description'],
                        'humidity'      : res_json['list'][0]['humidity'],
                        'icon'          : res_json['list'][0]['icon'],
                        'time'          : time,
                    }

                    context['weather'] = weather

                else:

                    messages.warning(request, "No data to report. Please, note that reports are at 3 hr intervals.")


            context['results'] = res_json

        context['form'] = form

        return render(request, self.template_name, context)
