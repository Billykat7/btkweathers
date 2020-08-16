
from django.db                                          import models


class AuditFields(models.Model):

    datetime_created    = models.DateTimeField('DATE CREATED',  auto_now_add=True)
    datetime_updated    = models.DateTimeField('DATE UPDATED',  auto_now=True)
    last_updated_by     = models.CharField('LAST UPDATED BY',   max_length=50, blank=True, null=True)
    bool_deleted        = models.BooleanField('IS DELETED?',    default=False)

    class Meta:
        abstract = True
