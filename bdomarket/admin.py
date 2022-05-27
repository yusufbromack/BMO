from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(Item)