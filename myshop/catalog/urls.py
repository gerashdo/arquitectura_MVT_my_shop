#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: urls.py
#
# Descripción:
#   En este archivo se definen las urls de la app del catálogo.
#
#   Cada url debe tener la siguiente estructura:
#
#   path( url, vista, nombre_url )
#
#-------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<str:slug>/', views.product_detail, name='product_detail'),
]
