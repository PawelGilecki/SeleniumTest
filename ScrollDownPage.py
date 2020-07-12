from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()
time.sleep(5)
# Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

# Scroll down to find flag
#flag = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[2]/tbody/tr[43]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();", flag)

# scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")