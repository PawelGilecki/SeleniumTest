from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

#driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID,"tab-flight-tab-hp").click()

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")

time.sleep(10)

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("07/05/2020")

driver.find_element(By.ID,"flight-returning-hp-flight").send_keys(Keys.CONTROL+"a")
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("07/12/2020")

driver.find_element(By.XPATH,"/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[8]/label/button").click()
#Explicit wait statement
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))

element.click()

time.sleep(3)

driver.quit()