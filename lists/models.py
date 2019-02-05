from django.db import models


class List(models.Model):
    """список"""
    pass


class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, blank=True, null=True, default=None, on_delete=models.CASCADE)


