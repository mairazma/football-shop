from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products_list = Products.objects.all()

    context = {
        'name': 'Maira Azma Shaliha',
        'class': 'PBP C',
        'product_list': products_list
    }

    return render(request, "main.html", context)

def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
       products_item = Products.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", products_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Products.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       products_item = Products.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [products_item])
       return HttpResponse(json_data, content_type="application/json")
   except Products.DoesNotExist:
       return HttpResponse(status=404)
   
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Products, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)