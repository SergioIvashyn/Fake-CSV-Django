from typing import List, Type

from app.models import SchemaColumn, DataSchema
from services.helpers.repository import Repository


class DataSchemaRepository(Repository):
    model = SchemaColumn

    def save_formset(self, related_obj: DataSchema, data: List[dict]):
        try:
            schema_column_arr: List[SchemaColumn] = [
                SchemaColumn(
                    name=elem.get('name'),
                    column_id=elem.get('column_id'),
                    range_min=elem.get('range_min'),
                    range_max=elem.get('range_max'),
                    order=elem.get('order'),
                    schema_id=related_obj
                )
                for elem in data if elem != {}]
            related_obj.schemacolumn_set.all().delete()
            self.model.objects.bulk_create(schema_column_arr)
        except Exception as e:
            print(e)
