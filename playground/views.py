from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    # query_set = Product.objects.all()
    # for p in query_set:
    #     print(p)

    prod = Product.objects.get(pk=1)
    return render(request, 'hello.html', {'name': 'Mosh'})
