from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://newtours.demoaut.com/")

#driver.save_screenshot(r"C:\Users\PawelGilecki\Desktop\SeleniumTest\screenshots\homepage.png")

driver.get_screenshot_as_file(r"C:\Users\PawelGilecki\Desktop\SeleniumTest\screenshots\homepage2.png")