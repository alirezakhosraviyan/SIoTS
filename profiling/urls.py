from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiling.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='home'),
    path('import', import_excel),
    path('login/', my_login),
    path('add_environment', add_environment),
    path('add_device', add_device),
    path('add_service', add_service),
    path('all_services', all_services),
    path('all_envs', all_environments),
    path('all_devices', all_devices),
    path('analytics', analytics),
    path('upload_backend_code', upload_backend_code),
    path('logout/', auth_views.logout_then_login, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
