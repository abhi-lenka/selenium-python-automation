import time

import pytest

from utility.utils import *
from page_objects.demo_qa_elements import *
import allure


homepage = HomePage()
elem_page = ElementsPage()
checkbox_page = CheckBoxPage()
radio_page = RadioButtonPage()


@allure.title("Demo QA: Elements")
class TestElements:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_elem_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, ELEMENTS))
        wait_until_elem_has_text(driver, homepage.main_header, ELEMENTS)

    def test_elem_text_box(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Text Box"))
        wait_until_elem_has_text(driver, homepage.main_header, "Text Box")
        input_text(driver, elem_page.username, username)
        input_text(driver, elem_page.email, email)
        input_text(driver, elem_page.current_addr, current_addr)
        input_text(driver, elem_page.permanent_addr, permanent_addr)
        scroll_to_elem_n_click(driver, elem_page.submit)
        wait_until_elem_present(driver, elem_page.out_user)
        assert username in get_text(driver, elem_page.out_user)
        assert email in get_text(driver, elem_page.out_email)
        assert current_addr in get_text(driver, elem_page.out_curr_addr)
        assert permanent_addr in get_text(driver, elem_page.out_perm_addr)

    def test_elem_check_box(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Check Box"))
        wait_until_elem_has_text(driver, homepage.main_header, "Check Box")

        # Open all the closed toggles
        while True:
            toggles = driver.find_elements(*checkbox_page.toggle_closed)
            if len(toggles) >= 1:
                for toggle in toggles:
                    scroll_to_elem_n_click(driver, toggle)
            else:
                break

        # Check all unchecked check boxes
        unchecked = True
        while unchecked:
            checkboxes = driver.find_elements(*checkbox_page.check_box(""))
            unchecked = False
            for check in checkboxes:
                if not check.is_selected():
                    scroll_to_elem_n_click(driver, check.find_element(*checkbox_page.check_box_icon))
                    unchecked = True

    def test_elem_radio_button(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Radio Button"))
        wait_until_elem_has_text(driver, homepage.main_header, "Radio Button")
        assert not driver.find_element(*radio_page.radio_yes).is_selected()
        assert not driver.find_element(*radio_page.radio_impressive).is_selected()
        assert not driver.find_element(*radio_page.radio_no).is_selected()
        assert not driver.find_element(*radio_page.radio_no).is_enabled()
        scroll_to_elem_n_click(driver, radio_page.radio_yes_label)
        wait_until_elem_has_text(driver, radio_page.radio_text, "Yes")
        assert driver.find_element(*radio_page.radio_yes).is_selected()
        assert not driver.find_element(*radio_page.radio_impressive).is_selected()
        assert not driver.find_element(*radio_page.radio_no).is_selected()
        scroll_to_elem_n_click(driver, radio_page.radio_impressive_label)
        wait_until_elem_has_text(driver, radio_page.radio_text, "Impressive")
        assert not driver.find_element(*radio_page.radio_yes).is_selected()
        assert driver.find_element(*radio_page.radio_impressive).is_selected()
        assert not driver.find_element(*radio_page.radio_no).is_selected()

    def test_elem_web_tables(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Web Tables"))
        wait_until_elem_has_text(driver, homepage.main_header, "Web Tables")
