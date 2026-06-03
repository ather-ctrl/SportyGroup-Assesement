from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TwitchHomePage(BasePage):
    """
    Page object for Twitch home page.
    """
    TWITCH_URL = "https://m.twitch.tv"   # Twitch URL for mobile emulation (mobile version has different search flow)
   
    # Browse tab in bottom navigation - this is where search is accessed
    BROWSE_BUTTON = (By.XPATH, "//*[text()='Browse']")
    # Search input field (appears at top of Browse/directory page)
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")

    HOME_PAGE_LOADED = (By.XPATH, "//*[text()='Home']")

    def open_twitch(self) -> None:
        """Open Twitch home page."""
        self.open(self.TWITCH_URL)
        # Additional wait for home page to load (look for Home link in header)
        self.wait_for_element(self.HOME_PAGE_LOADED)

    def open_search(self) -> None:
        """Open search on mobile Twitch (Browse page)."""
        # On mobile, search is accessed via Browse tab
        try:
            self.wait_for_element(self.BROWSE_BUTTON)
            self.click(self.BROWSE_BUTTON)
            print(f"✓ Browse button clicked to access search")

        except Exception as e:
            print(f"Browse button click failed: {e}")     

        #Search input appears at top of Browse page, wait for it to be visible
    def search_query(self, query: str) -> None:
        try:
            search_input = self.wait_for_element(self.SEARCH_INPUT)
            self.type_text(self.SEARCH_INPUT, query)
            search_input.send_keys(Keys.RETURN)  # Press Enter to submit search and navigate to results page
            print(f"✓ Search query '{query}' entered and submitted")
        except Exception as e:
            print(f"Search query failed: {e}")
