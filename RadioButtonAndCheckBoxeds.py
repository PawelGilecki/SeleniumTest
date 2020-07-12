from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# working with the radio buttons

status = driver.find_element_by_id("RESULT_RadioButton-7_0"). is_selected()
print(status)

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_enabled()
print(status)

driver.find_element_by_xpath("/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/label").click()

status = driver.find_element_by_id("RESULT_RadioButton-7_0"). is_selected()
print(status)

#working with check boxes

driver.find_element_by_xpath("/html/body/form/div[2]/div[17]/table/tbody/tr[7]/td/label").click()
driver.find_element_by_xpath("/html/body/form/div[2]/div[17]/table/tbody/tr[1]/td/label").click()