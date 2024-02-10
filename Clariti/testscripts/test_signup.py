import time
import allure
import pytest
from allure_commons.types import AttachmentType
from Clariti.pages.base_page import random_string
from Clariti.testscripts.base_test import BaseTest1, BaseTest3, BaseTest
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.utils import verify_status, status_report_update_to_xls


class TestSignup(BaseTest1):
    logger = LogGen.loggen()

    def test_Push(self):
        global status_tc_01
        generated_string1 = random_string(5)

        login_email = "triadqa1@yandex.com"
        login_password = "Welcome123$#@!"
        login_email1 = "triadqa8@gmail.com"
        login_password1 = "Welcome123$"
        login_email2 = "triadqa9@gmail.com"
        login_password2 = "Welcome123$"
        contactName = "Suriya S QA"
        From_Address = "Clariti Support"
        BrowserPassword = "Triad@#123"
        ClaritiName = "Triad QA1 YANDEX"
        ClaritiPassword = "Welcome123$#@!"
        option = "later"
        self.logger.info("* Mail test case TC_01 started *")

        status_tc_01 = None

        self.loginPage.clariti_sign_up(login_email, "", From_Address, login_email, BrowserPassword, ClaritiName, ClaritiPassword, option)
        #self.loginPage1.clariti_sign_in(login_email2, login_password2)
        #self.loginPage2.clariti_sign_in(login_email2, login_password2)

        #self.contactsPage.click_contacts_tab()
        #time.sleep(1)
        # found_row = self.contactsPage.get_contacts(subject)
        # if found_row:
        #     found_row.click()
        # else:
        #     print("contact not found")
        #self.contactsPage.block_contact(contact_name)
    #     # self.contactsPage.click_contact(contact_name)
    #     # time.sleep(0.1)
    #     # self.contactsPage.send_dc_message(generated_string1)
    #     # time.sleep(2)
    #     # self.homePage.click_hometab()
    #     # time.sleep(2)
    #     # self.contactsPage.hover_on_dc_contact(contact_name)
    #     # time.sleep(5)
    #     # self.contactsPage.click_on_dc_contact(contact_name)
    #
    #     #self.contactsPage.last_dc_messages(generated_string1)
    #     #time.sleep(15)
    #     #self.contactsPage.file_send(1)
    #     #time.sleep(5)
    #     #self.contactsPage.last_dc_messages("LoginData.xlsx")

    #     self.homePage.create_new_conversation(generated_string1)
    #     time.sleep(1)
    #     self.homePage.start_chat()
    #     self.contactsPage.contact_selection_ip_chat(contact_name)
    #     self.contactsPage.proceed_button_overlay()
    #    self.directChatPage.select_dc_contact_direct_chat(contact_name)

        time.sleep(10)