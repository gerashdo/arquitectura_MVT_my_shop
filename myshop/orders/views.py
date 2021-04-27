#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------
# Archivo: views.py
#
# Descripción:
#   En este archivo se definen las vistas para la app de órdenes.
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Verifica la infor- |
#           |                        |  - request: datos de     |    mación y crea la   |
#           |    order_create()      |    la solicitud.         |    orden de compra a  |
#           |                        |                          |    partir de los datos|
#           |                        |                          |    del cliente y del  |
#           |                        |                          |    carrito.           |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Crea y envía el    |
#           |        send()          |  - order_id: id del      |    correo electrónico |
#           |                        |    la orden creada.      |    para notificar la  |
#           |                        |                          |    compra.            |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

from django.shortcuts import render, redirect
from .models import OrderItem, Order
from catalog.models import Product
from .forms import OrderCreateForm
from django.core.mail import send_mail
from cart.cart import Cart
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404

def order_create(request):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Si la llamada es por método POST, es una creación de órden.
    if request.method == 'POST':

        # Se obtiene la información del formulario de la orden,
        # si la información es válida, se procede a crear la orden.
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            # Se limpia el carrito con ayuda del método clear()
            cart.clear()
            
            # Llamada al método para enviar el email.
            send(order.id, cart)
            return render(request, 'orders/order/created.html', { 'cart': cart, 'order': order })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})

def send(order_id, cart):
    # Se obtiene la información de la orden.
    order = Order.objects.get(id=order_id)

    # Se crea el subject del correo.
    subject = 'Order nr. {}'.format(order.id)

    # Se define el mensaje a enviar.
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.\n\n\n'.format(order.first_name,order.id)
    message_part2 = 'Your order: \n\n'
    mesagges = []

    for item in cart:
        msg = str(item['quantity']) + 'x '+ str(item['product'].name) +'  $'+ str(item['total_price'])+ '\n'
        mesagges.append(msg)
    
    message_part3 = ' '.join(mesagges)
    message_part4 = '\n\n\n Total: $'+ str(cart.get_total_price())
    body = message + message_part2 + message_part3 + message_part4

    # Se envía el correo.
    send_mail(subject, body, 'oscarcorverita@gmail.com', [order.email], fail_silently=False)

def search_orders(request):
    context={}
    if request.method=='POST':
        if(request.POST.getlist('items')):
            items=request.POST.getlist('items')
            # Cancela los items seleccionados
            order_cancel_items(request,items)
            # Notifica sobre los items que tiene la orden despues de borrar los seleccionados
            order_change(request,items)
            return render(request,'orders/order/order_form.html',context)
        elif(request.POST.get('id_order')): # Aqui sucede la busqueda de orden
            order_id=request.POST.get('id_order')
            get_object_or_404(Order,id=order_id) # Por si no encuentra la orden
            if(verify_expired_time(request,order_id)): # Verifica que el tiempo desde la creacion de la orden no sea mayor a 24 horas
                items=OrderItem.objects.filter(order_id=order_id)
                total=0
                for item in items: #Calcula el precio total de la orden
                    item.total_price=item.price*item.quantity
                    total+=item.total_price
                context={'items':items, 'total':total, 'order_id':order_id}
                return render(request,'orders/order/orders.html',context)
            else: # Esto sucede si el tiempo desde la creacion de la orden es mayor a 24 horas
                message='This order can not be cancelled due to the time that has passed (24 hours)'
                context={'message':message}
        else:
            return render(request,'orders/order/order_form.html',context)
    return render(request,'orders/order/order_form.html',context)

# Cancela los objetos que estan dentro de la lista llamada items.
def order_cancel_items(request, items):
    order_item=items

    for i in range(len(order_item)):
        order_item[i]=order_item[i].split(',')
        order_item[i]=OrderItem.objects.get(id=order_item[i][1], order_id=order_item[i][0])
    
    order=Order.objects.get(id=order_item[0].order_id)
    for i in range(len(order_item)):
        product=Product.objects.get(id=order_item[i].product_id)
        order_item[i].total_price=order_item[i].quantity*product.price

    send_email('cancelled products from', 'cancelation', order,order_item)
    item_delete(order_item)

# Notifica al usuario sobre los objetos que se quedaron en la orden tras la eliminacion de alguno.
def order_change(request,items):
    order_item=items
    order=Order.objects.get(id=order_item[0].order_id)
    order_item=OrderItem.objects.filter(order_id=order_item[0].order_id)

    if(len(order_item)==0):
        order.delete()
        return

    for i in range(len(order_item)):
        product=Product.objects.get(id=order_item[i].product_id)
        order_item[i].total_price=order_item[i].quantity*product.price
    
    send_email('updated','order',order,order_item)

# Cancela una orden completamente
def order_cancel(request,id):
    send_cancel_order_notification(request,id)
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('order_search')

# Notifica sobre la cancelacion de una orden.
def send_cancel_order_notification(request,id):
    order_id=id
    order=Order.objects.get(id=id)
    order_item=OrderItem.objects.filter(order_id=order_id)

    for item in order_item:
        item.total_price=item.quantity*item.product.price

    send_email('cancelled','cancelation',order,order_item)
    item_delete(order_item)

# Verifica que el tiempo desde que la orden se creó no sea mayor a 24 horas.
def verify_expired_time(request,id):
    order=Order.objects.get(id=id)
    hora=timezone.now()
    offset=hora-order.created
    horas_diferencia=offset.days*24+(offset.seconds/3600)
    if(horas_diferencia<24):
        return True
    else:
        return False

# Envia un email como si fuera un recibo de orden.
def send_email(change, action, order, order_item):

    subject = 'Order nr. {}'.format(order.id)
    # Se define el mensaje a enviar.
    message = 'Dear {},\n\nYou have successfully {} your order. Your order id is {}.\n\n\n'.format(order.first_name,change,order.id)
    message_part2 = 'Your {}: \n\n'.format(action)
    mesagges = []

    for item in order_item:
        msg = str(item.quantity) + 'x '+ str(item.product.name) +'  $'+ str(item.total_price)+ '\n'
        mesagges.append(msg)

    message_part3 = ' '.join(mesagges)
    body = message + message_part2 + message_part3

    # Se envía el correo.
    send_mail(subject, body, 'YOUR_MAIL_HERE', [order.email], fail_silently=False)

# Elimina los objetos que estan dentro de la lista order_item.
def item_delete(order_item):
    for item in order_item:
        item.delete()