from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    """
    Base page parent class with common methods.
    Inherited by all page objects.
    """    
    def __init__(self, driver: WebDriver, wait_timeout: int = 12):
        """
        Initialize base page with driver and implicit wait.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            wait_timeout (int): Explicit wait timeout in seconds. Default is 15.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.actions = ActionChains(driver)


    def open(self, url: str) -> None:
        #Open URL in browser.
        self.driver.get(url)

        #refresh page to ensure all elements load correctly (especially for Twitch which can have loading issues in mobile emulation)
    def page_refresh(self) -> None:
        self.driver.refresh()

        #reusable click method with scroll into view and retry on failure (handles Twitch's dynamic loading and click interception issues)
    def click(self, locator):
        element = self.wait.until(
        EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",element)
        try:
            element.click()
            print(f"✓ Clicked element: {locator}")
        except:
            self.driver.execute_script("arguments[0].click();", element)
            print(f"✓ Clicked element with JS fallback: {locator}")
    #Reusable method to find element with wait
    def wait_for_element(self, locator):
        return self.wait.until(
        EC.visibility_of_element_located(locator)
    )
    #// Wait for all elements to be visible
    def wait_for_all_elements(self, locator):  
        return self.wait.until(
        EC.visibility_of_all_elements_located(locator)
    )

    def type_text(self, locator, text: str) -> None:
        """
        Find element and type text.

        Args:
            locator (): (By, value).
            text (str): Text to type.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)


    def is_element_present(self, locator) -> bool:
        """
        Check if element is present (no exception).
        Args:
            locator (): (By, value).

        Returns:
            bool: True if present, False otherwise.
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            print(f"Element not found: {locator}")
            return False

    def wait_for_url_contains(self, partial_url: str) -> None:
        """
        Wait for URL to contain partial string.

        Args:
            partial_url (str): Partial URL string to match.
        """
        self.wait.until(EC.url_contains(partial_url))

    def get_current_url(self) -> str:
        """
        Get current page URL.

        Returns:
            str: Current URL.
        """
        return self.driver.current_url

    def get_page_title(self) -> str:
        """
        Get page title.

        Returns:
            str: Page title.
        """
        return self.driver.title
    #Scroll down by specified pixels.
    def scroll_down_pixels(self, pixels: int = 500) -> None:
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    #Scroll by a fraction of the visible viewport. fraction=0.5 -> half page
    def scroll_by_fraction(self, fraction: float = 0.5, times: int = 1) -> None:
        for _ in range(times):
            self.driver.execute_script(f"window.scrollBy(0, window.innerHeight * {fraction});"
            )

    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )