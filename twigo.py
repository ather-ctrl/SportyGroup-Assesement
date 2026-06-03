from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

mobile_emulation = {
    "deviceName": "iPhone 12 Pro"
}

options = webdriver.ChromeOptions()
options.add_experimental_option(
    "mobileEmulation",
    mobile_emulation
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.twitch.tv")