from typing import List
from faker import Faker
from dataclasses import dataclass


@dataclass
class Field:
    field: str
    faker_type: str
    options: dict


class FakerFactory:
    def __init__(self, fields: List[Field], rows: int):
        self._rows = rows
        self._fields = fields
        self._fake = Faker()

    def generate(self) -> List[dict]:
        return [{elem.field: getattr(self._fake, elem.faker_type)(**elem.options) for elem in self._fields}
                for _ in range(self._rows)]
