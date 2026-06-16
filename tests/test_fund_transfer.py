from pages.home_page import HomePage
from pages.fund_transfer import FundTransfer

def test_fund_transfer(authenticated_user,data):
    fund=FundTransfer(authenticated_user)
    fund.fund_transfer(data["payee_amount"],data["index"],data["index"])
    home=HomePage(authenticated_user)
    home.logout()
