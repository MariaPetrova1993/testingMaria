import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Yvesrocher_create_lk(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_create_lk(self):
        driver = self.driver
        driver.get("https://www.yves-rocher.ru/")
        time.sleep(5)
        elem = driver.find_element_by_link_text("Личный кабинет")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_link_text("Создать личный кабинет")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_css_selector('input#email.form_input.m-t.width_100p.border-radius_S')
        elem.send_keys("Petrova2019@gmail.com")
        time.sleep(3)
        elem = driver.find_element_by_css_selector('button.button.form_button.button_submit')
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_id('gender2')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id('firstname')
        elem.send_keys("Наталья")
        time.sleep(1)
        elem = driver.find_element_by_id('lastname')
        elem.send_keys("Петрова")
        time.sleep(1)
        elem = driver.find_element_by_id('emailconfirmation')
        elem.send_keys("Petrova2019@gmail.com")
        time.sleep(1)
        elem = driver.find_element_by_css_selector('input#newpassword.form_input.width_100p.password')
        elem.send_keys("Hlksdj374832dkfjvgs;")
        time.sleep(1)
        elem = driver.find_element_by_css_selector('button.button.form_button.button_submit')
        time.sleep(5)




if __name__ == '__main__':
    unittest.main()
