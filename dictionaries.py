from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

users = {"standard_user":"secret_sauce",
         "problem_user":"secret_sauce",
         "visual_user":"pass3"
}

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username = input("enter username: ")
password = input("enter password: ")

if username in users:
    if users[username]==password:
        print("login success")
    else:
        print("wrong password or email")
else:
    print("user not found")