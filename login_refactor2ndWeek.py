from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# Test users
users = [
    ("standard_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visual_user", "pass3")
    ]

#Setup driver
class Launch_driver_and_get_website:
    def driver_lauch(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 12)
        
#login page class
class Login_flow:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
    def user_login(self, username, password):
        for username, password in users:
            
            # Locating the username field
            username_input = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
            #locating password field
            password_input = self.driver.find_element(By.ID, "password")
            #locating the login button
            login_button = self.driver.find_element(By.ID, "login-button")
            
            #clear exiting texts
            username_input.clear()
            password_input.clear()
            
            #entering the username and password
            username_input.send_keys(username)
            password_input.send_keys(password)
            #clicking login button
            login_button.click()
            
 #logout page class      
class Logout_class(Login_flow):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        
    def logging_out_method(self):
        # url_after_login = "https://www.saucedemo.com/inventory.html"
        #if self.driver.current_url == url_after_login:
        #    print(self.username, "Pass")

            # clicking hamburger menu
            hamburger_menu = self.wait.until(EC.presence_of_element_located((By.ID,"react-burger-menu-btn"))).click()
            #driver.find_element(By.ID, "react-burger-menu-btn")
            #hamburger_menu.click()

            #wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))
            
            #clicking logout button
            logout_button = self.wait.until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link")))#.click()
            #driver.find_element(By.ID, "logout_sidebar_link")
            logout_button.click()
            print(driver.current_url)
            
            #wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        
        #else:
        #    print(username, "fail")
        
lauch_driver = Launch_driver_and_get_website()
login = Login_flow()
logging_out = Logout_class()

    
    #homepage_text = driver.find_element(By.XPATH, "//span[@class='title']")
    
#driver.quit()
    