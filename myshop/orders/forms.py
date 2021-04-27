#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: forms.py
#
# Descripción:
#
#   En este archivo se definen los formularios para las órdenes de compra.
#
#   Las características de ésta clase son las siguientes:
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |                        |
#           |                       |  - Provee los campos    |  - Define las          |
#           |                       |    necesarios para      |    propiedades de cada |
#           |    OrderCreateForm    |    que sea posible      |    uno de los campos   |
#           |                       |    crear las órdenes    |    que formarán parte  |
#           |                       |    de compra.           |    del formulario.     |
#           |                       |    compras.             |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from django import forms
from .models import Order, OrderItem

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
