from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time
import os

MAX_WHITE = 10


class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""
    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'https://' + staging_server

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def white_for_row_in_list_table(self, row_text):
        """ожидать строку в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WHITE:
                    raise e
                time.sleep(0.5)

    def white_for(self, fn):
        """ожидать"""
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WHITE:
                    raise e
                time.sleep(0.5)

