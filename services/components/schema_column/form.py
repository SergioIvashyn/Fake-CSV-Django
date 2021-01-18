from django import forms
from django.forms import inlineformset_factory

from app.models import SchemaColumn, DataSchema


class SchemaColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        exclude = ()


SchemaColumnFormSet = inlineformset_factory(
    DataSchema, SchemaColumn, form=SchemaColumnForm,
    fields=['name', 'column_id', 'range_min', 'range_max', 'order'], extra=1, can_delete=True
)
