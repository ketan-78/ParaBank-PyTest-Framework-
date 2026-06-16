from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import get_config_value

class Wait():
    def __init__(self,driver:WebDriver):
        self.driver=driver
        timeout=int(get_config_value("timeout"))
        mini_timeout=int(get_config_value("minitimeout"))
        self.wait=WebDriverWait(driver,timeout)
        self.mini_wait=WebDriverWait(driver,mini_timeout)
        
    def presence_of_element(self,locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def miniwait_for_element(self,locator):
        try:
            return self.mini_wait.until(
            EC.visibility_of_element_located(locator)
        )
        except TimeoutException:
            return None
        
    def element_click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def element_loaded(self,select_option):
        self.wait.until(lambda driver: len(select_option.options) >= 1)

    def web_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def element_clear(self,locator:tuple):
        self.wait.until(lambda driver:self.driver.find_element(*locator).get_attribute("value") != "")

    def presence_of_elements(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def send_keys(self,locator,value):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(value)

    def presence_of_element_r(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def loan_status(self,locator):
        self.wait.until(lambda driver:driver.find_element(*locator).text != "")  