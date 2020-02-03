import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import sin, log

from selenium import webdriver
def calc(x):
  return str(log(abs(12*sin(int(x)))))
try:
    browser = webdriver.Chrome()
    #browser.implicitly_wait(12)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element_by_css_selector("#book")
    book.click()
    val = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(val))
    book = browser.find_element_by_css_selector("#solve")
    book.click()

    assert "successful" in message.text

except Exception as error:
    print(error)

finally:
    time.sleep(10)
    browser.quit()
