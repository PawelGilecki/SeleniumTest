from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\PawelGilecki\Desktop\SeleniumTest\drivers\geckodriver.exe")

driver.get("https://www.amazon.de/")


# capture all cookies

def CountCookies():
    cookies = driver.get_cookies()
    print(len(cookies))
    print(cookies)


CountCookies()

# adding new cookie

cookie = {"name": "Mycookie", "value": "1234567890"}
driver.add_cookie(cookie)

CountCookies()

# deleting cookie file

driver.delete_cookie("Mycookie")

CountCookies()

# deleting all cookies

driver.delete_all_cookies()

CountCookies()
