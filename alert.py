from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
try:
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    time.sleep(1)
    x = driver.find_element(By.ID, 'input_value').text
    result = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
finally:
    print(driver.switch_to.alert.text)
    print('All done, test passed')
    time.sleep(7)
    driver.quit()