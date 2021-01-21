from django.db.models import Model
from django.utils.translation import ugettext_lazy as _


class Repository:
    model: Model = None

    def __init__(self):
        assert self.model is not None, _("field \"model\" is empty")

    def get(self, pk):
        return self.model.objects.filter(pk=pk).first()

    def create(self, data: dict):
        return self.model.objects.create(**data)

    def update(self, pk, data: dict):
        obj = self.get(pk)
        if obj is not None:
            for attr, value in data.items():
                setattr(obj, attr, value)
            obj.save()
        return obj

    def list(self, params=None):
        if params is None:
            params = {}
        return self.model.objects.all(**params)
