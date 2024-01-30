from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# REPLACE with your forms link
FORMS_LINK = "https://www.google.com/intl/pt-BR/forms/about/"

driver.get(FORMS_LINK)

text_box = driver.find_element(by=By.CLASS_NAME, value="className")
time.sleep(1)

text_box.click()
time.sleep(1)

text_box.send_keys("Answer 1")
time.sleep(1)

driver.quit()
