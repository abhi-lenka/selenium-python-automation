from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from utility.demo_qa_utils import *


class HomePage(PageFactory):

    logo = (By.XPATH, f"//a[@href='{URL}']")

    @staticmethod
    def card_elem(driver, text):
        return driver.find_element(By.XPATH, f"//div[@class='category-cards']//h5[contains(text(), '{text}')]")

    main_header = (By.CLASS_NAME, "main-header")

    @staticmethod
    def left_panel_elem(driver, text):
        return driver.find_element(By.XPATH, f"//div[@class='left-pannel']//div[@class='header-text'][contains(text(),"
                                             f"'{text}')]")

    @staticmethod
    def sub_ele(driver, text):
        return driver.find_element(By.XPATH, f"//div[@class='left-pannel']//span[contains(text(),'{text}')]/..")


class ElementsPage(PageFactory):

    # Input elements
    username = (By.ID, "userName")
    email = (By.ID, "userEmail")
    current_addr = (By.ID, "currentAddress")
    permanent_addr = (By.ID, "permanentAddress")
    submit = (By.ID, "submit")

    # Output elements
    out_user = (By.CSS_SELECTOR, "#output #name")
    out_email = (By.CSS_SELECTOR, "#output #email")
    out_curr_addr = (By.CSS_SELECTOR, "#output #currentAddress")
    out_perm_addr = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPage(PageFactory):

    toggle_closed = (By.CSS_SELECTOR, "button[title='Toggle'] .rct-icon-expand-close")
    toggle_opened = (By.CSS_SELECTOR, "button[title='Toggle'] .rct-icon-expand-open")

    @staticmethod
    def check_box(text):
        return By.XPATH, f"//span[@class='rct-title'][contains(text(),'{text}')]//..//input[@type='checkbox']"

    check_box_icon = (By.XPATH, "//..//*[contains(@class,'rct-icon-uncheck')]")


class RadioButtonPage(PageFactory):

    radio_yes = (By.ID, "yesRadio")
    radio_yes_label = (By.CSS_SELECTOR, "[for='yesRadio']")
    radio_impressive = (By.ID, "impressiveRadio")
    radio_impressive_label = (By.CSS_SELECTOR, "[for='impressiveRadio']")
    radio_no = (By.ID, "noRadio")
    radio_text = (By.CLASS_NAME, "text-success")


class WebTables(PageFactory):

    add = (By.ID, "addNewRecordButton")

    @staticmethod
    def t_cell(text):
        return By.XPATH,\
            f"//div[@class='rt-tbody']//div[@ role='rowgroup']//div[@role='gridcell'][contains(text(),'{text}')]"

    delete_record = (By.XPATH, "//span[contains(@id,'delete-record')]")
    edit_record = (By.XPATH, "//span[contains(@id,'edit-record')]")

    # Registration form
    registration_form = (By.ID, "registration-form-modal")
    form_first_name = (By.CSS_SELECTOR, "#userForm #firstName")
    form_last_name = (By.CSS_SELECTOR, "#userForm #lastName")
    form_email = (By.CSS_SELECTOR, "#userForm #userEmail")
    form_age = (By.CSS_SELECTOR, "#userForm #age")
    form_salary = (By.CSS_SELECTOR, "#userForm #salary")
    form_dep = (By.CSS_SELECTOR, "#userForm #department")
    form_submit = (By.CSS_SELECTOR, "#userForm #submit")


class Buttons(PageFactory):

    double_click_btn = (By.ID, "doubleClickBtn")
    right_click_btn = (By.ID, "rightClickBtn")
    click_me_btn = (By.XPATH, "//button[text()='Click Me']")
    double_click_msg = (By.ID, "doubleClickMessage")
    right_click_msg = (By.ID, "rightClickMessage")
    dynamic_click_msg = (By.ID, "dynamicClickMessage")


class Links(PageFactory):

    simple_link = (By.ID, "simpleLink")
    dynamic_link = (By.ID, "dynamicLink")
    created = (By.ID, "created")
    no_content = (By.ID, "no-content")
    moved = (By.ID, "moved")
    bad_request = (By.ID, "bad-request")
    un_auth = (By.ID, "unauthorized")
    forbidden = (By.ID, "forbidden")
    invalid_url = (By.ID, "invalid-url")
    link_response = (By.ID, "linkResponse")


class BrokenLinks(PageFactory):

    valid_image = (By.XPATH, "//p[contains(text(),'Valid image')]//following-sibling::img[1]")
    broken_image = (By.XPATH, "//p[contains(text(),'Broken image')]//following-sibling::img[1]")
    valid_link = (By.XPATH, "//a[text()='Click Here for Valid Link']")
    broken_link = (By.XPATH, "//a[text()='Click Here for Broken Link']")


class UploadDownload(PageFactory):

    download = (By.ID, "downloadButton")
    upload = (By.ID, "uploadFile")
    upload_file_path = (By.ID, "uploadedFilePath")


class DynamicProp(PageFactory):

    enable_after = (By.ID, "enableAfter")
    color_change = (By.ID, "colorChange")
    visible_after = (By.ID, "visibleAfter")
