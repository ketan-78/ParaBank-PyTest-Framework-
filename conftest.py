import json
import uuid
import pytest

from pages.home_page import HomePage
from utils.driver_factory import get_driver
from utils.config_reader import get_config_value
from utils.logger import logger

@pytest.fixture(scope="session", autouse=True)
def initialize_logger():
    # logger = setup_logger()
    logger.info("===== Test Session Started =====")
    yield logger
    logger.info("===== Test Session Finished =====")

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(get_config_value("base_url"))
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def data():
    with open("test_data/test_data.json") as file:
        return json.load(file)

@pytest.fixture(scope="function")
def authenticated_user(driver, data):
    home_page = HomePage(driver)
    logged_in = home_page.login(
        data["username"],
        data["password"]
    )
    if not logged_in:
        username = data["new_username"] + uuid.uuid4().hex[:4]
        home_page.register(
            data["fname"],
            data["lname"],
            data["addr"],
            data["city"],
            data["state"],
            data["pin"],
            data["phone"],
            data["ssn"],
            username,
            data["new_password"],
            data["confirm_new_password"]
        )
    return driver

@pytest.fixture(scope="session")
def credentials(data):
    username = data["username"]
    password = data["password"]
    return username,password

@pytest.fixture(scope="session")
def new_account_creation(data):
    acct_type = data["type"]
    old_acct_no = data["old_acct_no"]
    return acct_type,old_acct_no