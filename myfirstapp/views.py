from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request,'myfirstapp/all_app.html')


def addToCart(request):
    return render(request,'myfirstapp/add_to_cart.html')