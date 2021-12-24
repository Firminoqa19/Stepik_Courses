import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/simple_form_find_task.html'
driver = webdriver.Chrome()
try:

    driver.get(link)
    input_1 = driver.find_element(By.NAME, 'first_name')
    input_1.send_keys('Kostia')
    input_2 = driver.find_element(By.NAME, 'last_name')
    input_2.send_keys("Herasymchuk")
    input_3 = driver.find_element(By.CLASS_NAME, 'city')
    input_3.send_keys('Berezivka')
    input_4 = driver.find_element(By.ID, 'country')
    input_4.send_keys('Ukraine')
    input_button = driver.find_element(By.ID, 'submit_button')
    input_button.click()


finally:
    time.sleep(5)
    driver.quit()


