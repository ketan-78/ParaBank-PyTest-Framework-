from pages.home_page import HomePage
from pages.loan import Loan

def test_loan_request(authenticated_user,data):
    loan=Loan(authenticated_user)
    loan.loan_request(data["loan_amount"],data["down_payment"],data["index"])
    home=HomePage(authenticated_user)
    home.logout()
