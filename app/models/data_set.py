from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataSet(models.Model):
    READY = 'ready'
    PROCESSING = 'processing'

    STATUS_CHOICES = (
        (READY, _(READY.title())),
        (PROCESSING, _(PROCESSING.title())),
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=PROCESSING)
    row = models.PositiveIntegerField(default=1)
    schema_id = models.ForeignKey('DataSchema', on_delete=models.CASCADE)
    file = models.FileField(upload_to='data_sets', null=True)

    def __str__(self):
        return f"{self.pk}-{self.creation_date}-{self.status}"

    @property
    def creation_date_format(self):
        return self.creation_date.strftime("%Y-%m-%d")
