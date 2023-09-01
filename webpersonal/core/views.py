from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactoForm



# Create your views here.
def home(request):
    return render(request,"core/home.html")
def nosotros(request):
    return render(request,"core/nosotros.html")
def blog(request):
    return render (request, "core/blog.html")
def anuncios(request):
    return render (request, "core/anuncios.html")
def about(request):
    return render (request, "core/about.html")
def post(request):
    return render (request, "core/anuncio.html")
def entrada(request):
    return render (request, "core/entrada.html")
def gracias(request):
    return render (request, "core/gracias.html")
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')  
    else:
        form = ContactoForm()
    
    return render(request, 'core/contacto.html', {'form': form})


