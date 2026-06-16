from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class NewAccountPage:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def openAccount(self,type,old_acct_no): # type : string ("SAVINGS")
        logger.info(f"Opening New Account")
        wait=Wait(self.driver)
        wait.element_click(Locators.NEW_ACCOUNT)
        acct_type=self.driver.find_element(*Locators.ACCOUNT_TYPE)
        select_type=Select(acct_type)
        select_type.select_by_visible_text(type)

        old_acct=wait.web_element(Locators.OLD_ACCOUNT)
        select_new=Select(old_acct)
        wait.element_loaded(select_new)
        select_new.select_by_index(old_acct_no)
        wait.element_click(Locators.OPEN_ACCOUNT)