from django.http import HttpResponse
from django.shortcuts import render

# these are like controllers
# you can have function name whatever you want
def home(request):
    # return HttpResponse("Hello Welcome to Django!! Keep Learning")
    return render(request,'blog/index.html')


def about(request):
    return HttpResponse("This is About page of Django")

def history(request):
    return HttpResponse("Welcome to history Page!!")
