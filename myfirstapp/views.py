from django.shortcuts import render

from .models import User

from django.shortcuts import get_object_or_404;
#Create your views here.
def product(request):
    return render(request,'myfirstapp/all_app.html')


def addToCart(request):
    return render(request,'myfirstapp/add_to_cart.html')

def user(request):
    users=User.objects.all()
    return render(request,'myfirstapp/all_users.html',{'users':users})

def get_description(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    return render(request,'myfirstapp/get_user.html',{'user':user})