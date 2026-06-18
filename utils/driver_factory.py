from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.config_reader import get_config_value


def get_driver():
    browser = get_config_value("browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        # options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

    elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
            driver.maximize_window()

    elif browser == "edge":
            options = webdriver.EdgeOptions()
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
            driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    return driver
