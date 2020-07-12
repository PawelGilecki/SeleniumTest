from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
time.sleep(5)
#print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title =="Frames & windows":
        driver.close()

driver.quit()