# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, reverse
from .views import visaoGeral


urlpatterns = [
    path('', visaoGeral, name='visao_geral'),

]
