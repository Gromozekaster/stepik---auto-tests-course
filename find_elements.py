from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    arr = driver.find_elements_by_css_selector("input")
    for element in arr:
        element.send_keys("A")

    submit_button = driver.find_element_by_css_selector("button.btn")

    submit_button.click()

finally:
    time.sleep(25)
    driver.quit()