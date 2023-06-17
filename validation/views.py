from django.shortcuts import get_object_or_404, redirect, render
from pages.models import Product
from .models import Order
from django.views.decorators.http import require_POST

# Create your views here.

def validate(request):
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

    shipping_price = session['delivery']
    
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
    return render(request, 'validation/validate.html' , x)


def saveInfos(request):
    class Prod():
        id = None
        name = None
        quantity = None
        flavor = None
        price = None 
        total = None
        
    

    order = Order()
    session = request.session
    products_txt = '{ '
    productsids = ''
    for key in request.session['cart']:
       
        product = Prod()
        product.id = session['cart'][key]['id']
        produ = get_object_or_404(Product, id = int(product.id))
        
        product.name = session['cart'][key]['name']
        
        product.quantity = session['cart'][key]['quantity']
        
        product.flavor = session['cart'][key]['flavor']
        
        product.price = produ.price

        product.total = produ.price * int(product.quantity)
        
        productsids += str(product.id) + ' '

        product_text = str(product.id) + ' : { name:' + str(product.name) + ', quantity:' + str(product.quantity) + ', flavor:' + str(product.flavor) + ', price:' + str(product.price) + ', subtotal :' + str(product.total) + ' } ; '

        products_txt += product_text 

    products_txt += ' } '
    if(request.method == 'POST'):
        nom = request.POST['nom']
        email = request.POST['email']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        whatsapp = request.POST['whatsapp']
        adresse = request.POST['adresse']
        ville = request.POST['ville']
        pays = request.POST['pays']
        order.nom = nom
        order.prenom = prenom
        order.telephone = telephone
        order.whatsapp = whatsapp
        order.email = email
        order.adresse = adresse
        order.ville = ville
        order.pays = pays
        order.products = products_txt
        order.ids = productsids
        order.price = session['total']
        order.save()
    del session['cart']
    return redirect('thankyou')


def thankyou(request):
    return render(request, 'validation/thankyou.html')