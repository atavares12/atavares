# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("empresa/", include("apps.empresa.urls")),
    path("funcionario/", include("apps.funcionario.urls")),
    path("paciente/", include("apps.paciente.urls")),
    path("agenda/", include("apps.agenda.urls")),
    path("financeiro/", include("apps.financeiro.urls")),
    path("", include("apps.home.urls"))          # UI Kits Html files


]
