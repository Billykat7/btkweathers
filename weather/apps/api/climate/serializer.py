
from rest_framework                                                     import serializers

from weather.apps.web.climate.models                                    import Climate


class ClimateSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Climate
        fileds  = '__all__'
