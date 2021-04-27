#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------
# Archivo: views.py
#
# Descripción:
#   En este archivo se definen las vistas para la app del catálogo del sistema.
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |  - Obtiene los datos  |
#           |                        |    la solicitud.         |    para mostrar la    |
#           |    product_list()      |                          |    lista de los pro-  |
#           |                        |  - category_slug: slug   |    ductos de la cate- |
#           |                        |    de la categoría.      |    goría indicada.    |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Obtiene los datos  |
#           |    product_detail()    |                          |    para mostrar el    |
#           |                        |  - id: id del producto.  |    detalle del pro-   |
#           |                        |                          |    ducto indicado.    |
#           |                        |  - slug: slug del pro-   |                       |
#           |                        |    ducto a mostrar.      |                       |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None

    # Se obtienen todas las categorías.
    categories = Category.objects.all()

    # Se filtran los productos que se encuentran disponibles.
    products = Product.objects.filter(available=True)

    # Si se recibió el slug de la categoría, se seleccionan solo los productos pertenecientes
    # a esa categoría, de forma contraria, se envían todos los productos para mostrarlos.
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):

    # Se obtiene la información del producto que se mostrará.
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Se obtiene el formulario para agregar elementos de este producto al carrito.
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
