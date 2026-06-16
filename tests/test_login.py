import uuid

from pages.home_page import HomePage

def test_login(driver,credentials,data):
    username,password=credentials
    home_page=HomePage(driver)
    flag=home_page.login(username,password)
    if flag==False:
        home_page.register(data["fname"],data["lname"],data["addr"],data["city"],data["state"],data["pin"],
                          data["phone"],data["ssn"],data["new_username"]+uuid.uuid4().hex[:4],data["new_password"],
                          data["confirm_new_password"])
        home_page.logout()
        
    else:
        home_page.logout()