from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

button = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")
#time.sleep(5)

actions = ActionChains(driver)
actions.double_click(button).perform()