from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

users = [
    ("standard_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visual_user", "pass3")
    ]

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


for username, password in users:
    username_input = driver.find_element(By.ID, "user-name")
    passwrod_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_input.clear()
    passwrod_input.clear()
    
    username_input.send_keys(username)
    passwrod_input.send_keys(password)
    login_button.click()
    
    time.sleep(3)
    print(driver.current_url)
    
    url_after_login = "https://www.saucedemo.com/inventory.html"
    
    if driver.current_url == url_after_login:
        print(username, "Pass")
        
        hamburger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
        hamburger_menu.click()
    
        logout_button = driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()
        print(driver.current_url)
    
    else:
        print(username, "fail")
    
    #homepage_text = driver.find_element(By.XPATH, "//span[@class='title']")
    
#driver.quit()
    