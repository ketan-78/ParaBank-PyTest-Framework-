from pages.bill_payment import BillPayment
from pages.overview_page import Overview
from pages.home_page import HomePage

def test_bill_payment_service(authenticated_user,data):
    overview=Overview(authenticated_user)
    overview.overview_tab()
    bill_payment=BillPayment(authenticated_user)
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
    bill_payment=BillPayment(authenticated_user)
    home_page=HomePage(authenticated_user)
    home_page.logout()