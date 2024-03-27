import time
from page_objects.demo_qa_elements import *
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


# Elements
homepage = HomePage()
textbox_page = TextBoxPage()
checkbox_page = CheckBoxPage()
radio_page = RadioButtonPage()
webtable_page = WebTables()
button_page = Buttons()
link_page = Links()
broken_link_page = BrokenLinks()
upload_download_page = UploadDownload()
dynamic_page = DynamicProp()

# Forms
form_page = PracticeForm()

# Alert, Frame & Window
window_page = BrowserWindows()
alert_page = Alerts()
frame_page = Frames()
modal_page = Modals()

# Widgets
acc_page = Accordian()
auto_com_page = AutoComplete()
slider_page = Slider()
p_bar_page = ProgressBar()
tab_page = Tabs()
tooltip_page = ToolTips()
menu_page = Menu()
select_menu_page = SelectMenu()

# Interactions
sortable_page = Sortable()
resizeable_page = Resizeable()

# Book store app
book_store_page = BookStoreApp()


@allure.title(ELEMENTS)
class TestElements:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_elem_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, ELEMENTS))
        wait_until_elem_has_text(driver, homepage.main_header, ELEMENTS)

    @pytest.fixture(scope="function")
    def clean_download_folder(self):
        delete_files_in_directory(download_path)
        yield
        delete_files_in_directory(download_path)

    def test_elem_text_box(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Text Box"))
        wait_until_elem_has_text(driver, homepage.main_header, "Text Box")
        input_text(driver, textbox_page.username, username)
        input_text(driver, textbox_page.email, email)
        input_text(driver, textbox_page.current_addr, current_addr)
        input_text(driver, textbox_page.permanent_addr, permanent_addr)
        scroll_to_elem_n_click(driver, textbox_page.submit)
        wait_until_elem_present(driver, textbox_page.out_user)
        assert username in get_text(driver, textbox_page.out_user)
        assert email in get_text(driver, textbox_page.out_email)
        assert current_addr in get_text(driver, textbox_page.out_curr_addr)
        assert permanent_addr in get_text(driver, textbox_page.out_perm_addr)

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
        input_text(driver, webtable_page.form_first_name, f_name)
        input_text(driver, webtable_page.form_last_name, l_name)
        input_text(driver, webtable_page.form_email, email)
        input_text(driver, webtable_page.form_age, age)
        input_text(driver, webtable_page.form_salary, salary)
        input_text(driver, webtable_page.form_dep, department)
        scroll_to_elem_n_click(driver, webtable_page.form_submit)

        wait_until_elem_invisible(driver, webtable_page.registration_form)
        assert is_elem_displayed(driver, webtable_page.t_cell(f_name)), f"First name={f_name} entry is not displayed."

        # Edit the entry
        scroll_to_elem_n_click(driver, webtable_page.edit_record)
        wait_until_elem_present(driver, webtable_page.registration_form)
        input_text(driver, webtable_page.form_last_name, "Banner")
        scroll_to_elem_n_click(driver, webtable_page.form_submit)

        wait_until_elem_invisible(driver, webtable_page.registration_form)
        assert is_elem_displayed(driver, webtable_page.t_cell("Banner")),\
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
        # assert is_image_broken(driver, broken_link_page.broken_image), f"The image is not broken"
        # assert is_image_broken(driver, broken_link_page.broken_image, attr=True), f"The image is not broken"

        valid_url = driver.find_element(*broken_link_page.valid_link).get_attribute("href")
        valid_response = get(valid_url)
        assert valid_response.status_code == 200, f"Url doesn't return valid response"

        broken_url = driver.find_element(*broken_link_page.broken_link).get_attribute("href")
        broken_response = get(broken_url)
        assert broken_response.status_code == 500, f"Url doesn't return 500 as response"

    def test_elem_upload_download(self, driver, clean_download_folder):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Upload and Download"))
        wait_until_elem_has_text(driver, homepage.center_text, "Upload and Download")

        scroll_to_elem_n_click(driver, upload_download_page.download)
        # wait till the file gets downloaded
        while not os.path.isfile(downloaded_file_path):
            time.sleep(1)
        assert os.path.exists(downloaded_file_path), f"The file is not downloaded yet"

        # Upload the file
        input_text(driver, upload_download_page.upload, upload_file_path)
        wait_until_elem_has_text(driver, upload_download_page.upload_file_path, f"C:\\fakepath\\{upload_file_name}")

    def test_elem_dynamic_properties(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Dynamic Properties"))
        wait_until_elem_has_text(driver, homepage.main_header, "Dynamic Properties")

        assert not driver.find_element(*dynamic_page.enable_after).is_enabled(),\
            f"Button is enabled before 5 seconds"

        # Get the color of the element
        color = driver.find_element(*dynamic_page.color_change).value_of_css_property("color")

        assert not is_elem_displayed(driver, dynamic_page.visible_after),\
            f"Visible after button is displayed before 5 seconds"

        WebDriverWait(driver, 6).until(ec.visibility_of_element_located(dynamic_page.visible_after))
        assert driver.find_element(*dynamic_page.enable_after).is_enabled(), f"Button is not enabled after 5 seconds"

        new_color = driver.find_element(*dynamic_page.color_change).value_of_css_property("color")
        assert color != new_color, f"Color is not changed after 5 seconds"


@allure.title(FORMS)
class TestForms:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_form_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, FORMS))
        wait_until_elem_has_text(driver, homepage.main_header, FORMS)

    genders = ["Male", "Female", "Other"]

    @pytest.mark.parametrize("gender", genders)
    def test_form(self, driver, gender):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Practice Form"))
        wait_until_elem_has_text(driver, homepage.main_header, "Practice Form")
        input_text(driver, form_page.f_name, f_name)
        input_text(driver, form_page.l_name, l_name)
        input_text(driver, form_page.email, email)
        scroll_to_elem_n_click(driver, form_page.gender_label(gender))
        assert is_elem_selected(driver, form_page.gender(gender)), f"{gender} is not selected"
        input_text(driver, form_page.mobile, mobile)
        # input_text(driver, form_page.dob, dob + Keys.ENTER)
        # input_text(driver, form_page.subjects, subject + Keys.ENTER)
        scroll_to_elem_n_click(driver, form_page.hobby_c_box_label("Sports"))
        assert is_elem_selected(driver, form_page.hobby_c_box("Sports")), f"Sports hobby is not selected"
        input_text(driver, form_page.upload_pic, upload_file_path)
        input_text(driver, form_page.current_addr, current_addr)
        input_text(driver, form_page.state, state + Keys.ENTER)
        input_text(driver, form_page.city, city + Keys.ENTER)
        # scroll_to_elem_n_click(driver, form_page.submit)
        elem_click_script(driver, form_page.submit)
        wait_until_elem_present(driver, form_page.submit_form_header)

        assert is_elem_displayed(driver, form_page.table_row(gender)), f"{gender} is not present in table"
        assert is_elem_displayed(driver, form_page.table_row("Sports")), f"Sports is not present in table"
        # assert is_elem_displayed(driver, form_page.table_row(subject)), f"{subject} is not present in table"
        assert is_elem_displayed(driver, form_page.table_row(state + ' ' + city)),\
            f"{state + ' ' + city} is not present in table"
        # scroll_to_elem_n_click(driver, form_page.close_modal)
        elem_click_script(driver, form_page.close_modal)
        wait_until_elem_invisible(driver, form_page.submit_form_header)


@allure.title(ALERTS_FRAMES)
class TestAlertFrameWindow:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_alert_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, ALERTS_FRAMES))
        wait_until_elem_has_text(driver, homepage.main_header, ALERTS_FRAMES)

    def test_browser_window(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Browser Windows"))
        wait_until_elem_has_text(driver, homepage.main_header, "Browser Windows")

        scroll_to_elem_n_click(driver, window_page.new_tab)
        win_handles = driver.window_handles
        cur_handle = driver.current_window_handle

        # switch to new tab
        driver.switch_to.window(win_handles[1])
        driver.close()

        # switch back to current tab
        driver.switch_to.window(cur_handle)

        scroll_to_elem_n_click(driver, window_page.new_window)
        win_handles = driver.window_handles
        cur_handle = driver.current_window_handle

        # switch to new tab
        driver.switch_to.window(win_handles[1])
        driver.close()

        # switch back to current tab
        driver.switch_to.window(cur_handle)

        scroll_to_elem_n_click(driver, window_page.new_window_msg)
        win_handles = driver.window_handles
        cur_handle = driver.current_window_handle

        # switch to new tab
        driver.switch_to.window(win_handles[1])
        # txt = driver.find_element(By.TAG_NAME, "body").text
        # assert "Knowledge increases by sharing but not by saving" in txt,\
        #     f"Text is not present in the new window"
        driver.close()

        # switch back to current tab
        driver.switch_to.window(cur_handle)

    def test_alerts(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Alerts"))
        wait_until_elem_has_text(driver, homepage.main_header, "Alerts")

        # Alert
        scroll_to_elem_n_click(driver, alert_page.alert_btn)
        wait_until(driver, ec.alert_is_present())
        driver.switch_to.alert.accept()

        # Timer alert
        scroll_to_elem_n_click(driver, alert_page.timer_alert_btn)
        wait_until(driver, ec.alert_is_present(), timeout=6)
        driver.switch_to.alert.accept()

        # Accept alert
        scroll_to_elem_n_click(driver, alert_page.confirm_btn)
        wait_until(driver, ec.alert_is_present())
        driver.switch_to.alert.accept()
        wait_until_elem_has_text(driver, alert_page.confirm_result, "You selected Ok")

        # Dismiss alert
        scroll_to_elem_n_click(driver, alert_page.confirm_btn)
        wait_until(driver, ec.alert_is_present())
        driver.switch_to.alert.dismiss()
        wait_until_elem_has_text(driver, alert_page.confirm_result, "You selected Cancel")

        # Send input to alert
        scroll_to_elem_n_click(driver, alert_page.prompt_btn)
        wait_until(driver, ec.alert_is_present())
        driver.switch_to.alert.send_keys(f_name)
        driver.switch_to.alert.accept()
        wait_until_elem_has_text(driver, alert_page.prompt_result, f_name)

    def test_frames(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Frames"))
        wait_until_elem_has_text(driver, homepage.main_header, "Frames")

        driver.switch_to.frame("frame1")
        assert "This is a sample page" in get_text(driver, frame_page.sample_h), f"Sample header mismatch in frame1"

        driver.switch_to.parent_frame()

        driver.switch_to.frame("frame2")
        assert "This is a sample page" in get_text(driver, frame_page.sample_h), f"Sample header mismatch in frame2"

        driver.switch_to.parent_frame()

    def test_nested_frames(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Nested Frames"))
        wait_until_elem_has_text(driver, homepage.main_header, "Nested Frames")

        driver.switch_to.frame("frame1")
        assert "Parent frame" in driver.find_element(By.TAG_NAME, "body").text, f"Sample text mismatch in parent frame"

        driver.switch_to.frame(driver.find_element(*frame_page.child_frame))
        assert "Child Iframe" in driver.find_element(By.TAG_NAME, "p").text, f"Sample text mismatch in child frame"

        # This switches to parent frame
        driver.switch_to.parent_frame()

        # This switches to the primary window frame
        driver.switch_to.parent_frame()

    def test_modal_dialogs(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Modal Dialogs"))
        wait_until_elem_has_text(driver, homepage.main_header, "Modal Dialogs")

        scroll_to_elem_n_click(driver, modal_page.small_modal)
        wait_until_elem_present(driver, modal_page.modal_title("Small Modal"))
        scroll_to_elem_n_click(driver, modal_page.close_small_modal)
        wait_until_elem_invisible(driver, modal_page.modal_title("Small Modal"))

        scroll_to_elem_n_click(driver, modal_page.large_modal)
        wait_until_elem_present(driver, modal_page.modal_title("Large Modal"))
        scroll_to_elem_n_click(driver, modal_page.close_large_modal)
        wait_until_elem_invisible(driver, modal_page.modal_title("Large Modal"))

        scroll_to_elem_n_click(driver, modal_page.large_modal)
        wait_until_elem_present(driver, modal_page.modal_title("Large Modal"))
        scroll_to_elem_n_click(driver, modal_page.close_btn)
        wait_until_elem_invisible(driver, modal_page.modal_title("Large Modal"))


@allure.title(WIDGETS)
class TestWidgets:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_widget_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, WIDGETS))
        wait_until_elem_has_text(driver, homepage.main_header, WIDGETS)

    def test_accordian(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Accordian"))
        wait_until_elem_has_text(driver, homepage.main_header, "Accordian")

        assert is_elem_displayed(driver, acc_page.content_1), f"Section 1 content is not displayed."

        assert not is_elem_displayed(driver, acc_page.content_2), f"Section 2 content is displayed."

        assert not is_elem_displayed(driver, acc_page.content_3), f"Section 3 content is displayed."

        scroll_to_elem_n_click(driver, acc_page.heading_2)

        wait_until_elem_present(driver, acc_page.content_2)

        wait_until_elem_invisible(driver, acc_page.content_1)

        scroll_to_elem_n_click(driver, acc_page.heading_3)

        wait_until_elem_invisible(driver, acc_page.content_2)

        wait_until_elem_present(driver, acc_page.content_3)

    colors = ["Red", "Blue", "Black"]

    def test_autocomplete(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Auto Complete"))
        wait_until_elem_has_text(driver, homepage.main_header, "Auto Complete")

        for color in self.colors:
            input_text(driver, auto_com_page.autocomplete_multiple_input, color)
            wait_until_elem_present(driver, auto_com_page.autocomplete_option(color))
            scroll_to_elem_n_click(driver, auto_com_page.autocomplete_option(color))
            wait_until_elem_present(driver, auto_com_page.autocomplete_labels(color))

        scroll_to_elem_n_click(driver, auto_com_page.autocomplete_remove(self.colors[1]))
        wait_until_elem_invisible(driver, auto_com_page.autocomplete_remove(self.colors[1]))

        input_text(driver, auto_com_page.autocomplete_single_input, "Green")
        wait_until_elem_present(driver, auto_com_page.autocomplete_option("Green"))
        scroll_to_elem_n_click(driver, auto_com_page.autocomplete_option("Green"))
        wait_until_elem_present(driver, auto_com_page.autocomplete_single_value)
        assert "Green" == get_text(driver, auto_com_page.autocomplete_single_value), f"Single color value is wrong"

    def test_slider(self, driver, ac):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Slider"))
        wait_until_elem_has_text(driver, homepage.main_header, "Slider")

        for x in [70, 100, -200]:
            ac.drag_and_drop_by_offset(driver.find_element(*slider_page.slider), x, 0).perform()
            slider_value = driver.find_element(*slider_page.slider).value_of_css_property("value")
            slider_value1 = driver.find_element(*slider_page.slider_value).value_of_css_property("value")
            assert slider_value == slider_value1, f"Slider values mismatch"

    def test_progress_bar(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Progress Bar"))
        wait_until_elem_has_text(driver, homepage.main_header, "Progress Bar")

        ini_progress = int(get_property_value(driver, p_bar_page.progress_bar, "aria-valuenow"))
        scroll_to_elem_n_click(driver, p_bar_page.start_stop_btn)
        time.sleep(4)
        scroll_to_elem_n_click(driver, p_bar_page.start_stop_btn)
        cur_progress = int(get_property_value(driver, p_bar_page.progress_bar, "aria-valuenow"))
        assert cur_progress > ini_progress, f"Progress is not increased"
        scroll_to_elem_n_click(driver, p_bar_page.start_stop_btn)
        wait_until_elem_present(driver, p_bar_page.reset_btn)
        scroll_to_elem_n_click(driver, p_bar_page.reset_btn)
        cur_progress = int(get_property_value(driver, p_bar_page.progress_bar, "aria-valuenow"))
        assert cur_progress == 0, f"Progress is not reset"

    def test_tabs(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Tabs"))
        wait_until_elem_has_text(driver, homepage.main_header, "Tabs")

        assert get_property_value(driver, tab_page.more_tab, "aria-disabled") == "true", f"More tab is not disabled"
        assert not is_elem_displayed(driver, tab_page.origin_panel), f"Origin panel is displayed"
        assert not is_elem_displayed(driver, tab_page.use_panel), f"Use panel is displayed"

        scroll_to_elem_n_click(driver, tab_page.origin_tab)
        wait_until_elem_present(driver, tab_page.origin_panel)
        assert not is_elem_displayed(driver, tab_page.what_panel), f"What panel is displayed"

        scroll_to_elem_n_click(driver, tab_page.use_tab)
        wait_until_elem_present(driver, tab_page.use_panel)
        assert not is_elem_displayed(driver, tab_page.origin_panel), f"What panel is displayed"

    def test_tooltips(self, driver, ac):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Tool Tips"))
        wait_until_elem_has_text(driver, homepage.main_header, "Tool Tips")

        time.sleep(2)

        ac.move_to_element(driver.find_element(*tooltip_page.tooltip_btn)).perform()
        wait_until_elem_has_text(driver, tooltip_page.tooltip, "You hovered over the Button")

        ac.move_to_element(driver.find_element(*tooltip_page.tooltip_text)).perform()
        wait_until_elem_has_text(driver, tooltip_page.tooltip, "You hovered over the text field")

        scroll_to_elem(driver, tooltip_page.contrary_text)
        ac.move_to_element(driver.find_element(*tooltip_page.contrary_text)).perform()
        wait_until_elem_has_text(driver, tooltip_page.tooltip, "You hovered over the Contrary")

    def test_menu(self, driver, ac):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Menu"))
        wait_until_elem_has_text(driver, homepage.main_header, "Menu")

        time.sleep(2)

        ac.move_to_element(driver.find_element(*menu_page.menu_item("Main Item 2"))).perform()
        wait_until_elem_present(driver, menu_page.menu_item("SUB SUB LIST »"))

        ac.move_to_element(driver.find_element(*menu_page.menu_item("SUB SUB LIST »"))).perform()
        wait_until_elem_present(driver, menu_page.menu_item("Sub Sub Item 1"))

    def test_select_menu(self, driver, ac):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Select Menu"))
        wait_until_elem_has_text(driver, homepage.main_header, "Select Menu")

        option = "Group 2, option 2"
        input_text(driver, select_menu_page.select_option_input, option)
        wait_until_elem_present(driver, select_menu_page.select_menu_option(option))
        scroll_to_elem_n_click(driver, select_menu_page.select_menu_option(option))
        wait_until_elem_has_text(driver, select_menu_page.select_option_value, option)

        option = "Dr."
        input_text(driver, select_menu_page.select_title_input, option)
        wait_until_elem_present(driver, select_menu_page.select_title_option(option))
        scroll_to_elem_n_click(driver, select_menu_page.select_title_option(option))
        wait_until_elem_has_text(driver, select_menu_page.select_title_value, option)

        color = "Yellow"
        old_select_menu = Select(driver.find_element(*select_menu_page.old_select_menu))
        old_select_menu.select_by_visible_text(color)
        assert old_select_menu.first_selected_option.text == color, f"{color} is not selected in the menu"

        options = ["Green", "Black"]
        for op in options:
            input_text(driver, select_menu_page.multi_select_input, op)
            wait_until_elem_present(driver, select_menu_page.multi_select_option(op))
            scroll_to_elem_n_click(driver, select_menu_page.multi_select_option(op))
            wait_until_elem_present(driver, select_menu_page.multi_select_value(op))

        cars = ["volvo", "opel", "audi"]
        std_multi_select_menu = Select(driver.find_element(*select_menu_page.std_multi_select))
        for car in cars:
            std_multi_select_menu.select_by_value(car)
        for option in std_multi_select_menu.all_selected_options:
            assert option.text.lower() in cars
        std_multi_select_menu.deselect_all()
        assert len(std_multi_select_menu.all_selected_options) == 0, f"All car options are not deselected"
        std_multi_select_menu.select_by_value(cars[0])
        assert len(std_multi_select_menu.all_selected_options) == 1, f"More car options selected"
        assert std_multi_select_menu.all_selected_options[0].text.lower() == cars[0], f"{cars[0]} is not selected"


@allure.title(INTERACTIONS)
class TestInteractions:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_interaction_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, INTERACTIONS))
        wait_until_elem_has_text(driver, homepage.main_header, INTERACTIONS)

    def test_sortable(self, driver, ac):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Sortable"))
        wait_until_elem_has_text(driver, homepage.main_header, "Sortable")

        old_items = ["One", "Two", "Three", "Four", "Five", "Six"]
        new_items = ["Two", "Three", "Four", "Five", "One", "Six"]

        scroll_to_elem(driver, sortable_page.list_item(old_items[5]))

        list_items = driver.find_elements(*sortable_page.list_items)
        for index, item in enumerate(list_items):
            assert item.text == old_items[index], f"Items mismatch"

        drag_n_drop(driver, ac, sortable_page.list_item(old_items[0]), sortable_page.list_item(old_items[4]))
        wait_until(driver, ec.text_to_be_present_in_element(sortable_page.nth_list_item(1), old_items[1]), 10)

        for index, item in enumerate(list_items):
            assert item.text == new_items[index], f"Items mismatch after drag n drop"

        old_items = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        new_items = ["One", "Two", "Four", "Five", "Six", "Seven", "Eight", "Three", "Nine"]

        scroll_to_elem_n_click(driver, sortable_page.grid_tab)
        wait_until_elem_present(driver, sortable_page.grid_item(old_items[0]))

        grid_items = driver.find_elements(*sortable_page.grid_items)
        for index, item in enumerate(grid_items):
            assert item.text == old_items[index], f"Items mismatch"

        drag_n_drop(driver, ac, sortable_page.grid_item(old_items[2]), sortable_page.grid_item(old_items[7]))
        wait_until(driver, ec.text_to_be_present_in_element(sortable_page.nth_grid_item(3), old_items[3]), 10)

        for index, item in enumerate(grid_items):
            assert item.text == new_items[index], f"Items mismatch after drag n drop"

    def test_selectable(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Selectable"))
        wait_until_elem_has_text(driver, homepage.main_header, "Selectable")

        items = [1, 2]

        for item in items:
            scroll_to_elem_n_click(driver, sortable_page.nth_list_item(item))

        for item in items:
            assert "active" in get_property_value(driver, sortable_page.nth_list_item(item), "class"),\
                f"{item} is not selected"

        scroll_to_elem_n_click(driver, sortable_page.grid_tab)
        wait_until_elem_present(driver, sortable_page.nth_grid_item(items[0]))

        for item in items:
            scroll_to_elem_n_click(driver, sortable_page.nth_grid_item(item))

        for item in items:
            assert "active" in get_property_value(driver, sortable_page.nth_grid_item(item), "class"),\
                f"{item} is not selected"

    def test_resizeable(self, driver):
        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Resizable"))
        wait_until_elem_has_text(driver, homepage.main_header, "Resizable")

        driver.execute_script("arguments[0].style='width: 300px; height: 250px;'",
                              driver.find_element(*resizeable_page.resizeable_restriction))

        assert "width: 300px; height: 250px;"\
               in get_property_value(driver, resizeable_page.resizeable_restriction, "style"), f"Box didn't resize"

        driver.execute_script("arguments[0].style='width: 300px; height: 250px;'",
                              driver.find_element(*resizeable_page.resizeable))

        assert "width: 300px; height: 250px;" \
               in get_property_value(driver, resizeable_page.resizeable, "style"), f"Box didn't resize"


@allure.title(BOOK_STORE)
class TestBookStoreApp:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_bookstore_page(self, driver):
        navigate_to_url(driver, URL, homepage.logo)
        scroll_to_elem_n_click(driver, homepage.card_elem(driver, BOOK_STORE))
        wait_until_elem_has_text(driver, homepage.main_header, "Book Store")

    # @pytest.fixture(scope="class", autouse=True)
    # def create_new_user(self, driver):
    #     navigate_to_url(driver, URL, homepage.logo)
    #     scroll_to_elem_n_click(driver, homepage.card_elem(driver, BOOK_STORE))
    #     wait_until_elem_has_text(driver, homepage.main_header, "Book Store")
    #     scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Login"))
    #     wait_until_elem_has_text(driver, homepage.main_header, "Login")
    #
    #     wait_until_elem_present(driver, book_store_page.new_user)
    #     scroll_to_elem_n_click(driver, book_store_page.new_user)
    #     wait_until_elem_present(driver, book_store_page.register)
    #     input_text(driver, book_store_page.f_name, book_store_f_name)
    #     input_text(driver, book_store_page.l_name, book_store_l_name)
    #     input_text(driver, book_store_page.username, book_store_user)
    #     input_text(driver, book_store_page.password, book_store_pass)
    #
    #     driver.switch_to.frame(driver.find_element(*book_store_page.captcha_frame))
    #     wait_until_elem_present(driver, book_store_page.captcha_checkbox)
    #     scroll_to_elem_n_click(driver, book_store_page.captcha_checkbox)
    #     driver.switch_to.parent_frame()
    #
    #     scroll_to_elem_n_click(driver, book_store_page.register)
    #     wait_until(driver, ec.alert_is_present())
    #     assert "User Register Successfully." in driver.switch_to.alert.text, f"User is not created successfully"
    #     driver.switch_to.alert.accept()
    #     wait_until(driver, ec.element_to_be_clickable(book_store_page.back_to_login))
    @pytest.fixture(scope="function", autouse=True)
    def login(self, driver, go_to_bookstore_page):

        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Login"))
        wait_until_elem_has_text(driver, homepage.main_header, "Login")

        wait_until_elem_present(driver, book_store_page.username)
        input_text(driver, book_store_page.username, book_store_user)
        input_text(driver, book_store_page.password, book_store_pass)

        assert book_store_user in get_property_value(driver, book_store_page.username, "value"), f"User name mismatch"
        assert book_store_pass in get_property_value(driver, book_store_page.password, "value"), f"Password mismatch"

        scroll_to_elem_n_click(driver, book_store_page.login)

    def test_login(self, driver):

        wait_until_elem_present(driver, book_store_page.submit_btn("Log out"))

        assert book_store_user == get_text(driver, book_store_page.username_value), f"User name mismatch in profile"

        scroll_to_elem_n_click(driver, book_store_page.submit_btn("Log out"))
        wait_until_elem_present(driver, book_store_page.login)

    def test_book_store_app(self, driver):
        wait_until_elem_present(driver, book_store_page.submit_btn("Log out"))

        scroll_to_elem_n_click(driver, book_store_page.submit_btn("Go To Book Store"))
        wait_until_elem_present(driver, book_store_page.book_link("Git Pocket Guide"))

        scroll_to_elem_n_click(driver, book_store_page.book_link("Git Pocket Guide"))
        wait_until_elem_present(driver, book_store_page.submit_btn("Add To Your Collection"))

        scroll_to_elem_n_click(driver, book_store_page.submit_btn("Add To Your Collection"))

        wait_until(driver, ec.alert_is_present())
        assert "Book added to your collection." in driver.switch_to.alert.text, f"Text in alert mismatch"
        driver.switch_to.alert.accept()

        scroll_to_elem_n_click(driver, homepage.sub_ele(driver, "Profile"))
        wait_until_elem_has_text(driver, homepage.main_header, "Profile")
        wait_until_elem_present(driver, book_store_page.book_link("Git Pocket Guide"))

        scroll_to_elem_n_click(driver, book_store_page.submit_btn("Delete All Books"))
        wait_until_elem_present(driver, book_store_page.delete_all_books_modal)
        scroll_to_elem_n_click(driver, book_store_page.delete_all_ok)

        wait_until(driver, ec.alert_is_present())
        assert "All Books deleted." in driver.switch_to.alert.text, f"Text in alert mismatch"
        driver.switch_to.alert.accept()

        is_elem_displayed(driver, book_store_page.book_link("Git Pocket Guide"))
        scroll_to_elem_n_click(driver, book_store_page.submit_btn("Log out"))
        wait_until_elem_present(driver, book_store_page.login)
