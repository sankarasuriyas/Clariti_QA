import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchWindowException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Clariti.pages.base_page import BasePage
from Clariti.utilities.locators import Locators


def get_domain(email):
    domain = email.split('@')[-1].split('.')[-2]
    return domain


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # username = (By.XPATH, "//input[@name='somethingAutofillDoesntKnow']")
    # password = (By.XPATH, "//*[@class='im-au-login-password']/input")
    # login_button = (By.CSS_SELECTOR, "button.im-au-custom-login-btn")
    # homepage_ui = (By.XPATH, "//div[@class='im-floatingdlg-section-people im-app-leftside-pane']")
    # improper_logout_alert = (By.XPATH, '//span[contains(text(),"Yes")]')
    # onboarding_ui = (By.XPATH, "//div[@class='im-td-onboarding-options-container']")
    # onboarding_ui_later_option = (By.CSS_SELECTOR, f"[class*='{'im-td-onboardingoption-dialog dialog1'}']")
    # onboarding_ui_now_option = (By.CSS_SELECTOR, f"[class*='{'im-td-onboardingoption-dialog dialog2'}']")
    # onboarding_ui_selection_text = (By.CLASS_NAME, "im-td-onboardingoption-text1")
    # # continue_button1 = (By.CSS_SELECTOR, f"[class*='{'im-td-continue-btn'}']")
    # login_with_microsoft_button = (By.XPATH,
    #                                "//*[@class='im-au-btemplate-socialText' and text()='Login with Microsoft']")
    # login_with_google_button = (By.XPATH, "//*[@class='im-au-btemplate-socialText' and text()='Login with Google']")
    # login_with_yahoo_button = (By.XPATH, "//*[@class='im-au-btemplate-socialText' and text()='Login with Yahoo']")
    # login_with_apple_button = (By.XPATH, "//*[@class='im-au-btemplate-socialText' and text()='Login with Apple']")
    # profile_name_container = (By.CLASS_NAME, "im-np-hm-userNameSpan")
    # logout = (By.XPATH, ".//*[contains(text(), 'logout')]")
    # microsoft_email = (By.XPATH, "//input[@type='email']")
    # Locators.LoginPage.MICROSOFT_EMAIL_NEXT = (By.XPATH, "//input[@type='submit']")
    # microsoft_password = (By.XPATH, "//input[@name='passwd']")
    # MICROSOFT_PASSWORD_NEXT = (By.XPATH, "//input[@type='submit']")
    # microsoft_signin_ui = (By.XPATH, "//*[@text()='Stay signed in?']")
    # microsoft_signin_button = (By.XPATH, "//input[@type='submit']")
    # google_email = (By.XPATH, "//input[@id='identifierId']")
    # GOOGLE_EMAIL_NEXT = (By.ID, "identifierNext")
    # google_password = (By.XPATH, "//input[@type='password']")
    # GOOGLE_PASSWORD_NEXT = (By.ID, "passwordNext")
    # yahoo_email = (By.XPATH, "//input[@id='login-username']")
    # yahoo_email_next = (By.XPATH, "//input[@name='signin']")
    # yahoo_password = (By.XPATH, "//input[@id='login-passwd']")
    # yahoo_password_next = (By.XPATH, "//button[@id='login-signin']")
    # yandex_userid_textbox = (By.XPATH, "//input[@id='passp-field-login']")
    # yandex_login_button = (By.XPATH, "//button[@type='submit']")
    # yandex_password_textbox = (By.XPATH, "//input[@id='passp-field-passwd']")
    # yandex_forgot_password_link = (By.ID, "field:link-passwd")
    # yandex_homepage = (By.CLASS_NAME, "PSHeader-Left")
    # yandex_inbox_items = (By.CSS_SELECTOR, ".ns-view-container-desc.mail-MessagesList.js-messages-list")
    # yandex_inbox_item_row = (By.XPATH, "//*[@class='mail-MessageSnippet-Content']")
    # from_address_class = (By.CSS_SELECTOR,
    #                       ".mail-MessageSnippet-Item.mail-MessageSnippet-Item_sender.js-message-snippet-sender")
    # from_address = (By.CLASS_NAME, "mail-MessageSnippet-FromText")
    # sign_up_button_mail = (By.XPATH, "//a[normalize-space()='Click here to set up your password']")
    # signup_href_links = (By.CSS_SELECTOR, "a[href]")
    # enter_name_custom_signup = (By.CSS_SELECTOR, "input[placeholder='Enter name']")
    # Locators.LoginPage.ENTER_PASSWORD_CUSTOM_SIGNUP = (By.CSS_SELECTOR, "input[placeholder='Enter password']")
    # enter_re_enter_custom_signup = (By.CSS_SELECTOR, "input[placeholder='Re-enter password']")
    # signup_button = (By.XPATH, "//*[@class='im-au-custom-proceed-button' and text()=' Sign up ']")
    # onboarding_container = (By.CLASS_NAME, "im-td-onboarding-options-container")
    # invite_later = (By.CSS_SELECTOR, f"[class*='{'im-td-onboardingoption-dialog dialog1'}']")
    # invite_now = (By.CSS_SELECTOR, f"[class*='{'im-td-onboardingoption-dialog dialog2'}']")
    # invite_option_text = (By.CLASS_NAME, "im-td-onboardingoption-text1")
    # continue_button = (By.XPATH, "//button/span[contains(text(), 'Continue')]")
    # lets_go_button = (By.CSS_SELECTOR, f"[class*='{'im-da-letsgobutton'}']")

    def clariti_sign_in(self, email, password):
        domain = get_domain(email)
        print("Login to clariti with " + domain + " domain login")

        if domain == "gmail":
            self.google_sign_in(email, password)

        elif domain == "yahoo":
            self.yahoo_sign_in(email, password)

        elif domain == "outlook":
            self.microsoft_sign_in(email, password)

        elif domain in ["cadcam-e", "triad-india", "rediffmail", "yandex", "aol"]:
            self.custom_sign_in(email, password)

        time.sleep(1)

        # wait until home tab appears
        Homepage = self.wait_until_login_success()
        if Homepage:
            # return True
            print("Login Success")
        else:
            # print("Login not success")
            # return False
            allure.attach(self.driver.get_screenshot_as_png(), name="User B Login Failed",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("Login to Clariti Failed!.")

    def microsoft_sign_in(self, email, password):
        # Getting current window handle
        current_window = self.driver.current_window_handle

        # clicking Login with Microsoft button
        self.click(Locators.LoginPage.LOGIN_WITH_MICROSOFT_BUTTON)

        time.sleep(2)
        try:
            # wait until handle becomes more than 1
            WebDriverWait(self.driver, 20).until(lambda driver: len(driver.window_handles) > 1)
        except TimeoutException or NoSuchWindowException or NoSuchElementException:
            print("Oauth window not opened due to some Issues ")
            pytest.fail("Oauth window not opened due to some Issues")

        # Get all the window handle
        window_handles = self.driver.window_handles

        # Switch to the new window
        for handle in window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break
        new_handle = self.driver.current_window_handle
        # Enter Outlook address
        self.send_keys(Locators.LoginPage.MICROSOFT_EMAIL, email)

        # Click Next button in Enter email address page
        self.click(Locators.LoginPage.MICROSOFT_EMAIL_NEXT)

        time.sleep(2)

        # Wait until password page opens
        self.wait_for_element(Locators.LoginPage.MICROSOFT_PASSWORD)

        # Enter Gmail Password
        self.send_keys(Locators.LoginPage.MICROSOFT_PASSWORD, password)

        # Click Next button in password page
        self.click(Locators.LoginPage.MICROSOFT_PASSWORD_NEXT)
        time.sleep(2)
        self.click(Locators.LoginPage.MICROSOFT_SIGNIN_BUTTON)

        # focusing to old window handle
        WebDriverWait(self.driver, 30).until(lambda driver: len(driver.window_handles) == len(window_handles) - 1)

        self.driver.switch_to.window(current_window)

    def google_sign_in(self, email, password):
        # Getting current window handle
        current_window = self.driver.current_window_handle

        # clicking Login with Google button
        self.click(Locators.LoginPage.LOGIN_WITH_GOOGLE_BUTTON)

        time.sleep(2)
        try:
            # wait until handle becomes more than 1
            WebDriverWait(self.driver, 20).until(lambda driver: len(driver.window_handles) > 1)
        except TimeoutException or NoSuchWindowException or NoSuchElementException:
            print("Oauth window not opened due to some Issues ")
            pytest.fail("Oauth window not opened due to some Issues")

        # Get all the window handle
        window_handles = self.driver.window_handles

        # Switch to the new window
        for handle in window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break

        new_handle = self.driver.current_window_handle

        # Enter Gmail address
        self.send_keys(Locators.LoginPage.GOOGLE_EMAIL, email)

        # Click Next button in Enter email address page
        self.click(Locators.LoginPage.GOOGLE_EMAIL_NEXT)

        time.sleep(2)

        # Wait until password page opens
        self.wait_for_element(Locators.LoginPage.GOOGLE_PASSWORD)

        # Enter Gmail Password
        self.send_keys(Locators.LoginPage.GOOGLE_PASSWORD, password)

        # Click Next
        self.click(Locators.LoginPage.GOOGLE_PASSWORD_NEXT)

        # focusing to old window handle
        WebDriverWait(self.driver, 30).until(lambda driver: len(driver.window_handles) == len(window_handles) - 1)

        self.driver.switch_to.window(current_window)

    def yahoo_sign_in(self, email, password):
        # Getting current window handle
        current_window = self.driver.current_window_handle

        # clicking Login with Google button
        self.click(Locators.LoginPage.LOGIN_WITH_YAHOO_BUTTON)

        time.sleep(2)
        try:
            # wait until handle becomes more than 1
            WebDriverWait(self.driver, 20).until(lambda driver: len(driver.window_handles) > 1)
        except TimeoutException or NoSuchWindowException or NoSuchElementException:
            print("Oauth window not opened due to some Issues ")
            pytest.fail("Oauth window not opened due to some Issues")

        # Get all the window handle
        window_handles = self.driver.window_handles

        # Switch to the new window
        for handle in window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break

        new_handle = self.driver.current_window_handle

        # Enter Gmail address
        self.send_keys(Locators.LoginPage.YAHOO_EMAIL, email)

        # Click Next button in Enter email address page
        self.click(Locators.LoginPage.YAHOO_EMAIL_NEXT)

        time.sleep(2)

        # Wait until password page opens
        self.wait_for_element(Locators.LoginPage.YAHOO_PASSWORD)

        # Enter Gmail Password
        self.send_keys(Locators.LoginPage.YAHOO_PASSWORD, password)

        # Click Next
        self.click(Locators.LoginPage.YAHOO_PASSWORD_NEXT)

        # focusing to old window handle
        WebDriverWait(self.driver, 30).until(lambda driver: len(driver.window_handles) == len(window_handles) - 1)

        self.driver.switch_to.window(current_window)

    def custom_sign_in(self, email, password):

        self.send_keys(Locators.LoginPage.USERNAME, email)
        self.send_keys(Locators.LoginPage.PASSWORD, password)
        self.click(Locators.LoginPage.LOGIN_BUTTON)

    def wait_until_login_success(self):
        start_time = time.time()
        timeout = 60
        while time.time() - start_time < timeout:
            try:
                main_element = self.get_elements(Locators.LoginPage.HOMEPAGE_UI)
                if main_element:
                    print("Home Page appears and loaded")
                    return True
                else:
                    dialog_alert = self.get_elements(Locators.LoginPage.IMPROPER_LOGOUT_ALERT)
                    if dialog_alert and dialog_alert[0].is_displayed():
                        dialog_alert[0].click()
                        print("Improper logout Alert appears and click Yes Button")
                        time.sleep(1)  # Wait for the page to update after clicking
            except:
                # pass
                WebDriverWait(self.driver, 1)

            time.sleep(1)  # Wait before checking again

        print("Home page not loaded due to Oauth Issue or Network Issue")
        return False

    def clariti_sign_up(self, email, password, from_address, custom_login_id, custom_login_password,
                        clariti_name, clariti_password, option):
        domain = get_domain(email)
        print("Signup to clariti with " + domain + " domain login")

        if domain == "gmail":
            self.google_sign_in(email, password)

        elif domain == "yahoo":
            self.yahoo_sign_in(email, password)

        elif domain == "outlook":
            self.microsoft_sign_in(email, password)

        elif domain in ["cadcam-e", "triad-india", "rediffmail", "yandex", "aol"]:
            self.custom_sign_up(email, from_address, custom_login_id, custom_login_password,
                                clariti_name, clariti_password)

        time.sleep(1)

        # wait until home tab appears
        self.wait_until_signup_success()

        self.proceed_from_onboarding(option)

        HomePageUi = self.wait_until_login_success()

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DELETE).perform()
        time.sleep(1)
        self.driver.close()

        if HomePageUi:
            # return True
            print("Signup Success")
        else:
            # print("Login not success")
            # return False
            allure.attach(self.driver.get_screenshot_as_png(), name="Sign Up Failed",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("Signup to Clariti Failed!.")

    def custom_sign_up(self, email, from_address, custom_login_id, custom_login_password,
                       clariti_name, clariti_password):
        self.send_keys(Locators.LoginPage.USERNAME, email)
        self.click(Locators.LoginPage.LOGIN_BUTTON)
        domain = get_domain(email)
        if domain == 'yandex':
            self.yandex_mail_click(from_address, custom_login_id, custom_login_password)
            self.custom_signup_enter_details(clariti_name, clariti_password)

    def wait_until_signup_success(self):
        start_time = time.time()
        timeout = 60
        while time.time() - start_time < timeout:
            try:
                main_element = self.get_elements(Locators.LoginPage.ONBOARDING_UI)
                if main_element:
                    print("Home Page appears and loaded")
                    return True
            except:
                # pass
                WebDriverWait(self.driver, 1)

            time.sleep(1)  # Wait before checking again

        print("Home page not loaded due to Oauth Issue or Network Issue")
        return False

    def yandex_mail_click(self, from_address, yandex_email_id, yandex_password):
        self.driver.get("https://passport.yandex.com/auth?retpath=https%3A%2F%2Fmail.yandex.com")
        self.send_keys(Locators.LoginPage.YANDEX_USERID_TEXTBOX, yandex_email_id)
        self.click(Locators.LoginPage.YANDEX_LOGIN_BUTTON)
        self.wait_for_element(Locators.LoginPage.YANDEX_FORGOT_PASSWORD_LINK)
        self.send_keys(Locators.LoginPage.YANDEX_PASSWORD_TEXTBOX, yandex_password)
        self.click(Locators.LoginPage.YANDEX_LOGIN_BUTTON)
        self.wait_until_yandex_inbox_loaded()
        time.sleep(1)
        self.get_mail_items(from_address)
        time.sleep(1)
        self.click_signup_link()
        time.sleep(1)

    def wait_until_yandex_inbox_loaded(self):
        start_time = time.time()
        timeout = 60
        while time.time() - start_time < timeout:
            try:
                main_element = self.get_elements(Locators.LoginPage.YANDEX_HOMEPAGE)
                if main_element:
                    print("Home Page appears and loaded")
                    return True
            except:
                # pass
                WebDriverWait(self.driver, 1)

            time.sleep(1)  # Wait before checking again

        print("Home page not loaded due to Oauth Issue or Network Issue")
        return False

    def get_mail_items(self, from_address):

        # Get the table body element
        table = self.get_element(Locators.LoginPage.YANDEX_INBOX_ITEMS)

        # Find all the rows in the table
        rows = table.find_elements(*Locators.LoginPage.YANDEX_INBOX_ITEM_ROW)

        for row in rows:

            From_cell = row.find_element(*Locators.LoginPage.FROM_ADDRESS_CLASS)
            From_address_name = From_cell.find_elements(*Locators.LoginPage.FROM_ADDRESS)
            for item in From_address_name:
                if from_address == item.text:
                    item.click()
                    return

    def click_signup_link(self):
        AllLinks = self.get_elements(Locators.LoginPage.SIGNUP_HREF_LINKS)
        for link in AllLinks:
            if "qa.clariti.app" in link.text:
                # print(link.text)
                # actions = ActionChains(self.driver)
                # actions.context_click(link).perform()
                time.sleep(1)
                href_value = link.get_attribute("href")
                new_tab_script = "window.open('{}');".format(href_value)
                self.driver.execute_script(new_tab_script)
                # Switch to the new tab
                self.driver.switch_to.window(self.driver.window_handles[-1])
                break

    def custom_signup_enter_details(self, clariti_name, clariti_password):
        self.send_keys(Locators.LoginPage.ENTER_NAME_CUSTOM_SIGNUP, clariti_name)
        self.send_keys(Locators.LoginPage.ENTER_PASSWORD_CUSTOM_SIGNUP, clariti_password)
        self.send_keys(Locators.LoginPage.ENTER_RE_ENTER_CUSTOM_SIGNUP, clariti_password)
        self.click(Locators.LoginPage.SIGNUP_BUTTON)
        # self.wait_until_signup_success()

    def proceed_from_onboarding(self, option):
        if option == 'later':
            LaterOption = self.get_element(Locators.LoginPage.INVITE_LATER)
            SelectLaterOption = LaterOption.find_element(*Locators.LoginPage.INVITE_OPTION_TEXT)
            SelectLaterOption.click()
            time.sleep(1)
            self.click(Locators.LoginPage.CONTINUE_BUTTON)
            self.wait_until_login_success()
            time.sleep(1)
            self.click(Locators.LoginPage.LETS_GO_BUTTON)
        elif option == 'now':
            nowOption = self.get_element(Locators.LoginPage.INVITE_NOW)
            SelectNowOption = nowOption.find_element(*Locators.LoginPage.INVITE_OPTION_TEXT)
            SelectNowOption.click()
            self.click(Locators.LoginPage.CONTINUE_BUTTON)