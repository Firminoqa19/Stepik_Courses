import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:

    link = "https://rozetka.com.ua/"
    driver.get(link)
    time.sleep(3)
    search_laptop = driver.find_element(By.CLASS_NAME, 'search-form__input')
    search_laptop.send_keys('Ноутбук')
    driver.find_element(By.CLASS_NAME, 'button_color_green').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "[href='https://rozetka.com.ua/acer-nhqdweu004/p323906515/']").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'buy-button__label').click()
finally:
    time.sleep(5)
    driver.quit()