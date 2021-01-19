from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from app.models import DataSchema
from services.helpers.formset_layout import FormsetLayout


class DataSchemaForm(forms.ModelForm):
    class Meta:
        model = DataSchema
        exclude = ("user_id",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('column_separator'),
                Field('string_character'),
                Fieldset('Add columns',
                         FormsetLayout('columns_data')),
                HTML("<br/>"),
                ButtonHolder(Submit('submit', _('Save'))),
            )
        )
