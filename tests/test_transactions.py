from pages.home_page import HomePage
from pages.find_transactions import FindTransactions

def test_transactions(authenticated_user,data):
    transaction=FindTransactions(authenticated_user)

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

    home=HomePage(authenticated_user)
    home.logout()

