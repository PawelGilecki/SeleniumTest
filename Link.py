from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")
original_links = ["Hotels", "Cruises"]
links_list = []
print("Number of links present: ", len(links))

for link in links:
    links_list.append(link.text)
print(links_list)

set1 = set(original_links)
set2 = set(links_list)

if set1.intersection(set2):
    print("Linki sa na liscie")
else:
    print("Nie ma")

# clicking on the link

#driver.find_element(By.LINK_TEXT, "REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()

