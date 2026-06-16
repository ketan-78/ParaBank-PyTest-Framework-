from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class Loan:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def loan_request(self,loan_amt,down_payment,acct):
        logger.info(f"Loan Request")
        wait=Wait(self.driver)
        wait.element_click(Locators.LOAN_REQUEST)

        wait.send_keys(Locators.LOAN_AMOUNT,loan_amt)
        wait.send_keys(Locators.DOWN_PAYMENT,down_payment)

        account=wait.web_element(Locators.LOAN_ACCOUNT)
        account_select=Select(account)
        wait.element_loaded(account_select)
        account_select.select_by_index(acct)

        wait.element_click(Locators.LOAN_APPLY)
        wait.presence_of_element(Locators.LOAN_PROCESSED)
        wait.loan_status(Locators.LOAN_STATUS)
        print("Loan Status :",wait.presence_of_element_r(Locators.LOAN_STATUS).text)   