from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

users = [
    ("standard_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visual_user", "pass3")
    ]

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 12)

def user_login():
    for username, password in users:
        driver.get("https://www.saucedemo.com/")
        username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_input.clear()
        password_input.clear()
        
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        
        #time.sleep(3)
        print(driver.current_url)
        
        url_after_login = "https://www.saucedemo.com/inventory.html"
        
    def logging_out():
        if driver.current_url == url_after_login:
            print(username, "Pass")
        
            hamburger_menu = wait.until(EC.presence_of_element_located((By.ID,"react-burger-menu-btn"))).click()
            #driver.find_element(By.ID, "react-burger-menu-btn")
            #hamburger_menu.click()

            #wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))
        
            logout_button = wait.until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link")))#.click()
            #driver.find_element(By.ID, "logout_sidebar_link")
            logout_button.click()
            print(driver.current_url)
            
            #wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        
        else:
            print(username, "fail")
            
user_login()
    
    #homepage_text = driver.find_element(By.XPATH, "//span[@class='title']")
    
#driver.quit()
    