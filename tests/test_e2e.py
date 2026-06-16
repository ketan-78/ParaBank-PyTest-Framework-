import uuid

from pages.loan import Loan
from pages.home_page import HomePage
from pages.update_info import UpdateInfo
from pages.overview_page import Overview
from pages.bill_payment import BillPayment
from pages.fund_transfer import FundTransfer
from pages.new_acct_page import NewAccountPage
from pages.find_transactions import FindTransactions

def test_e2e(driver,credentials,data,new_account_creation):
    home_page=HomePage(driver)
    username,password=credentials
    flag=home_page.login(username,password)
    if flag==False:
        home_page.register(data["fname"],data["lname"],data["addr"],data["city"],data["state"],data["pin"],
                          data["phone"],data["ssn"],data["new_username"]+uuid.uuid4().hex[:4],data["new_password"],
                          data["confirm_new_password"])
    
    new_account_page=NewAccountPage(driver)
    acct_type,old_acct_no=new_account_creation
    new_account_page.openAccount( acct_type,old_acct_no)

    overview_page=Overview(driver)
    overview_page.overview_tab()

    fund=FundTransfer(driver)
    fund.fund_transfer(data["payee_amount"],data["index"],data["index"])

    # overview=Overview(driver)
    overview_page.overview_tab()
    bill_payment=BillPayment(driver)
    bill_payment.payment_service(
        data["payee_name"],
        data["payee_addr"],
        data["payee_city"],
        data["payee_state"],
        data["payee_pin"],
        data["payee_phone"],
        data["payee_amount"],
        data["index"]
        )
    bill_payment=BillPayment(driver)

    transaction=FindTransactions(driver)
    #Find by Id
    transaction.account_selection(data["index"])
    transaction.find_by_id(data["id"])
    #Find by Date
    transaction.account_selection(data["index"])
    transaction.find_by_date(data["date"])
    #Find by Date Range
    transaction.account_selection(data["index"])
    transaction.find_by_duration(data["from_date"],data["to_date"])
    #Find by Amount
    transaction.account_selection(data["index"])
    transaction.find_by_amount(data["payee_amount"])

    update_info=UpdateInfo(driver)
    update_info.update_profile(
        data["fname"],
        data["lname"],
        data["addr"],
        data["city"],
        data["state"],
        data["pin"],
        data["phone"]
        )

    loan=Loan(driver)
    loan.loan_request(data["loan_amount"],data["down_payment"],data["index"])
    home_page.logout()