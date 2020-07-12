from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("file:///C:/Users/PawelGilecki/Desktop/SeleniumTest/sample.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
columns = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(rows)
print(columns)

print("Product"+"    "+"Article"+"    "+"Price")

for row in range(2, rows+1):
    for column in range(1, columns+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(row)+"]/td["+str(column)+"]").text
        print(value, end='    ')
    print()