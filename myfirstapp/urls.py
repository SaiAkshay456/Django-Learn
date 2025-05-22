from django.contrib import admin
from django.urls import path
from . import views
'''
you can imagine like routers in nodejs
'''

urlpatterns = [
    path('',views.product),
    path('addtocart/',views.addToCart),
    path('users/',views.user),
    path('<int:user_id>/',views.get_description,name="user_detail")
]