from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from app.models import SchemaColumn, DataSchema


class SchemaColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        exclude = ()


SchemaColumnFormSet = inlineformset_factory(
    DataSchema, SchemaColumn, form=SchemaColumnForm,
    fields=['name', 'column_id', 'range_min', 'range_max', 'order'], labels={
        "name": _("Column name"),
        "column_id": _("Type"),
        "range_min": _("From"),
        "range_max": _("To"),
        "order": _("Order"),
    }, widgets={
        "column_id": forms.Select(attrs={'class': 'column_id'}),
        "range_min": forms.NumberInput(attrs={'class': 'range_min'}),
        "range_max": forms.NumberInput(attrs={'class': 'range_max'}),
        "order": forms.NumberInput(attrs={'class': 'order'}),
    }, extra=1, can_delete=True
)
