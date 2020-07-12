from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()

time.sleep(5)

#driver.switch_to.alert.accept()

driver.switch_to.alert.dismiss()

