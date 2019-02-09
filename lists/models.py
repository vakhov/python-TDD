from django.db import models
from django.urls import reverse


class List(models.Model):
    """список"""

    def get_absolute_url(self):
        """получить абсолютный url"""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, blank=True, null=True, default=None, on_delete=models.CASCADE)


