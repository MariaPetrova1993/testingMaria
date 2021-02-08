import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Проверка кнопки Donate и заполнение поля: другая сумма
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()
    def test_donate_in_python_org(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org
        driver.get("http://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # ждем 5 секунд
        time.sleep(3)
        elem = driver.find_element_by_link_text("Donate")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_id("CIVICRM_QFID_0_18")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_id("price_47")
        elem.click()
        elem.send_keys("1")
        time.sleep(3)




if __name__ == '__main__':
    unittest.main()
