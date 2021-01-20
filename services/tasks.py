from __future__ import absolute_import, unicode_literals

from services.components.data_set.data_set_file_generator import DataSetFileGenerator
from settings.celery import app

from app.models import DataSet


@app.task()
def generate_file(dataset_id):
    dataset: DataSet = DataSet.objects.get(id=dataset_id)
    DataSetFileGenerator(dataset).generate_file()
