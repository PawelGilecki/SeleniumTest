from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# select by visible text
#drp.select_by_visible_text("Morning")

# select by index number
#drp.select_by_index(2)

# select by value
drp.select_by_value("Radio-2")

# count number of option
print(len(drp.options))

# capture all the options and print them as an output
all_options = drp.options

for option in all_options:
    print(option.text)


