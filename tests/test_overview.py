from pages.home_page import HomePage
from pages.overview_page import Overview


def test_overview(authenticated_user):
    overview_page=Overview(authenticated_user)
    overview_page.overview_tab()
    home_page=HomePage(authenticated_user)
    home_page.logout()