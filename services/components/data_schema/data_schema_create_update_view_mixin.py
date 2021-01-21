from django.db import transaction

from services.components.schema_column import DataSchemaRepository


class DataSchemaCreateUpdateViewMixin:
    def form_valid(self, form):
        context = self.get_context_data()
        columns_data = context['columns_data']
        with transaction.atomic():
            form.instance.user_id = self.request.user
            self.object = form.save()
            print(columns_data.is_valid())
            if columns_data.is_valid():
                columns_data.instance = self.object
                DataSchemaRepository().save_formset(self.object, columns_data.cleaned_data)

        return super().form_valid(form)
