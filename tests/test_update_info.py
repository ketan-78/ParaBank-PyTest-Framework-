from pages.home_page import HomePage
from pages.update_info import UpdateInfo

def test_update_info(authenticated_user,data):
    update_info=UpdateInfo(authenticated_user)
    update_info.update_profile(
        data["fname"],
        data["lname"],
        data["addr"],
        data["city"],
        data["state"],
        data["pin"],
        data["phone"]
        )
    home_page=HomePage(authenticated_user)
    home_page.logout()