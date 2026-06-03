import os
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage


class TestTwitchSearchAndStreamer:
    """Test suite for Twitch search and streamer page functionality."""

    def test_search_and_open_streamer(self, driver: WebDriver):
        """
        Test workflow:
        1. Open Twitch homepage
        2. Search StarCraft II
        3. Wait for search results
        4. Scroll twice
        5. Open first streamer
        6. Wait for streamer page load
        7. Take screenshot
        
        Assertions:
        - Search results displayed
        - Streamer page loaded
        - Screenshot exists
        """
        # Initialize page objects
        home_page = TwitchHomePage(driver)
        search_results_page = TwitchSearchResultsPage(driver)
        streamer_page = TwitchStreamerPage(driver)

        # Step 1: Open Twitch
        home_page.open_twitch()
        # Accept both desktop and mobile URLs (mobile emulation may redirect)
        assert "twitch.tv" in driver.current_url, f"Failed to open Twitch homepage. Got: {driver.current_url}"

        # Step 2: Open search
        home_page.open_search()

        # Step 3: Search for StarCraft II
        search_query = "StarCraft II"
        home_page.search_query(search_query)

        # Step 4: Wait for search results to load
        search_results_page.wait_for_search_results()
        
        # Assertion: Search results are displayed
        streamer_count = search_results_page.get_streamer_count()
        assert streamer_count > 0, "No search results found for StarCraft II"
        print(f"✓ Search results displayed: {streamer_count} streamers found")

        # Step 7: Scroll down twice, loading more results, using reusable method
        search_results_page.scroll_down_twice()
        print(f"✓ Scrolled down twice")

        # Step 8: Get first streamer name for logging
        first_streamer_name = search_results_page.get_first_streamer_name()
        print(f"✓ Opening streamer: {first_streamer_name}")

        # Step 9: Select first streamer
        search_results_page.select_one_streamer_randomly()
        print(f"✓ Selected first streamer from search results")
        #Streamer page is loaded
        streamer_page.wait_for_loading_spinner()
        print(f"✓ Wait for loading spinner to appear")
        streamer_page.verify_page_loaded()
        print(f"✓ Streamer page loaded successfully")

        # Step 10: Take screenshot
        screenshot_path = streamer_page.take_screenshot()
        print(f"✓ Screenshot captured: {screenshot_path}")

        # Assertion: Screenshot exists
        assert os.path.exists(screenshot_path), f"Screenshot not found at {screenshot_path}"
        assert os.path.getsize(screenshot_path) > 0, "Screenshot file is empty"
        print(f"✓ Screenshot captured: {screenshot_path}")

        # Final assertion: All steps completed
        assert "twitch.tv" in driver.current_url and "/search" not in driver.current_url, "Navigation to streamer page failed"
        print("✓ Test completed successfully!")