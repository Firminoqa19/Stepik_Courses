from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/registration1.html'

try:
    driver.get(link)
    fields = driver.find_elements(By.CSS_SELECTOR, 'input[required]')
    for i in fields:
        i.send_keys('Test')
    driver.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(2)
    txt = driver.find_element(By.TAG_NAME, 'h1').text
    assert txt == "Congratulations! You have successfully registered!"
    print('test passed')


finally:
    time.sleep(3)
    driver.quit()