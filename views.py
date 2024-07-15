from django.shortcuts import render , get_object_or_404
from .cart import Cart
from store.models import *
from Cart.models import *
from Cart.models import *
from .models import *
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    cart = Cart(request)

    cart_products = cart.get_prods
    return render(request, "cart_summary.html" , {"cart_products": cart_products})

    
from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .cart import Cart
# from .models import * 

# Get the Cart
def add_cart(request):
    cart = Cart(request)
    
    # Check for POST request
    if request.POST.get('action') == 'post':

        # Get product ID from the POST data
        product_id = int(request.POST.get('product_id'))

        # Lookup Product in the Database
        product = get_object_or_404(Product, id=product_id)

        # Add product to cart and save it to session
        cart.add(product=product)

        # Get cart quantity
        cart_quantity = cart.__len__()

        # Return the cart quantity as JSON response
        response = JsonResponse({'qty': cart_quantity})
        return response


        
   
def cart_delete(request):
    pass

def cart_update(request):
    pass