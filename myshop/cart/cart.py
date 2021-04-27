#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: cart.py
# Proyecto original obtenido en:
#
# Descripción:
#
#   Esta clase define el carrito de compras del sistema.
#
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Inicializa el      |
#           |                        |  - request: datos de     |    carrito de com-    |
#           |       __init__()       |    la solicitud.         |    pras, si no se ha  |
#           |                        |                          |    creado uno, lo     |
#           |                        |                          |    crea.              |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Realiza un conteo  |
#           |        __len__()       |         Ninguno          |    de los items que   |
#           |                        |                          |    se encuentran en   |
#           |                        |                          |    el carrito.        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Itera sobre los    |
#           |       __iter__()       |         Ninguno          |    items del carrito  |
#           |                        |                          |    y obtiene los pro- |
#           |                        |                          |    ductos de la db.   |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |  - product: producto a   |  - Agrega un producto |
#           |                        |    ser agregado.         |    al carrito de com- |
#           |          add()         |  - quantity: cantidad de |    pras o actualiza   |
#           |                        |    productos a agregar.  |    su cantidad si ya  |
#           |                        |  - update_quantity: si   |    se encuentra agre- |
#           |                        |    es una actualización. |    gado.              |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |  - product: representa   |  - Remueve el pro-    |
#           |        remove()        |    el producto que se    |    ducto indicado     |
#           |                        |    desea remover.        |    del carrito.       |
#           |                        |                          |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Actualiza la       |
#           |         save()         |         Ninguno          |    información del    |
#           |                        |                          |    carrito en la      |
#           |                        |                          |    sesión.            |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Vacía el carrito   |
#           |         clear()        |         Ninguno          |    almacenado en la   |
#           |                        |                          |    sesión.            |
#           |                        |                          |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Obtiene el precio  |
#           |    get_total_price()   |         Ninguno          |    total del carrito. |
#           |                        |                          |                       |
#           |                        |                          |                       |
#           +------------------------+--------------------------+-----------------------+
#
#
#-------------------------------------------------------------------------

from decimal import Decimal
from django.conf import settings
from catalog.models import Product

class Cart(object):

    def __init__(self, request):

        # Se obtiene el carrito de la sesión actual
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        # Si no existe un carrito en la sesión, se crea uno
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __len__(self):
        # Regresa la suma de los items en el carrito
        return sum(item['quantity'] for item in self.cart.values())


    def __iter__(self):

        # Obtiene la lista de los productos que se encuentran en el carrito
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        # Asigna los datos de cada producto a cada item del carrito
        for product in products:
            self.cart[str(product.id)]['product'] = product

        # Actualiza los valores de precio y precio total de cada item 
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        # Si el producto no se encuentra en el carrito, lo agrega.
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        
        # Se actualiza la cantidad de productos dependiendo de si es una 
        # actualización o se está agregando un producto nuevo.
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)

        # Si el producto se encuentra en el carrito, procede a removerlo.
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # Se actualiza el carrito que se encuentra almacenado en la sesión.
        self.session[settings.CART_SESSION_ID] = self.cart
        # Se marca la sesión como modificada para asegurar que se actualizó la información.
        self.session.modified = True

    def clear(self):
        # Se asigna un objeto vacío al carrito de la sesión.
        self.session[settings.CART_SESSION_ID] = {}
        # Se indica que se ha modificado información de la sesión.
        self.session.modified = True

    def get_total_price(self):
        # Se obtiene el precio total de acuerco con la cantidad de productos de cada item
        # y el precio del producto.
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
