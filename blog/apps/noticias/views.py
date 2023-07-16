from django.shortcuts import render, HttpResponse

# Create your views here.

#def inicio (request):
 #   return HttpResponse("<h1>Hola mundo</h1> <h2> desde django</h2>")

def inicio (request):
    return render(request, 'noticias/inicio.html')
