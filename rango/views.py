from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def about(request):

    return render(request, 'rango/about.html')

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    #returning a rendered response
    return render(request, 'rango/index.html', context=context_dict)
