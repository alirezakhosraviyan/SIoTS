from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiling.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='home'),
    path('add_new', add_new, name='add_new'),
    path('import', import_excel),
    path('login/', login),
    path('add_environment', add_environment),
    path('add_component/first/', add_component_1),
    path('add_service', add_service),
    path('analytics', analytics),
    path('upload_backend_code', upload_backend_code),
    path('logout/', auth_views.logout_then_login, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
