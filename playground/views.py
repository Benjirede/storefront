from django.forms import DecimalField
from django.shortcuts import render
from django.db import transaction
from django.db.models import Q, F, Value, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    queryset = Product.objects.raw('select * from store_product')
    
    return render(request, 'hello.html', {'name': 'Ben', 'result': list(queryset)})