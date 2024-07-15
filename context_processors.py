from .cart import Cart 

# Create context_processor so our cart work on all pages of website 
def cart(request):
    return {'cart': Cart(request)} # Here Cart is using of cart.py Model
