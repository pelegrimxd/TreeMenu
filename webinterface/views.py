from django.shortcuts import render

def home(request):
    return render(request, 'webinterface/index.html')

def under_home(request):
    return render(request, 'webinterface/under_home.html')

def dunder_home(request):
    return render(request, 'webinterface/dunder_home.html')

def about(request):
    return render(request, 'webinterface/about.html')

def reviews(request):
    return render(request, 'webinterface/reviews.html')

def products(request):
    return render(request, 'webinterface/products.html')

def products_category(request):
    return render(request, 'webinterface/product_category.html')