from django.shortcuts import render

from .models import User
# Create your views here.
def product(request):
    return render(request,'myfirstapp/all_app.html')


def addToCart(request):
    return render(request,'myfirstapp/add_to_cart.html')

def user(request):
    users=User.objects.all()
    return render(request,'myfirstapp/all_users.html',{'users':users})