from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    """
    Factory class for creating and managing Selenium WebDriver instances
    with Chrome browser, mobile emulation (iPhone 14 Pro Max), and configurable options.
    """
    @staticmethod
    def create_driver(headless: bool = False) -> webdriver.Chrome:
        """
        Create and configure a Chrome WebDriver with mobile emulation.

        Args:
            headless (bool): Run browser in headless mode. Default is False.

        Returns:
            webdriver.Chrome: Configured Chrome WebDriver instance.
        """
        chrome_options = Options()

        # Using Google Pixel 7 as it has a similar screen size to iPhone 11 and is available in Chrome's device list,
        mobile_emulation = {
            "deviceName": "Pixel 7"  
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        # Headless mode
        if headless:
            chrome_options.add_argument("--headless")

        # Additional Chrome options
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-notifications")

        # Initialize Chrome WebDriver with webdriver-manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    @staticmethod
    def close_driver(driver: webdriver.Chrome) -> None:
        if driver:
            driver.quit()
