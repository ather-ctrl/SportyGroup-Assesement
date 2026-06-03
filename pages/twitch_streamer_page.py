import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class TwitchStreamerPage(BasePage):
    """
    Page object for Twitch streamer page.
    Handles page load, popups, mature content warnings, and screenshots.
    """
    # Locators for this page
    STREAM_CONTAINER = (By.XPATH,"//video[@aria-label='Twitch video player']")

    LOADING_SPINNER = (By.XPATH,"//div[contains(@class,'SpinnerCircle')]")

    def wait_for_loading_spinner(self) -> None:
        """Wait for loading spinner to appear."""
        try:
            self.wait.until(EC.presence_of_element_located(self.LOADING_SPINNER))
        except Exception:
            pass

    def take_screenshot(self, filename: str = None) -> str:
        #Take screenshot and save to screenshots folder with timestamped filename if not provided
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        if not filename:
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
            filename = f"streamerPage_{timestamp}"

        if not filename.endswith(".png"):
            filename += ".png"

        screenshot_path = os.path.join(
            screenshots_dir,
            filename
        )
        try:
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"Error occurred while capturing screenshot: {e}")
            raise Exception(
                f"Failed to capture screenshot: {e}"
            )
    #page load verification - wait for loading spinner to disappear and video to start playing
    def verify_page_loaded(self) -> bool:   
        """
        Verify streamer page loaded correctly.
        """
        try: 
            self.wait.until(
                EC.invisibility_of_element_located(self.LOADING_SPINNER)
            )
            self.wait_for_element(self.STREAM_CONTAINER)
            start_time = self.driver.execute_script("return document.querySelector('video').currentTime")
            self.wait.until(
                lambda d: d.execute_script(f"""
                let v = document.querySelector('video');
                return v && (v.currentTime - {start_time}) >= 2;
                    """)
            )
            print("Streamer page loaded successfully.")
            return True
        except Exception as e:
            print(f"Error occurred while verifying page load: {e}")
            return False