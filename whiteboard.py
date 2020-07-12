from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import random
import time
import datetime
driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://dbankdemo.com/signup")
driver.maximize_window()
wait = WebDriverWait(driver, 5)
wait.until(ec.visibility_of_element_located((By.ID, "title")))
Select(driver.find_element_by_id("title")).select_by_index(random.randint(1, 3))
selected = Select(driver.find_element_by_id("title"))
print(selected.first_selected_option.text)

# initialize Select object
#select = Select(user_defined_type_dropdown_element)

# to print the text
#print select.first_selected_option.text

# to print the value
#print select.first_selected_option.get_attribute("value")