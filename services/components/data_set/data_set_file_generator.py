from app.models import DataSet
from typing import List
from datetime import datetime
from io import StringIO
import csv
from django.core.files.base import ContentFile

from services.components.schema_column import SchemaColumnToFieldFakerAdapter
from services.helpers.faker_factory import Field, FakerFactory


class DataSetFileGenerator:
    def __init__(self, data_set: DataSet):
        self._data_set = data_set

    def _get_field_names(self) -> List[str]:
        return [col.name for col in self._data_set.schema_id.schemacolumn_set.order_by('order')]

    def _get_adapted_schema_columns(self) -> List[Field]:
        adapter = SchemaColumnToFieldFakerAdapter
        return [adapter(elem).render() for elem in self._data_set.schema_id.schemacolumn_set.order_by('order')]

    def generate_file(self) -> None:
        data_set = self._data_set
        filename = f'{datetime.now().strftime("%H-%M-%S__%d.%m.%Y")}_{data_set.schema_id.name}.csv'
        fieldnames = self._get_field_names()
        csv_buffer = StringIO()
        writer: csv.DictWriter = csv.DictWriter(csv_buffer, fieldnames=fieldnames,
                                                delimiter=data_set.schema_id.column_separator,
                                                quotechar=data_set.schema_id.string_character)
        writer.writeheader()
        faker_factory = FakerFactory(fields=self._get_adapted_schema_columns(), rows=data_set.row)
        for elem in faker_factory.generate():
            writer.writerow(elem)
        csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
        data_set.file.save(filename, csv_file)
        data_set.status = DataSet.READY
        data_set.save()
