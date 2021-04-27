#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------
# Archivo: views.py
#
# Descripción:
#   En este archivo se definen las vistas para la app del carrito de compras del sistema.
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |  - Añade el producto  |
#           |                        |    la solicitud.         |    indicado al carrito|
#           |       cart_add()       |                          |    de compras con     |
#           |                        |  - product_id: id del    |    ayuda de la clase  |
#           |                        |    producto a agregar.   |    Cart.              |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |  - Remueve el pro-    |
#           |                        |    la solicitud.         |    ducto indicado     |
#           |      cart_remove()     |                          |    del carrito con    |
#           |                        |  - product_id: id del    |    ayuda de la clase  |
#           |                        |    producto a remover.   |    Cart.              |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Obtiene los datos  |
#           |                        |  - request: datos de     |    necesarios para    |
#           |      cart_detail()     |    la solicitud.         |    mostrar el detalle |
#           |                        |                          |    del carrito de     |
#           |                        |                          |    compras.           |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información del producto a agregar y los datos del formulario.
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    # Se verifica si el formulario es válido, si es así se procede a agregar el producto.
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información del producto a remover y se procede a eliminarlo del carrito.
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información de cada item del carrito para mostrarla
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
