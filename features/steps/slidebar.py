import unittest
from datetime import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver import ActionChains

class Mytestslider(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver_win32_93\chromedriver.exe")

    def test_testdrag(self):
        browser = self.browser

        browser.get("https://qavbox.github.io/demo/dragndrop/")
        slider = browser.find_element_by_xpath('/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]')
        action = ActionChains(browser)
        elm = self.browser.find_element_by_xpath("//input[@value='0']")
        move = ActionChains(self.browser)
        move.click_and_hold(elm).move_by_offset(131, 0).release().perform()
        target1 = browser.find_element_by_id('range')
        print(target1.text)
        self.assertEqual("100", target1.text)
        time.sleep(5)

        def tearDown(self):
            self.browser.quit()

    if __name__ == '__main__':
        unittest.main()



