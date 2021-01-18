from app.models import *
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

# Register your models here.


@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


class SchemaColumnInline(admin.TabularInline):
    model = SchemaColumn
    extra = 0


@admin.register(DataSchema)
class SchemaAdmin(admin.ModelAdmin):
    inlines = [SchemaColumnInline]


admin.site.site_header = _('Fake CSV')
