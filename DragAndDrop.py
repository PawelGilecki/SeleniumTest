from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

rome = driver.find_element_by_xpath("//*[@id='box6']")
italy = driver.find_element_by_xpath("//*[@id='box106']")

actions = ActionChains(driver)
actions.drag_and_drop(rome,italy).perform()