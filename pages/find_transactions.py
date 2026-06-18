from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class FindTransactions:
    def __init__(self,driver:WebDriver):
        self.driver=driver
        self.wait=Wait(self.driver)

    def account_selection(self,account_index):
        logger.info(f"Tansactions Details")
        self.wait.element_click(Locators.TRANSACTIONS)
        account=self.wait.presence_of_element_r(Locators.ACCOUNT_SELECTION)
        
        select_account=Select(account)
        self.wait.element_loaded(select_account)
        select_account.select_by_index(account_index)

    def find_by_id(self,id):
        logger.info(f"Tansactions Details by ID")
        self.wait.send_keys(Locators.TRANSACTIONS_ID,id)
        self.wait.element_click(Locators.FIND_BY_ID)
        self.wait.presence_of_element(Locators.TRANSACTION_RESULTS)

    def find_by_date(self,date):
        logger.info(f"Tansactions Details by Date")
        self.wait.send_keys(Locators.TRANSACTIONS_DATE,date)
        self.wait.element_click(Locators.FIND_BY_DATE)
        self.wait.presence_of_element(Locators.TRANSACTION_RESULTS)

    def find_by_duration(self,from_date,to_date):
        logger.info(f"Tansactions Details by Period")
        self.wait.send_keys(Locators.TRANSACTIONS_FROM_DATE,from_date)
        self.wait.send_keys(Locators.TRANSACTIONS_TO_DATE,to_date)
        self.wait.element_click(Locators.FIND_BY_RANGE)
        self.wait.presence_of_element(Locators.TRANSACTION_RESULTS)

    def find_by_amount(self,amount):
        logger.info(f"Tansactions Details by Amount")
        self.wait.send_keys(Locators.TRANSACTIONS_AMOUNT,amount)
        self.wait.element_click(Locators.FIND_BY_AMOUNT)
        self.wait.presence_of_element(Locators.TRANSACTION_RESULTS)
