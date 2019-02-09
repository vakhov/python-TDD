from django.core.exceptions import ValidationError

from lists.models import Item, List
from django.test import TestCase


class ListAndItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохранения и получения элемента списка"""
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'Первый (самый) элемент списка'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Элемент второй'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Первый (самый) элемент списка')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Элемент второй')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_list_items(self):
        """тест: нельзя добавить пустые элементы списка"""
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
        # Альтернатива with
        # try:
        #     item.save()
        #     self.fail('Метод save должен поднять исключение')
        # except ValidationError:
        #     pass

    def test_get_absolute_url(self):
        """тест: получен абсолютный url"""
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')
