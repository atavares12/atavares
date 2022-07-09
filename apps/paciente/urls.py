# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, reverse
from .views import PacienteList, PacienteCreate, PacienteUpdate


urlpatterns = [
    path('', PacienteList.as_view(), name='list_paciente'),
    path('create/', PacienteCreate.as_view(), name='create_paciente'),
    path('edit/<int:pk>/', PacienteUpdate.as_view(), name='update_paciente'),

]
