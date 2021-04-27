#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: admin.py
#
# Descripción:
#
#   En este archivo se definen las clases de la Orden para el administrador
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |  - Provee las confi-    |  - Indica los campos   |
#           |                       |    guraciones para      |    a mostrar del       |
#           |    OrderItemInline    |    la aplicación del    |    modelo de los       |
#           |                       |    administrador de     |    items de las        |
#           |                       |    los items de las     |    órdenes.            |
#           |                       |    órdenes.             |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |                         |  - Indica los campos   |
#           |                       |  - Provee las confi-    |    a mostrar del       |
#           |                       |    guraciones para      |    modelo de           |
#           |      OrderAdmin       |    la aplicación del    |    órdenes.            |
#           |                       |    administrador de     |  - Indica el filtro a  |
#           |                       |    las órdenes del      |    utilizar cuando se  |
#           |                       |    sistema.             |    listen las órdenes. |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    
admin.site.register(Order, OrderAdmin)