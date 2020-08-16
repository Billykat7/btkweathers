
from django.db                                          import models
from django_countries.fields                            import CountryField

from core.model_mixins                                  import AuditFields


# Create your models here.
class Climate(AuditFields):

    city            = models.CharField('CITY',      max_length=255, blank=True, null=True)

    country         = CountryField('COUNTRY',                       blank=True, null=True)

    lat             = models.FloatField('LATITUDE',                 default=0.00)
    lng             = models.FloatField('LONGITUDE',                default=0.00)

    weather_time    = models.DateTimeField('WEATHER TIME',          blank=True, null=True)
    period_start    = models.DateTimeField('START PERIOD',          blank=True, null=True)
    period_end      = models.DateTimeField('END PERIOD',            blank=True, null=True)

    min_temp        = models.FloatField('MIN. TEMP',                default=0.00)
    max_temp        = models.FloatField('MAX. TEMP',                default=0.00)
    avg_temp        = models.FloatField('AVERAGE. TEMP',            default=0.00)
    med_temp        = models.FloatField('MEDIAN. TEMP',             default=0.00)

    humidity        = models.CharField('HUMIDITY',      max_length=200, blank=True, null=True)
    description     = models.CharField('DESCRIPTION',   max_length=200, blank=True, null=True)
    sunrise         = models.CharField('SUNRISE',       max_length=200, blank=True, null=True)
    sunset          = models.CharField('SUNSET',        max_length=200, blank=True, null=True)
    icon            = models.CharField('WEATHER ICON',  max_length=200, blank=True, null=True)

    class Meta:
        app_label   = 'climate'
        db_table    = 'btk_climates'

    def __str__(self):
        return self.city
