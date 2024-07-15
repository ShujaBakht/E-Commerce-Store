from store.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get the current cart from session or create a new one if not exists
        self.cart = self.session.get('cart', {})

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            # Update quantity or other logic if needed
            pass
        else:
            # Add new product to cart
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': 1  # Initialize quantity as needed
            }
        self.save()

    def save(self):
        # Save the cart back to session
        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        # Calculate and return the total number of items in the cart
        return len(self.cart)
    
    def get_prods(self):
        # Get Ids from the cart
        product_ids = self.cart.keys()

        #use Ids to lookup product in DB Models
        products = Product.objects.filter(id__in=product_ids)

        # Return those looked up Products
        return products
