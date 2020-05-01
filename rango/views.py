from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

def index(request):
    #dict established to allow passing of template engine
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #returning a rendered response
    return render(request, 'rango/index.html', context=context_dict)
