#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------
# Archivo: views.py
#
# Descripción:
#   En este archivo se definen las vistas generales del sistema.
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Muestra el template|
#           |      error_400()       |                          |    de acuerdo con la  |
#           |                        |  - exception: exepción   |    excepción recibida |
#           |                        |    recibida.             |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Muestra el template|
#           |      error_403()       |                          |    de acuerdo con la  |
#           |                        |  - exception: exepción   |    excepción recibida |
#           |                        |    recibida.             |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Muestra el template|
#           |      error_404()       |                          |    de acuerdo con la  |
#           |                        |  - exception: exepción   |    excepción recibida |
#           |                        |    recibida.             |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Muestra el template|
#           |      error_500()       |                          |    de acuerdo con la  |
#           |                        |  - exception: exepción   |    excepción recibida |
#           |                        |    recibida.             |                       |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

from django.shortcuts import render

def error_400(request, exception):
    data={}
    return render(request,'400.html', data)


def error_403(request, exception):
    data={}
    return render(request,'403.html', data)


def error_404(request, exception):
    data = {}
    return render(request,'404.html', data)


def error_500(request):
    data={}
    return render(request,'500.html', data)