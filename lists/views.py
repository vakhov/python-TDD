from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    """домашняя страница"""
    return render(request, 'lists/home.html')


def view_list(request):
    """представление списка"""
    items = Item.objects.all()
    return render(request, 'lists/list.html', context={'items': items})


def new_list(request):
    """новый список"""
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/trololo/')
