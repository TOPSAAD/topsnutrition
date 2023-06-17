from django.shortcuts import get_object_or_404, render
from .models import Product, Contact
# Create your views here.




def index(request):
    # session = request.session
    # del session['cart']
    
    x={
        'products':Product.objects.all()[:4]
    }
    
    return render(request, 'pages/index.html',x)

def products(request):
    categories = ['gainer','proteine','acidamineetbcaa','preworkoutetbooster','creatine','omega3etfishoil','vitaminesetmineraux','bruluresdegraisse','0calorie']
    x={
        'products':Product.objects.all(),
        
        'categories':categories,
    }
    return render(request, 'pages/products.html',x)
def product(request, id):
    product = get_object_or_404(Product, id=id)
    flavors = product.flavor.split(',')
    x={
        'product':product,
        'flavors':flavors,
        'range':range(50),
        'oldprice':product.price+80,
    }
    return render(request, 'pages/details.html', x)


def contact(request):
    sender = Contact()
    if(request.method == 'POST'):
        sender.nom = request.POST['nom']
        sender.email = request.POST['email']
        sender.message = request.POST['message']
        sender.save()
        
        
    return render(request, 'pages/contact.html')