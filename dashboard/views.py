from django.shortcuts import render, redirect, get_object_or_404
from topsnutrition.settings import DASHBOARD_USERNAME, DASHBOARD_PASSWORD
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from validation.models import Order
from pages.models import Product
# Create your views here.

logged = False
def isLogged(request):
    global logged
    correct = True
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        if username == DASHBOARD_USERNAME and password == DASHBOARD_PASSWORD:
            logged = True
            return redirect(dashboard)
        else:
            correct = False
        
    
    return render(request,'dashboard/login.html' , {'correct':correct})

def dashboard(request):
    if(logged == False):
        return redirect(isLogged)
    orders = Order.objects.all()
    orders_list = list()
    for order in orders:
        T = {
                'id':order.order_id, 
                'name':order.prenom + ' ' + order.nom,
                'email':order.email,
                'number':order.telephone,
                'price':order.price,
                'state':order.delivered,
                }
        
    
        orders_list.append(T)
      
    
    x = {
        'orders':orders_list,
        

    }
    return render(request, 'dashboard/dashboard_panel.html', x)

def order_details(request, id):
    order = get_object_or_404(Order, order_id=id)
    print(order.ids)
    idss = order.ids.split()
    ordermod = list()
    orders = order.products.split(';')
    for ord in orders:
        ord = ord.replace('{', '').replace('}', '').split(',')
        for o in ord: 
            o = o.split(':')
            o = o[len(o)-1]
            ordermod.append(o)
      
    
    
    orderproducts = list()
    prod = list()
    
    
    for i in range(len(ordermod)):
        if(i%5==0 and i!=0):
            product = get_object_or_404(Product, id = idss[int(i/5)-1])
            orderdict = {
            'product':product,
            'name':prod[0],
            'quantity':prod[1],
            'flavor':prod[2],
            'price':prod[3],
            'subtotal':prod[4],
            }
            orderproducts.append(orderdict)
            prod = []
        prod.append(ordermod[i])

    
    
    x={
        'order':order,
        'orderproducts':orderproducts,
    }
    return render(request, 'dashboard/details.html', x)
    

    
        
    


    
    
    