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
    path('login/', auth_views.LoginView.as_view(template_name='login-register.html', redirect_field_name='home'), name='login'),
    path('logout/', auth_views.logout_then_login, {'next_page': '/app/authentication/login/'}, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
