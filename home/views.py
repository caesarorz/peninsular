from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home/home.html', {})


def aboutus(request):
    return render(request, 'nosotros.html', {})


def events(request):
    return render(request, 'eventos.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def organizacion(request):
    return render(request, 'organizacion.html', {})