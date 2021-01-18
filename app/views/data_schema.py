from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect

from app.models import DataSchema
from services.components.data_schema import DataSchemaCreateUpdateViewMixin, DataSchemaForm
from services.components.data_set import DataSetForm
from services.components.schema_column import SchemaColumnFormSet
from services.helpers.access_mixin import SchemaAccessMixin


class DataSchemaListView(LoginRequiredMixin, ListView):
    template_name = 'app/list.html'
    model = DataSchema

    def get_queryset(self):
        return DataSchema.objects.filter(user_id=self.request.user)


class DataSchemaCreateView(LoginRequiredMixin, DataSchemaCreateUpdateViewMixin, CreateView):
    template_name = 'app/create.html'
    model = DataSchema
    form_class = DataSchemaForm

    def get_success_url(self):
        return reverse('app:detail', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['columns_data'] = SchemaColumnFormSet(self.request.POST)
        else:
            data['columns_data'] = SchemaColumnFormSet()
        return data


class DataSchemaDetailView(LoginRequiredMixin, SchemaAccessMixin, FormView, DetailView):
    template_name = 'app/detail.html'
    model = DataSchema
    form_class = DataSetForm

    def get_context_data(self, **kwargs):
        context = super(DataSchemaDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_superuser and not request.user == self.object.user_id:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        dataset = form.save(commit=False)
        dataset.schema_id_id = self.object.pk
        dataset.save()

        return HttpResponseRedirect(reverse('app:detail', args=(self.object.pk,)))


class DataSchemaUpdateView(LoginRequiredMixin, DataSchemaCreateUpdateViewMixin, SchemaAccessMixin, UpdateView):
    template_name = 'app/update.html'
    model = DataSchema
    form_class = DataSchemaForm
    success_url = reverse_lazy('app:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['columns_data'] = SchemaColumnFormSet(self.request.POST, instance=self.object)
        else:
            data['columns_data'] = SchemaColumnFormSet(instance=self.object)
        return data


class DataSchemaDeleteView(LoginRequiredMixin, SchemaAccessMixin, DeleteView):
    template_name = 'app/delete.html'
    model = DataSchema
    success_url = reverse_lazy('app:list')
