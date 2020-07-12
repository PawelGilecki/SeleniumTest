from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# how many text boxes

inputboxes = driver.find_elements(By.CLASS_NAME, "text_field")
number = int(len(inputboxes))+1
print(type(number))
"""
status = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print("Displayed or not: ", status)

status = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print("Enabled or not: ", status)
# how to provide value into the text box

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Pawel")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Gilecki")

driver.find_element_by_id("RESULT_TextField-3").send_keys("333333")
"""

for i in range(1, number):
    text_field = "RESULT_TextField-"+str(i)
    driver.find_element_by_id(text_field).send_keys("hi")



