import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType
from utility.utils import *
# browsers = ["Edge", "Chrome"]
browsers = ["Chrome"]


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


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default "function" scope
    if request.node.rep_setup and request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup and request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


# take screenshot and attach in the report
def take_screenshot(driver, filename):
    screenshot_file = driver.get_screenshot_as_png()
    allure.attach(screenshot_file, name=filename, attachment_type=AttachmentType.PNG)


@allure.step("Update environment properties in Allure")
@pytest.fixture(scope="session", autouse=True)
def update_allure_report(pytestconfig):
    allure_dir = pytestconfig.option.allure_report_dir
    if allure_dir is not None:
        with open(os.path.join(allure_dir, "environment.properties"), "w+") as env_file:
            env_file.write("project=Selenium-Pytest\n")
            env_file.write(f"time_stamp={datetime.date.today()}\n")
