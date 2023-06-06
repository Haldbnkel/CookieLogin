from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import warnings
import time
import os

warnings.simplefilter('ignore')

print("Easy Twitter Login - Haldbnkel Alpha")
auth_token = input("auth_token: ")
print("Started. Console does not auto-close. Please close it manually.")

options = webdriver.ChromeOptions()
options.add_argument("--log-level=OFF")
options.add_argument("--disable-logging")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get('https://twitter.com/')
driver.add_cookie({"name": "auth_token", "value": auth_token, "domain": ".twitter.com"})
driver.get('https://twitter.com/settings/account')


while True:
    time.sleep(1)