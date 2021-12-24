import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:

    link = "http://suninjuly.github.io/find_link_text"
    driver.get(link)
    button_click = driver.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    button_click.click()
    input_1 = driver.find_element(By.NAME, 'first_name')
    input_1.send_keys('Kostia')
    input_2 = driver.find_element(By.NAME, 'last_name')
    input_2.send_keys("Herasymchuk")
    input_3 = driver.find_element(By.CLASS_NAME, 'city')
    input_3.send_keys('Berezivka')
    input_4 = driver.find_element(By.ID, 'country')
    input_4.send_keys('Ukraine')
    input_button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    input_button.click()

finally:
    time.sleep(5)
    driver.quit()