from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import restItem

# Register your models here.
class foodsalesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = restItem
    fields:"__all__"
   
admin.site.register(restItem,foodsalesAdmin)
