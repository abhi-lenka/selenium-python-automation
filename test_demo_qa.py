import time

from utility.utils import *
from page_objects.demo_qa_elements import *
import allure


homepage = HomePage()
elem_page = ElementsPage()
checkbox_page = CheckBoxPage()
radio_page = RadioButtonPage()
webtable_page = WebTables()
button_page = Buttons()
link_page = Links()
broken_link_page = BrokenLinks()


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

        # Delete all the entries
        delete_icons = driver.find_elements(*webtable_page.delete_record)
        for i in range(len(delete_icons)):
            scroll_to_elem_n_click(driver, webtable_page.delete_record)

        # Add an entry
        scroll_to_elem_n_click(driver, webtable_page.add)
        wait_until_elem_present(driver, webtable_page.registration_form)
        input_text(driver, webtable_page.form_first_name, fname)
        input_text(driver, webtable_page.form_last_name, lname)
        input_text(driver, webtable_page.form_email, email)
        input_text(driver, webtable_page.form_age, age)
        input_text(driver, webtable_page.form_salary, salary)
        input_text(driver, webtable_page.form_dep, department)
        scroll_to_elem_n_click(driver, webtable_page.form_submit)

        WebDriverWait(driver, 10).until(ec.invisibility_of_element(webtable_page.registration_form))
        assert driver.find_element(*webtable_page.t_cell(fname)).is_displayed(),\
            f"First name={fname} entry is not displayed."

        # Edit the entry
        scroll_to_elem_n_click(driver, webtable_page.edit_record)
        wait_until_elem_present(driver, webtable_page.registration_form)
        input_text(driver, webtable_page.form_last_name, "Banner")
        scroll_to_elem_n_click(driver, webtable_page.form_submit)

        WebDriverWait(driver, 10).until(ec.invisibility_of_element(webtable_page.registration_form))
        assert driver.find_element(*webtable_page.t_cell("Banner")).is_displayed(),\
            f"Last name=Banner edited entry is not displayed."

    def test_elem_buttons(self, driver, ac):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Buttons"))
        wait_until_elem_has_text(driver, homepage.main_header, "Buttons")

        ac.double_click(driver.find_element(*button_page.double_click_btn)).perform()
        wait_until_elem_present(driver, button_page.double_click_msg)
        assert "You have done a double click" in get_text(driver, button_page.double_click_msg),\
            f"Double click message mismatch"

        ac.context_click(driver.find_element(*button_page.right_click_btn)).perform()
        wait_until_elem_present(driver, button_page.right_click_msg)
        assert "You have done a right click" in get_text(driver, button_page.right_click_msg),\
            f"Right click message mismatch"

        scroll_to_elem_n_click(driver, button_page.click_me_btn)
        wait_until_elem_present(driver, button_page.dynamic_click_msg)
        assert "You have done a dynamic click" in get_text(driver, button_page.dynamic_click_msg),\
            f"Dynamic click message mismatch"

    def test_elem_links(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Links"))
        wait_until_elem_has_text(driver, homepage.main_header, "Links")

        scroll_to_elem_n_click(driver, link_page.simple_link)
        handles = driver.window_handles
        current_window = driver.current_window_handle

        # switch to new tab
        driver.switch_to.window(handles[1])
        driver.close()

        # switch back to current tab
        driver.switch_to.window(current_window)
        wait_until_elem_present(driver, link_page.dynamic_link)

        scroll_to_elem_n_click(driver, link_page.dynamic_link)
        handles = driver.window_handles

        # switch to new tab
        driver.switch_to.window(handles[1])
        driver.close()

        # switch back to current tab
        driver.switch_to.window(current_window)
        wait_until_elem_present(driver, link_page.dynamic_link)

        scroll_to_elem_n_click(driver, link_page.created)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 201 and status text Created")
        scroll_to_elem_n_click(driver, link_page.no_content)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 204 and status text No Content")
        scroll_to_elem_n_click(driver, link_page.moved)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 301 and status text Moved Permanently")
        scroll_to_elem_n_click(driver, link_page.bad_request)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 400 and status text Bad Request")
        scroll_to_elem_n_click(driver, link_page.un_auth)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 401 and status text Unauthorized")
        scroll_to_elem_n_click(driver, link_page.forbidden)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 403 and status text Forbidden")
        scroll_to_elem_n_click(driver, link_page.invalid_url)
        wait_until_elem_has_text(driver, link_page.link_response,
                                 "Link has responded with staus 404 and status text Not Found")

    def test_elem_broken_images_links(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Broken Links - Images"))
        wait_until_elem_has_text(driver, homepage.main_header, "Broken Links - Images")

        assert not is_image_broken(driver, broken_link_page.valid_image), f"The image is broken"
        assert not is_image_broken(driver, broken_link_page.valid_image, attr=True), f"The image is broken"
        assert is_image_broken(driver, broken_link_page.broken_image), f"The image is not broken"
        assert is_image_broken(driver, broken_link_page.broken_image, attr=True), f"The image is not broken"

        valid_url = driver.find_element(*broken_link_page.valid_link).get_attribute("href")
        valid_response = get(valid_url)
        assert valid_response.status_code == 200, f"Url doesn't return valid response"

        broken_url = driver.find_element(*broken_link_page.broken_link).get_attribute("href")
        broken_response = get(broken_url)
        assert broken_response.status_code == 500, f"Url doesn't return 500 as response"

