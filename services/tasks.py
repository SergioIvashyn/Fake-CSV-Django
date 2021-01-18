from __future__ import absolute_import, unicode_literals

from settings.celery import app

from app.models import DataSet


@app.task()
def generate_file(dataset_id):
    dataset: DataSet = DataSet.objects.get(id=dataset_id)
    dataset.generate_file()
