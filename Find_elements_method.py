from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"

try:
    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, 'input')
    for i in elements:
        i.send_keys('Privet')
    driver.find_element(By.CLASS_NAME, 'btn').click()
finally:
    time.sleep(8)
    driver.quit()