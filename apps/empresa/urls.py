# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include  # add this
from .views import EmpresaCreate

urlpatterns = [
    path('novo/',EmpresaCreate.as_view(),name='create_empresa')          # Django admin route

]
