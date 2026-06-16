from selenium.webdriver.remote.webdriver import WebDriver

from utils.wait import Wait
from utils.logger import logger
from locators.locators import Locators

class Overview:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def overview_tab(self):
        logger.info(f"Overview")
        wait=Wait(self.driver)
        wait.element_click(Locators.OVERVIEW)