import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   
from pages.base_page import BasePage
 
class TwitchSearchResultsPage(BasePage):

    STREAMER_ITEMS = (By.XPATH, "//button[contains(@class,'ScCoreLink')]")

    FIRST_STREAMER = (By.XPATH," //div[text()='Top' ]//following::h2[@title][1]")

    LOADING_SPINNER = (By.XPATH,"//div[contains(@class,'SpinnerCircle')]")

    def wait_for_search_results(self) -> None:
        """Wait for search results to load."""
        self.wait_for_all_elements(self.STREAMER_ITEMS)
        try:
            EC.presence_of_element_located(self.LOADING_SPINNER)
        except Exception:
            pass

    def scroll_down_twice(self) -> None:
        """Scroll down the page twice."""
        self.wait_for_all_elements(self.STREAMER_ITEMS)

        self.scroll_by_fraction(fraction=0.5, times=1)  # scroll first time
        print("Scrolled down once, waiting for more results to load...")
        self.wait_for_all_elements(self.STREAMER_ITEMS) 
        self.scroll_by_fraction(fraction=0.5, times=1) # scroll second time
        print("Scrolled down once, more results loaded.")
     #Return number of streamers found in search results
    def get_streamer_count(self) -> int:
        streamer_count = len(self.wait_for_all_elements(self.STREAMER_ITEMS))
        print(f"Found {streamer_count} streamers in search results.")
        return streamer_count

    def select_one_streamer_randomly(self):
        try:
        # Wait for all streamer elements to load
            elements = self.wait_for_all_elements(self.STREAMER_ITEMS)
            if not elements:
                raise Exception("No streamer items found")
            # Pick a random streamer
            random_streamer = random.choice(elements)
            # Click the selected streamer
            random_streamer.click()
            print("Clicked on a random streamer in search results.")
        except Exception as e:
            print(f"Error selecting streamer item: {e}")
            raise


    def get_first_streamer_name(self) -> str: #Get the first streamer name."""
        streamer = self.wait_for_element(self.FIRST_STREAMER)
        print(f"First streamer found: {streamer.text}")
        return streamer.text