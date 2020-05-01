from django.shortcuts import render
from django.http import HttpResponse

def about(request):

    return render(request, 'rango/about.html')

def index(request):
    #dict established to allow passing of template engine
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #returning a rendered response
    return render(request, 'rango/index.html', context=context_dict)
