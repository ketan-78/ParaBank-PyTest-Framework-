from pages.new_acct_page import NewAccountPage
from pages.home_page import HomePage

def test_new_account(authenticated_user,new_account_creation):
    new_account_page=NewAccountPage(authenticated_user)
    acct_type,old_acct_no=new_account_creation
    new_account_page.openAccount( acct_type,old_acct_no)
    home_page=HomePage(authenticated_user)
    home_page.logout()
