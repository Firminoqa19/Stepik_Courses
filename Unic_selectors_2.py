from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input_1.send_keys("Vasya")
    input_2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    input_2.send_keys("Pupkin")
    email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    email.send_keys("dssdas@mail.ua")
    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button.click()
    time.sleep(2)
    result_validate = browser.find_element(By.CSS_SELECTOR, "h1")
    welcome_text = result_validate.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()