from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path =r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://newtours.demoaut.com/")

#print(driver.title) #title of the page

#print(driver.current_url) #url of the page

print(driver.page_source) #html code for the page

driver.close()