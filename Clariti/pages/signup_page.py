import time
from selenium.webdriver.common.by import By
from Clariti.pages.base_page import BasePage
from Clariti.utilities.locators import Locators


def get_domain(email):
    domain = email.split('@')[-1].split('.')[-2]
    return domain


class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # username = (By.XPATH, "//input[@name='somethingAutofillDoesntKnow']")
    # password = (By.XPATH, "//*[@class='im-au-login-password']/input")
    # signup_button = (By.CSS_SELECTOR, "button.im-au-custom-login-btn")
    #
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
    # Sign_up_button_mail = (By.XPATH, "//a[normalize-space()='Click here to set up your password']")
    # onboarding_container = (By.CLASS_NAME, "im-td-onboarding-options-container")
    # invite_later = (By.CLASS_NAME, "im-td-onboardingoption-text1")
    # continue_button = (By.XPATH, "//button/span[contains(text(), 'Continue')]")

    def clariti_sign_up(self, email, subject, yandex_email_id, yandex_password):
        domain = get_domain(email)
        print("Signup to clariti with " + domain + " domain login")

        if domain == "gmail":
            # GmailSignIn(driver, email, password)
            pass

        elif domain == "yahoo":
            # yahoo_sign_in(driver, email, password)
            pass

        elif domain == "outlook":
            # self.microsoft_sign_in(email, password)
            pass

        elif domain in ["cadcam-e", "triad-india", "rediffmail", "yandex", "aol"]:
            # self.custom_sign_up(email)
            pass

        time.sleep(1)

        #self.yandex_mail_click(subject, yandex_email_id, yandex_password)

        # # wait until home tab appears
        # Onboarding = self.wait_until_login_success()
        # if Onboarding:
        #     #return True
        #     print("Signup Success")
        # else:
        #     # print("Login not success")
        #     # return False
        #     allure.attach(self.driver.get_screenshot_as_png(), name="User B Signup Failed",
        #                   attachment_type=AttachmentType.PNG)
        #     pytest.fail("Signup to Clariti Failed!.")

    def custom_sign_up(self, email):

        self.send_keys(Locators.SignUpPage.USERNAME, email)
        self.click(Locators.SignUpPage.SIGNUP_BUTTON)





