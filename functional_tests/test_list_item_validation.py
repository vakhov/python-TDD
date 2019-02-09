from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTets(FunctionalTest):
    """тест валидации элемента списка"""

    def test_cannot_add_empty_list_item(self):
        """тест: нельзя добавлять пустые элементы списка"""
        # Эдит открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка. Она нажимает Enter на пустом поле ввода
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Браузер перехватывает запрос и не перезагружает страницу со списком
        self.white_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # Она пробует снова, теперь с неким текстом для элемента, и теперь
        # это срабатывает
        self.get_item_input_box().send_keys('Buy milk')
        self.white_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.white_for_row_in_list_table('1: Buy milk')

        # Как ни странно Эдит решает отправить второй пустой элемент списка
        self.get_item_input_box().send_keys(Keys.ENTER)

        # И снова браузер не подчинится
        self.white_for_row_in_list_table('1: Buy milk')
        self.white_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # И она может его исправить, заполнив поле неким текстом
        self.get_item_input_box().send_keys('Make tea')
        self.white_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.white_for_row_in_list_table('1: Buy milk')
        self.white_for_row_in_list_table('2: Make tea')
