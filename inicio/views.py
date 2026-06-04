from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def error_404(request):
    return render(request, '404.htm') 

def shop(request):
    return render(request, 'shop.html')