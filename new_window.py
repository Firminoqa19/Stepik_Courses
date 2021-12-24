from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
    tab_1 = driver.window_handles[0]
    tab_2 = driver.window_handles[1]
    driver.switch_to.window(tab_2)
    time.sleep(1)
    x = driver.find_element(By.ID, 'input_value').text
    result = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(result)
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
finally:
    print(driver.switch_to.alert.text)
    driver.quit()
