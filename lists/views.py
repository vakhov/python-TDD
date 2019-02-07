from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.html import escape

from lists.models import Item, List


def home_page(request):
    """домашняя страница"""
    return render(request, 'lists/home.html')


def view_list(request, id):
    """представление списка"""
    list_ = List.objects.get(id=id)
    return render(request, 'lists/list.html', context={'list': list_})


def new_list(request):
    """новый список"""
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
    except ValidationError:
        list_.delete()
        error = escape("You can't have an empty list item")
        return render(request, 'lists/home.html', {'error': error})
    return redirect(f'/lists/{list_.id}/')


def add_item(request, id):
    """добавить элемент"""
    list_ = List.objects.get(id=id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
