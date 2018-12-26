from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


@admin.register(ExcelFile)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ['__str__']

