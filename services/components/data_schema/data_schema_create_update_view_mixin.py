from django.db import transaction


class DataSchemaCreateUpdateViewMixin:
    def form_valid(self, form):
        context = self.get_context_data()
        columns_data = context['columns_data']
        with transaction.atomic():
            form.instance.user_id = self.request.user
            self.object = form.save()
            if columns_data.is_valid():
                columns_data.instance = self.object
                columns_data.save()

        return super().form_valid(form)
