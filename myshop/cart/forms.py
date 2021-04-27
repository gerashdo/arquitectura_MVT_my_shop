#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: forms.py
# Proyecto original obtenido en:
#
# Descripción:
#
#   En este archivo se definen los formularios para el carrito de compras.
#
#   Las características de ésta clase son las siguientes:
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Genera el número    |
#           |                       |                         |    de opciones dispo-  |
#           |                       |  - Provee los campos    |    nibles para         |
#           |                       |    necesarios para      |    agregar productos.  |
#           |   CartAddProductForm  |    que sea posible      |  - Define las          |
#           |                       |    añadir productos     |    propiedades de cada |
#           |                       |    al carrito de        |    uno de los campos   |
#           |                       |    compras.             |    que formarán parte  |
#           |                       |                         |    del formulario.     |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from django import forms

# Se genera el número de opciones para el campo de cantidad del formulario.
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
