from .cart import Cart

# Se crea para poder utilizar la clase Cart en la sesión.
def cart(request):
    return {'cart': Cart(request) }
