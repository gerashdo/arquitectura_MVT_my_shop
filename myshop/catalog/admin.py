#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: admin.py
#
# Descripción:
#
#   En este archivo se definen las clases del Catálogo para el administrador
#
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |  - Provee las confi-    |  - Indica los campos   |
#           |                       |    guraciones para      |    a mostrar del       |
#           |     CategoryAdmin     |    la aplicación del    |    modelo de           |
#           |                       |    administrador de     |    categorías.         |
#           |                       |    las categorías del   |                        |
#           |                       |    sistema.             |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |                         |  - Indica los campos   |
#           |                       |  - Provee las confi-    |    a mostrar del       |
#           |                       |    guraciones para      |    modelo de           |
#           |     ProductAdmin      |    la aplicación del    |    categorías.         |
#           |                       |    administrador de     |  - Indica el filtro a  |
#           |                       |    los productos del    |    utilizar cuando se  |
#           |                       |    sistema.             |    listen los productos|
#           |                       |                         |    y los campos edita- |
#           |                       |                         |    bles.               |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)