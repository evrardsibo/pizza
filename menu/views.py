from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza

def index(request):
    pizzas = Pizza.objects.all().order_by('price')
    output = ' , '.join([p.name + " : " + str(p.price) + " $" for p in pizzas])
    # return HttpResponse(f"Les Pizzas : {output}")
    return render(request, 'menu/index.html', {'pizzas': pizzas})
