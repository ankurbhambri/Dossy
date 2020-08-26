from django.contrib import admin
from .models import Customer
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    fields = ('name', 'city', )
    list_display = ('name', 'city')
