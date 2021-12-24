from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
try:
    driver.get(link)
    elements = driver.find_elements(By.CLASS_NAME, 'form-control')
    for i in elements:
        i.send_keys('aaaaa')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt.txt')
    driver.find_element(By.CSS_SELECTOR, '[type=file]').send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()

finally:
    time.sleep(8)
    driver.quit()