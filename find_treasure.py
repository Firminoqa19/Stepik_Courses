from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    x = driver.find_element(By.ID, 'treasure').get_attribute('valuex')
    result = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
finally:
    time.sleep(8)
    driver.quit()
