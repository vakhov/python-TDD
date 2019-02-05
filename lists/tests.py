from lists.models import Item
from django.test import TestCase


# TODO: Уборка после выполнения ФТ
# TODO: Удаление операторов time.sleep
# TODO: Поддержка более чем одного списка!
# TODO: Скорректировать модель так, чтобы элементы были связаны с разными списками
# TODO: Добавить уникальные URL для каждого списка...
# TODO: Добавить URL для создания нового списка посредством POST
# TODO: Добавить URL для создания нового элемента в с вующем списке посредством POST

class HomePageTest(TestCase):
    """тест домашней страницы"""

    def test_uses_home_template(self):
        """тест: домашняя страница возвращает правильный html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        """тест: можно сохранить post-запрос"""
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        """тест: переадресует после post-запроса"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        """тест: сохранять элементы, только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_display_all_list_item(self):
        """тест: отображает все элементы списка"""
        # настройка
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        # вызов програмного кода
        response = self.client.get('/')
        # проверка утверждения
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохранения и получения элемента списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
