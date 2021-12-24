from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    x = driver.find_element(By.ID, 'input_value').text
    result = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID,'robotCheckbox').click()
    driver.find_element(By.CSS_SELECTOR, '[for=robotsRule]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
finally:
    time.sleep(8)
    driver.quit()
