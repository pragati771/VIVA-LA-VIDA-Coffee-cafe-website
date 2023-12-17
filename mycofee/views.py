

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")
def product(request):
    return render(request,"product.html")
def testimonial(request):
    return render(request,"testimonial.html")
def home(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"aboutus.html")

