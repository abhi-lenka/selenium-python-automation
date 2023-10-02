import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
# browsers = ["Edge", "Chrome"]
browsers = ["Chrome"]
download_path = os.path.join(os.path.dirname(__file__), "downloads")
data_folder_path = os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture(scope="session", autouse=True, params=browsers)
def driver(request):
    browser = request.param
    driver = None
    if browser == "Edge":
        driver = webdriver.Edge()
    elif browser == "Chrome":
        chrome_options = Options()
        # Set the download path in the ChromeOptions instance.
        chrome_options.add_experimental_option(name="prefs", value={"download.default_directory": download_path})
        driver = webdriver.Chrome(options=chrome_options)
    else:
        assert False, f"{browser} is not supported!!"
    print(f"Opening {browser} browser!!!")
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
