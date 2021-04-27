#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: urls.py
#
# Descripción:
#   En este archivo se definen las urls de la app de las órdenes.
#
#   Cada url debe tener la siguiente estructura:
#
#   path( url, vista, nombre_url )
#
#-------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('search/',views.search_orders,name='order_search'),
    path('cancel-items/',views.order_cancel_items,name='order_cancel_items'),
    path('cancel-order/<int:id>',views.order_cancel,name='order_cancel')
]
