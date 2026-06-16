from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from locators.locators import Locators
from utils.wait import Wait
from utils.logger import logger

class BillPayment:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def payment_service(self,name,addr,city,state,pin,phone,amt,index):
        wait=Wait(self.driver)
        acct_no=wait.presence_of_element_r(Locators.ACCOUNT_NUMBER).text
        logger.info(f"Bill PAyment for Account No. {acct_no}")
        wait.element_click(Locators.BILL_PAY)

        wait.send_keys(Locators.PAYEE_NAME,name)
        wait.send_keys(Locators.PAYEE_ADDRESS,addr)
        wait.send_keys(Locators.PAYEE_CITY,city)
        wait.send_keys(Locators.PAYEE_STATE,state)
        wait.send_keys(Locators.PAYEE_PINCODE,pin)
        wait.send_keys(Locators.PAYEE_PHONE,phone)
        wait.send_keys(Locators.PAYEE_ACCOUNT,acct_no)
        wait.send_keys(Locators.PAYEE_ACCOUNT_VERIFY,acct_no)
        wait.send_keys(Locators.AMOUNT_PAY,amt)

        bill_account=wait.presence_of_element_r(Locators.BILL_ACCOUNT)
        select_account=Select(bill_account)
        wait.element_loaded(select_account)
        select_account.select_by_index(index)

        wait.element_click(Locators.SEND_PAYMENT)     