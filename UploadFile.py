from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r'C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
time.sleep(3)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys(r"C:\Users\PawelGilecki\Desktop\quiz\zdjecia\1.PNG")