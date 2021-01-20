from django.core.exceptions import ValidationError
from django.db import models

from services.helpers.faker_factory import Field
from django.utils.translation import ugettext_lazy as _

from random import randint


class SchemaColumn(models.Model):
    name = models.CharField(max_length=40)
    column_id = models.ForeignKey('Column', on_delete=models.CASCADE)
    schema_id = models.ForeignKey('DataSchema', on_delete=models.CASCADE)
    range_min = models.IntegerField(default=0)
    range_max = models.IntegerField(default=0)
    order = models.IntegerField(default=0)

    def clean(self):
        if self.range_min > self.range_max:
            raise ValidationError(_("\"Min\" value is greater than \"Max\""))
