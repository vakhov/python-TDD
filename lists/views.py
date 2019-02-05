from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    """домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/trololo/')
    return render(request, 'lists/home.html')


def view_list(request):
    """представление списка"""
    items = Item.objects.all()
    return render(request, 'lists/list.html', context={'items': items})
