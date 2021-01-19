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

    def adapted_to_field_faker(self):
        options = {}
        if self.column_id.is_ranged:
            if self.column_id.is_number:
                options["min_value"] = self.range_min
                options["max_value"] = self.range_max
            else:
                options["nb_words"] = abs(randint(self.range_min, self.range_max))
        return Field(field=self.name, faker_type=self.column_id.type_name, options=options)

    def clean(self):
        if self.range_min > self.range_max:
            raise ValidationError(_("\"Min\" value is greater than \"Max\""))
