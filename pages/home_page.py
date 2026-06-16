from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class HomePage:
    def __init__(self,driver:WebDriver):
        self.driver=driver
        self.wait=Wait(self.driver)

    def login(self,username,password):
        logger.info(f"Attempting Login")
        self.wait.send_keys(Locators.USERNAME,username)
        self.wait.send_keys(Locators.PASSWORD,password)
        self.wait.element_click(Locators.LOGIN)
        
        mini=Wait(self.driver)
        errors=mini.miniwait_for_element(Locators.ERROR)
        if errors:
            return False
        else:
            return True
        
    def logout(self):
        logger.info(f"Logging Out")
        self.wait.element_click(Locators.LOGOUT)
        
    def register(self,fname,lname,addr,city,state,pin,phone,ssn,username,password,c_password):
        logger.info(f"Registration")
        self.wait.element_click(Locators.REGISTRATION)

        self.wait.send_keys(Locators.FNAME,fname)
        self.wait.send_keys(Locators.LNAME,lname)
        self.wait.send_keys(Locators.ADDRESS,addr)
        self.wait.send_keys(Locators.CITY,city)
        self.wait.send_keys(Locators.STATE,state)
        self.wait.send_keys(Locators.PIN_CODE,pin)
        self.wait.send_keys(Locators.PHONE,phone)
        self.wait.send_keys(Locators.SSN,ssn)
        self.wait.send_keys(Locators.NEW_USERNAME,username)
        self.wait.send_keys(Locators.NEW_PASSWORD,password)
        self.wait.send_keys(Locators.CONFIRM_PASSWORD,c_password)

        self.wait.element_click(Locators.REGISTER)