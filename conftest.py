import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

@pytest.fixture
def driver():
    # Set the download directory
    downloads_path = str(Path.home() / "Downloads")

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
    chrome_options.add_argument("--allow-insecure-localhost")   # Allow insecure localhost
    chrome_options.add_argument("--allow-running-insecure-content")  # Allow insecure content
    chrome_options.add_argument("disable-web-security")
    #chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://35.198.251.75:8001")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downloads_path,  # Set download directory
        "download.prompt_for_download": False,          # Disable the download prompt
        "download.directory_upgrade": True,             # Allow overwriting files
        "safebrowsing.enabled": True                     # Enable safe browsing
    })
    

    # Setup: Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    yield driver  # This will allow the tests to use the driver
    driver.quit()  # Cleanup: Quit the driver after tests are done

@pytest.fixture(scope="session")
def session_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()