from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
user_mgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
time.sleep(5)

actions.move_to_element(admin).move_to_element(user_mgmt).move_to_element(users).click().perform()