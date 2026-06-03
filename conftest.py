import pytest
import os
from datetime import datetime
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """
    Fixture to create and manage WebDriver for each test.
    Creates driver before test, closes after test.
    """
    driver = DriverFactory.create_driver(headless=False)
    driver.implicitly_wait(10)
    
    yield driver
    
    DriverFactory.close_driver(driver)


@pytest.fixture(scope="function")
def driver_headless() -> WebDriver:
    """
    Fixture to create and manage WebDriver in headless mode.
    """
    driver = DriverFactory.create_driver(headless=True)
    driver.implicitly_wait(10)
    
    yield driver
    
    DriverFactory.close_driver(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture screenshot on test failure.
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Capture screenshot on failure
    if rep.failed and call.when == "call":
        if hasattr(item, "funcargs") and "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            _capture_screenshot(driver, item.nodeid)


def _capture_screenshot(driver: WebDriver, test_name: str) -> None:
    """
    Capture screenshot on test failure.
    
    Args:
        driver (WebDriver): Selenium WebDriver instance.
        test_name (str): Name of the test that failed.
    """
    screenshots_dir = "screenshots"
    
    # Create screenshots directory if it doesn't exist
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    # Create timestamped directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_dir = os.path.join(screenshots_dir, timestamp)
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Generate screenshot filename
    safe_test_name = test_name.replace("::", "_").replace("/", "_")
    screenshot_path = os.path.join(test_dir, f"{safe_test_name}.png")
    
    # Capture screenshot
    try:
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"\nFailed to capture screenshot: {e}")
