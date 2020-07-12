from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name("userName")

print(user_ele.is_displayed()) #returns true/fals based of element status
print(user_ele.is_enabled()) #returns true/false

pass_ele = driver.find_element_by_name("password")

print(pass_ele.is_displayed()) #returns true/fals based of element status
print(pass_ele.is_enabled()) #returns true/false

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

driver.find_element_by_name("login").click()
time.sleep(5)

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button", roundtrip_radio.is_selected()) #print status of radio button round trip

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of one way radio button", onetrip_radio.is_selected())

