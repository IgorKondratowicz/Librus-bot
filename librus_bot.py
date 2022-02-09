"""
    Written by Igor Kondratowicz, 09.02.2022
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from gui import Application

class Librus:
    """
        Logging into Librus using tkinter module and selenium webdriver
    """
    def __init__(self, login, password):
        self.base_url = "https://portal.librus.pl/rodzina/home"
        options = Options()
        options.add_experimental_option("detach", True)
        self.login = login
        self.password = password
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)
        self.driver.get(self.base_url)
        self.main()

    def __repr__(self):
        return "Librus bot"

    def redirect(self) -> None:
        """
        Redirecting to Librus login page
        """

        box = self.driver.find_element(By.CLASS_NAME, "btn-synergia-top")
        box.click()
        sleep(2)
        menu_box = self.driver.find_elements(By.CLASS_NAME, "dropdown-item--synergia")
        menu_box[1].click()
        sleep(2)
        self.driver.switch_to.frame("caLoginIframe")


    def log_in(self) -> None:
        """
        Logging into Synergia
        """
        login_box = self.driver.find_element(By.ID, "Login")
        pass_box = self.driver.find_element(By.ID, "Pass")
        login_box.send_keys(self.login)
        sleep(1)
        pass_box.send_keys(self.password)
        sleep(1)
        log_button = self.driver.find_element(By.ID, 'LoginBtn')
        log_button.click()

    def main(self) -> None:
        """
        Main function
        """
        self.redirect()
        self.log_in()

if __name__ == "__main__":
    gui = Application()
    gui.mainloop()
    if gui.login != "" and gui.password != "":
        Librus(gui.login, gui.password)
