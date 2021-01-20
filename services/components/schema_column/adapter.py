from random import randint

from app.models import SchemaColumn
from services.helpers.faker_factory import Field


class SchemaColumnToFieldFakerAdapter:

    def __init__(self, schema_column: SchemaColumn):
        self._schema_column = schema_column

    def render(self) -> Field:
        options = {}
        schema_column = self._schema_column
        if schema_column.column_id.is_ranged:
            if schema_column.column_id.is_number:
                options["min_value"] = schema_column.range_min
                options["max_value"] = schema_column.range_max
            else:
                options["nb_words"] = abs(randint(schema_column.range_min, schema_column.range_max))
        return Field(field=schema_column.name, faker_type=schema_column.column_id.type_name,
                     options=options)
