

from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render


from pages.models import Product

from django.views.decorators.http import require_POST


#------------------------------
def MergeDicts(dict1, dict2):
    if(isinstance(dict1 , list) and isinstance(dict2, list)):
        return dict1+dict2
    elif(isinstance(dict1 , dict) and isinstance(dict2, dict)):
        return dict(list(dict1.items())+ list(dict2.items()))
    return False
#--------------------------------

@require_POST
def add_to_cart(request, product_id):
    print(product_id)
    product = get_object_or_404(Product, id = product_id)
    print(product)
    print(product.price)
    session = request.session
    
    
    if(request.method == 'POST'):
        quantity = request.POST['quantity']
        flavor = request.POST['flavor']
        keyItem = str(product.id)+'('+ str(flavor) +')'
        DictItems = {
            keyItem:{
                'id':str(product.id),
                'name':product.name,
                'quantity':quantity,
                'flavor':flavor,
                
            }
        }
        if 'cart' in session:
            
            if keyItem in session['cart']:
                if(session['cart'][keyItem]['flavor'] == flavor):
                    print(session['cart'][keyItem]['quantity'])
                    session['cart'][keyItem]['quantity'] = int(session['cart'][keyItem]['quantity']) + int(quantity)
                    print(session['cart'][keyItem]['quantity'])
                    session.modified = True
                else:
                    
                    session['cart'] = MergeDicts(session['cart'], DictItems)
            else:
                session['cart'] = MergeDicts(session['cart'], DictItems)
            

        else:
            session['cart'] = DictItems
        
        
    session.modified = True
    print(session['cart'])
    return redirect('cart_detail')

def ChangeQuantity(request, id, flavor):
    session = request.session
    keyItem = str(id)+'('+ str(flavor) +')'
    if(request.method == 'POST'):
        NewQuantity = request.POST['quantity']
        
        if(keyItem in session['cart']):
            session['cart'][keyItem]['quantity'] = NewQuantity
            
            session.modified = True

    return redirect('cart_detail')
      
def delete(request, id, flavor):
    session = request.session
    product = get_object_or_404(Product, id = id )
    keyItem = str(id)+'('+ str(flavor) +')'
    if(keyItem in session['cart']):
        session['total'] -= float(product.price)*int(session['cart'][keyItem]['quantity'])
        del session['cart'][keyItem]
        
        session.modified = True
    
    return redirect('cart_detail')
def UpdateTotal(request, subtotal, shippingprice):

    session = request.session
    session['total']=float(subtotal) + int(shippingprice)
    session.modified = True




def cart_detail(request):
    class Prod():
        id = None
        name = None
        quantity = None
        flavor = None
        price = None
        total = None
        img = None


    total=0
    subtotal = 0
    shipping_price = 0
    session = request.session
    
    if('cart' not in session or len(session['cart']) < 1):
        return redirect('/products')
    
    if('total' not in session):
        session['total'] = 0

    if('delivery' not in session):
        session['delivery']=0

    if(request.method == 'POST'):
        shipping_price = request.POST['delivery']
        session['delivery'] = shipping_price
        session.modified = True
        

    

    products = []
    
    for key in request.session['cart']:
       
        product = Prod()
        product.id = session['cart'][key]['id']
        produ = get_object_or_404(Product, id = int(product.id))
        
        product.name = session['cart'][key]['name']
        
        product.quantity = session['cart'][key]['quantity']
        
        product.flavor = session['cart'][key]['flavor']
        
        product.price = produ.price

        product.total = produ.price * int(product.quantity)
        
        product.img = produ.image1.url

        products.append(product)

        subtotal += product.total
    
    total = subtotal + int(shipping_price)
    session['total'] = int(total)
    session.modified = True
    
    x={
        
        'products':products,
        'subtotal':subtotal,
        'total':total,
        'delivery':int(shipping_price),
        'prods':Product.objects.all()[:4]
    }
    return render(request, 'cart/cart.html', x)

