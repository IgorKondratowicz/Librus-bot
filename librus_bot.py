from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from time import sleep



class Librus:
    def __init__(self):
        self.base_url = "https://portal.librus.pl/rodzina/home"
        options = Options()
        options.add_experimental_option("detach", True)
        
        login, password = self.get_pass()

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)
        self.driver.get(self.base_url)
        sleep(2)

        self.synergia(login, password)
        
    def synergia(self, login, password):
        box = self.driver.find_element(By.CLASS_NAME, "btn-synergia-top")
        box.click()
        sleep(2)

        menu_box = self.driver.find_elements(By.CLASS_NAME, "dropdown-item--synergia")
        menu_box[1].click()
        sleep(2)
        
        self.driver.switch_to.frame("caLoginIframe")

        login_box = self.driver.find_element(By.ID, "Login")
        pass_box = self.driver.find_element(By.ID, "Pass")

        login_box.send_keys(login)
        sleep(1)
        pass_box.send_keys(password)
        sleep(1)
        log_button = self.driver.find_element(By.ID, 'LoginBtn')
        log_button.click() 
        
        
    def get_pass(self):
        login = input("Login: ")
        password = input("Password: ")
        return login, password
        
        
Librus()