import os
import unittest
import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By

# Using Selenium, we’ll be able to define a testing file in Python where we can simulate a user opening a web browser,
# navigating to our page, and interacting with it. Our main tool when doing this is known as a Web Driver,
# which will open up a web browser on your computer.


# Finds the Uniform Resourse Identifier of a file (unique string that represents the file)
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()

class WebpageTest(unittest.TestCase):

    def test_title(self):
        '''Make sure the title is correct'''
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        '''Make sure increase button works correctly'''
        driver.get(file_uri("counter.html"))
        increase_button = driver.find_element(By.ID, "increase")
        increase_button.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrease(self):
        '''Make sure decrease button works correctly'''
        driver.get(file_uri("counter.html"))
        decrease_button = driver.find_element(By.ID, "decrease")
        decrease_button.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        '''Make sure header is updated to 20 after increase button in clicked 20 times'''
        driver.get(file_uri("counter.html"))
        increase_button = driver.find_element(By.ID, "increase")
        for i in range(20):
            increase_button.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "20")

if  __name__ == '__main__':
    unittest.main()