import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    driver.find_element(By.ID, 'book').click()
    x = driver.find_element(By.ID, 'input_value').text
    result = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(result)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type=submit]'))).click()
finally:
    print(driver.switch_to.alert.text)
    print('Test Passed')
    driver.quit()