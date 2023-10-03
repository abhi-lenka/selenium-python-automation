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


class TextBoxPage(PageFactory):

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


class PracticeForm(PageFactory):

    f_name = (By.ID, "firstName")
    l_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")

    @staticmethod
    def gender(text):
        return By.CSS_SELECTOR, f"[type='radio'][value='{text}']"

    @staticmethod
    def gender_label(text):
        return By.XPATH, f"//input[@type='radio'][@value='{text}']//parent::div"

    mobile = (By.ID, "userNumber")
    dob = (By.ID, "dateOfBirthInput")
    subjects = (By.ID, "subjectsInput")

    @staticmethod
    def hobby_c_box(text):
        return By.XPATH, f"//div[@id='hobbiesWrapper']//label[text()='{text}']//parent::div//input"

    @staticmethod
    def hobby_c_box_label(text):
        return By.XPATH, f"//div[@id='hobbiesWrapper']//label[text()='{text}']"

    upload_pic = (By.ID, "uploadPicture")
    current_addr = (By.ID, "currentAddress")
    state = (By.CSS_SELECTOR, "#state input")
    city = (By.CSS_SELECTOR, "#city input")
    submit = (By.ID, "submit")

    submit_form_header = (By.XPATH,
                          "//div[contains(@class,'modal-title')][contains(text(),'Thanks for submitting the form')]")

    @staticmethod
    def table_row(text):
        return By.XPATH, f"//td[text()='{text}']"

    close_modal = (By.ID, "closeLargeModal")


class BrowserWindows(PageFactory):

    new_tab = (By.ID, "tabButton")
    new_window = (By.ID, "windowButton")
    new_window_msg = (By.ID, "messageWindowButton")


class Alerts(PageFactory):

    alert_btn = (By.ID, "alertButton")
    timer_alert_btn = (By.ID, "timerAlertButton")
    confirm_btn = (By.ID, "confirmButton")
    confirm_result = (By.ID, "confirmResult")
    prompt_btn = (By.ID, "promtButton")
    prompt_result = (By.ID, "promptResult")


class Frames(PageFactory):

    sample_h = (By.ID, "sampleHeading")
    child_frame = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")


class Modals(PageFactory):

    small_modal = (By.ID, "showSmallModal")
    large_modal = (By.ID, "showLargeModal")

    @staticmethod
    def modal_title(text):
        return By.XPATH, f"//div[contains(@class,'modal-title')][text()='{text}']"

    close_btn = (By.XPATH, "//span[text()='Close']//parent::button")
    close_small_modal = (By.ID, "closeSmallModal")
    close_large_modal = (By.ID, "closeLargeModal")


class Accordian(PageFactory):

    heading_1 = (By.ID, "section1Heading")
    heading_2 = (By.ID, "section2Heading")
    heading_3 = (By.ID, "section3Heading")
    content_1 = (By.ID, "section1Content")
    content_2 = (By.ID, "section2Content")
    content_3 = (By.ID, "section3Content")


class AutoComplete(PageFactory):

    autocomplete_multiple_input = (By.ID, "autoCompleteMultipleInput")

    @staticmethod
    def autocomplete_option(text):
        return By.XPATH, f"//div[contains(@class,'auto-complete__menu')]" \
                         f"//div[contains(@class,'auto-complete__option')][text()='{text}']"

    @staticmethod
    def autocomplete_labels(text):
        return By.XPATH, f"//div[contains(@class,'auto-complete__multi-value__label')][text()='{text}']"

    @staticmethod
    def autocomplete_remove(text):
        return By.XPATH, f"//div[contains(@class,'auto-complete__multi-value__label')][text()='{text}']" \
                         f"//following-sibling::div[contains(@class,'auto-complete__multi-value__remove')]"

    autocomplete_single_input = (By.ID, "autoCompleteSingleInput")
    autocomplete_single_value = (By.XPATH, "//div[contains(@class,'auto-complete__single-value')]")


class Slider(PageFactory):

    slider = (By.CSS_SELECTOR, "#sliderContainer [type='range']")
    slider_value = (By.ID, "sliderValue")


class ProgressBar(PageFactory):

    start_stop_btn = (By.ID, "startStopButton")
    progress_bar = (By.CSS_SELECTOR, "#progressBar [role='progressbar']")
    reset_btn = (By.ID, "resetButton")


class Tabs(PageFactory):

    what_tab = (By.ID, "demo-tab-what")
    origin_tab = (By.ID, "demo-tab-origin")
    use_tab = (By.ID, "demo-tab-use")
    more_tab = (By.ID, "demo-tab-more")
    what_panel = (By.ID, "demo-tabpane-what")
    origin_panel = (By.ID, "demo-tabpane-origin")
    use_panel = (By.ID, "demo-tabpane-use")


class ToolTips(PageFactory):

    tooltip_btn = (By.ID, "toolTipButton")
    tooltip_text = (By.ID, "toolTipTextField")
    contrary_text = (By.XPATH, "//a[text()='Contrary']")
    tooltip = (By.CLASS_NAME, "tooltip-inner")


class Menu(PageFactory):

    @staticmethod
    def menu_item(text):
        return By.XPATH, f"//a[text()='{text}']"


class SelectMenu(PageFactory):

    select_option_input = (By.ID, "react-select-2-input")
    select_option_value = (By.XPATH, "//div[@id='withOptGroup']//div[contains(@class,'singleValue')]")

    @staticmethod
    def select_menu_option(text):
        return By.XPATH, f"//div[contains(@id, 'react-select-2-option')][contains(text(),'{text}')]"

    select_title_input = (By.ID, "react-select-3-input")
    select_title_value = (By.XPATH, "//div[@id='selectOne']//div[contains(@class,'singleValue')]")

    @staticmethod
    def select_title_option(text):
        return By.XPATH, f"//div[contains(@id, 'react-select-3-option')][contains(text(),'{text}')]"

    old_select_menu = (By.ID, "oldSelectMenu")

    multi_select_input = (By.ID, "react-select-4-input")

    @staticmethod
    def multi_select_option(text):
        return By.XPATH, f"//div[contains(@id, 'react-select-4-option')][contains(text(),'{text}')]"

    @staticmethod
    def multi_select_value(text):
        return By.XPATH, f"//div[contains(@class,'multiValue')]//child::div[contains(text(),'{text}')]"

    std_multi_select = (By.ID , "cars")


class Sortable(PageFactory):

    list_tab = (By.ID, "demo-tab-list")
    list_items = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

    @staticmethod
    def list_item(text):
        return By.XPATH, f"//div[@id='demo-tabpane-list']//div[contains(@class,'list-group-item')]" \
                         f"[contains(text(),'{text}')]"

    @staticmethod
    def nth_list_item(n):
        return By.XPATH, f"//div[@id='demo-tabpane-list']//*[contains(@class,'list-group-item')][{n}]"

    grid_tab = (By.ID, "demo-tab-grid")
    grid_items = (By.CSS_SELECTOR, "#demo-tabpane-grid .list-group-item")

    @staticmethod
    def grid_item(text):
        return By.XPATH, f"//div[@id='demo-tabpane-grid']//div[contains(@class,'list-group-item')]" \
                         f"[contains(text(),'{text}')]"

    @staticmethod
    def nth_grid_item(n):
        return By.XPATH, f"//div[@id='demo-tabpane-grid']//*[contains(@class,'list-group-item')][{n}]"


class Resizeable(PageFactory):

    resizeable_restriction = (By.ID, "resizableBoxWithRestriction")
    resizeable = (By.ID, "resizable")
