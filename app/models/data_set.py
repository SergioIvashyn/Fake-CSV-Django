import base64
from typing import List

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from io import StringIO
import csv
from django.core.files.base import ContentFile
from services.helpers.faker_factory import Field, FakerFactory


class DataSet(models.Model):
    READY = 'ready'
    PROCESSING = 'processing'

    STATUS_CHOICES = (
        (READY, _(READY.title())),
        (PROCESSING, _(PROCESSING.title())),
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=PROCESSING)
    row = models.IntegerField(default=1)
    schema_id = models.ForeignKey('DataSchema', on_delete=models.CASCADE)
    file = models.FileField(upload_to='data_sets', null=True)

    def __str__(self):
        return f"{self.pk}-{self.creation_date}-{self.status}"

    def _get_field_names(self) -> List[str]:
        return [col.name for col in self.schema_id.schemacolumn_set.order_by('order')]

    def _get_adapted_schema_columns(self) -> List[Field]:
        return [elem.adapted_to_field_faker() for elem in self.schema_id.schemacolumn_set.order_by('order')]

    def generate_file(self):
        filename = f'{datetime.now().strftime("%H:%M:%S_%d.%m.%Y")}_{self.schema_id.name}.csv'
        fieldnames = self._get_field_names()
        csv_buffer = StringIO()
        writer: csv.DictWriter = csv.DictWriter(csv_buffer, fieldnames=fieldnames,
                                                delimiter=self.schema_id.column_separator,
                                                quotechar=self.schema_id.string_character)
        writer.writeheader()
        faker_factory = FakerFactory(fields=self._get_adapted_schema_columns(), rows=self.row)
        for elem in faker_factory.generate():
            writer.writerow(elem)
        csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
        self.file.save(filename, csv_file)
        self.status = self.READY
        self.save()
        return self
