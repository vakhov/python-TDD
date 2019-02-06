from django.shortcuts import render, redirect
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
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, id):
    """добавить элемент"""
    list_ = List.objects.get(id=id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
