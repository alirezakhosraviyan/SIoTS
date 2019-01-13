from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


@admin.register(ExcelFile)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ['__str__']


@admin.register(Service)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ['__str__']


@admin.register(User)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ['__str__']


@admin.register(DeviceType)
class EventTypeAdmin(ImportExportModelAdmin):
    list_display = ['__str__']


@admin.register(Device)
class DeviceAdmin(ImportExportModelAdmin):
    list_display = ['__str__']


@admin.register(Environment)
class DeviceAdmin(ImportExportModelAdmin):
    list_display = ['__str__']




