from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    driver.get(link)
    x = driver.find_element(By.ID, 'num1').text
    y = driver.find_element(By.ID, 'num2').text
    result = int(x) + int(y)
    print(result)
    select = Select(driver.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))
    driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
finally:
    print('Test Passed')
    time.sleep(8)
    driver.quit()