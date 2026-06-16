from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class UpdateInfo:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def update_profile(self,fname,lname,addr,city,state,pin,ph):
        logger.info(f"Updating Profile")
        wait=Wait(self.driver)
        wait.element_click(Locators.UPDATE_CONTACT)

        wait.element_clear(Locators.VISIBLE)
        elements=wait.presence_of_elements(Locators.INPUT_BOXES)
        for element in elements:
            element.clear()
             
        wait.send_keys(Locators.UPDATE_FNAME,fname)
        wait.send_keys(Locators.UPDATE_LNAME,lname)
        wait.send_keys(Locators.UPDATE_ADDRESS,addr)
        wait.send_keys(Locators.UPDATE_CITY,city)
        wait.send_keys(Locators.UPDATE_STATE,state)
        wait.send_keys(Locators.UPDATE_PINCODE,pin)
        wait.send_keys(Locators.UPDATE_PHONE,ph)

        wait.element_click(Locators.UPDATE_PROFILE)