import unittest


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Yvesrocher_create_lk(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search(self):
        driver = self.driver
        driver.get("https://www.yves-rocher.ru/")
        time.sleep(5)
        elem = driver.find_element_by_css_selector('article form button.button.m-b_M')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elem = driver.find_element_by_id("mainHeaderSearchInput")
        elem.send_keys("вавпжовпж")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("Упс", driver.page_source)
        elem = driver.find_element_by_id("mainHeaderSearchInput")
        elem.send_keys("сыворотка")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("результат(ов)", driver.page_source)










if __name__ == '__main__':
    unittest.main()
