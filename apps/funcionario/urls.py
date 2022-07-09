# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, reverse
from .views import FuncionarioList, FuncionarioCreate, FuncionarioUpdate


urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionario'),
    path('create/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('edit/<int:pk>/', FuncionarioUpdate.as_view(), name='update_funcionario'),
]
