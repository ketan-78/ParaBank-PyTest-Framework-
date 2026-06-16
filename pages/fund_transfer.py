from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class FundTransfer:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def fund_transfer(self,amount,from_index,to_index):
        logger.info(f"Fund Transfer")
        wait=Wait(self.driver)
        wait.element_click(Locators.FUND_TRANSFER)
        wait.send_keys(Locators.AMOUNT,amount)
        
        from_account=wait.presence_of_element_r(Locators.FROM_ACCOUNT)
        select_from=Select(from_account)
        wait.element_loaded(select_from)
        select_from.select_by_index(from_index)

        to_account=wait.presence_of_element_r(Locators.TO_ACCOUNT)
        select_to=Select(to_account)
        wait.element_loaded(select_to)
        select_to.select_by_index(to_index)

        wait.element_click(Locators.TRANSFER)