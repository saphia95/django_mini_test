from django.shortcuts import get_object_or_404, render
from django.template import loader
import requests

from .forms import ItemForm

from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Inventory

# Create your views here.


def index(request):
    latest_inventory_list = Inventory.objects.order_by('expiry_date')
    template = loader.get_template('inventory/index.html')
    context = {
        'latest_inventory_list': latest_inventory_list,
    }
    return HttpResponse(template.render(context, request))


def get_image_url(gtin):
    url = f"https://world.openfoodfacts.org/api/v0/product/{gtin}.json?fields=image_front_small_url"
    r = requests.get(url)
    image_url = r.json()["product"]["image_front_small_url"]
    return image_url


def get_product_name(gtin):
    url = f"https://world.openfoodfacts.org/api/v0/product/{gtin}.json"
    r = requests.get(url)
    product_name = r.json()["product"]["product_name_fr"]
    return product_name


def item_create(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        for i in Inventory.objects.all():
            if i.gtin == item.gtin:
                i.expiry_date = item.expiry_date
                i.save()
                return HttpResponseRedirect(reverse('index'))
        item.name = get_product_name(item.gtin)
        item.image_url = get_image_url(item.gtin)
        item.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "inventory/add.html", {'form': form})

def delete_item(request, pk): 
    Inventory.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('index'))

def modify_item(request, pk):
    item = Inventory.objects.get(id=pk)
    form = ItemForm(request.POST)
    if form.is_valid():
        itemF = form.save(commit=False)
        item.name = itemF.name
        item.expiry_date = itemF.expiry_date
        for i in Inventory.objects.all():
            if i.gtin == itemF.gtin:
                item.save()
                return HttpResponseRedirect(reverse('index'))
        item.gtin = itemF.gtin
        item.save()
        return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form,
        'item': item
    }
    return render(request, "inventory/modify.html", context)


def detail(request, id):
    item = get_object_or_404(Inventory, pk=id)
    return render(request, 'inventory/detail.html', {'item': item})