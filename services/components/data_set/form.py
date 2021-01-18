from django import forms

from app.models import DataSet


class DataSetForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ('row',)
