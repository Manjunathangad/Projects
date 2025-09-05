from selenium import By
from selenium.webdriver.common.keys import Keys


class Login_Admin_page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"


    def __init__(self,driver):
        self.driver = driver


    def enter_username(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.Xpath, self.btn_login_xpath).click()
        
