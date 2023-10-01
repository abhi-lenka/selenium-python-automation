import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from seleniumpagefactory.Pagefactory import WebElement
from confest import *
from requests import get


@pytest.fixture(scope="session")
def ac(driver):
    ac = ActionChains(driver)
    yield ac


@allure.step("Navigates to the URL and waits for the element")
def navigate_to_url(driver, url, ele):
    driver.get(url)
    wait_until_elem_present(driver, ele)


@allure.step("Scroll to the element")
def scroll_to_elem(driver, ele):
    if isinstance(ele, WebElement):
        driver.execute_script("arguments[0].scrollIntoView(true)", ele)
    else:
        driver.execute_script("arguments[0].scrollIntoView(true)", driver.find_element(*ele))


@allure.step("Scroll to the element and click")
def scroll_to_elem_n_click(driver, ele):
    scroll_to_elem(driver, ele)
    if isinstance(ele, WebElement):
        ele.click()
    else:
        driver.find_element(*ele).click()


@allure.step("Get the text from the element")
def get_text(driver, ele):
    scroll_to_elem(driver, ele)
    return driver.find_element(*ele).get_text()


@allure.step("Wait for the element to have desired text")
def wait_until_elem_has_text(driver, ele, text, timeout=10):
    wait_until_elem_present(driver, ele)
    WebDriverWait(driver, timeout).until(ec.text_to_be_present_in_element(ele, text))


@allure.step("Wait until the element is present")
def wait_until_elem_present(driver, ele, timeout=10):
    WebDriverWait(driver, timeout).until(ec.presence_of_element_located(ele))


@allure.step("Input the text inside the input element")
def input_text(driver, ele, text):
    scroll_to_elem(driver, ele)
    driver.find_element(*ele).clear()
    driver.find_element(*ele).send_keys(text)


@allure.step("Check if image is broken")
def is_image_broken(driver, ele, attr=False):
    elem = driver.find_element(*ele)
    if not attr:
        image_url = elem.get_attribute("src")
        response = get(image_url)

        # Check the status code of the response.
        if response.status_code != 200:
            # The image is broken.
            return True
        # The image is not broken.
        return False
    else:
        # We can check the width of the image to check if it is broken
        if elem.size["width"] == 0:
            return True
        return False
