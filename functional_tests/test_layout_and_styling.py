from selenium.webdriver.common.keys import Keys
from functional_tests.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    """тест макета и стелевого оформления"""

    def test_layout_and_styling(self):
        """тест макета стилевого оформления"""
        # Эдит открывает домашнюю страницу
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Она замечает что поле ввода аккуратно центрировано
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=10
        )

        # Она начинает новый список и видит, что поле ввода там тоже
        # аккуратно центрировано
        input_box.send_keys('testing')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=10
        )
