import time
import allure
import pytest
from Clariti.pages.base_page import random_string, upload_files
from Clariti.testscripts.base_test import BaseTest, BaseTest1
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.utils import verify_status, status_report_update_to_xls


class TestDirectChat(BaseTest):
    logger = LogGen.loggen()

    # pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_01 - User A add User B contact and User B contact should focused. "
                        "User B side, User A contact should not Add.")
    def test_dc_01(self):
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadqa2@aol.com"
        UserB_password = "Welcome123$#@!"
        UserB_name = "Triadqa2 AOL"
        test_case_number = "TC_01"
        sheet_name = "Direct Chat"
        status_tc_01 = None
        status_dict = {
            "TC_01": status_tc_01
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Add User B contact and Verify contact is Focused"):
                Check = self.contactsPage.verify_contact_added_and_dc_focused(UserB_name)
                time.sleep(2)

            with allure.step("Verify contact Added in User A side"):
                self.directChatPage.verify_dc_contact_under_contacts(UserB_name)
                time.sleep(1)

            with allure.step("Verify contact Added in User A side in Direct chat tab"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.verify_dc_contact_in_contacts_tab(UserB_name)

            with allure.step("Verify contact not Added in User B side"):
                self.directChatPage1.verify_dc_contact_not_exists(UserA_name)

            with allure.step("Verify contact Added in User A side in Direct chat tab"):
                self.contactsPage1.click_contacts_tab()
                time.sleep(1)
                self.contactsPage1.verify_dc_contact_not_exists_in_contacts_tab(UserA_name)
                if Check:
                    status_tc_01 = True
                    status_dict["TC_01"] = status_tc_01

            with allure.step("Block User B contact in User A side"):
                with allure.step("Verify User B contact present or not to Block"):
                    self.contactsPage.block_contact(UserB_name)
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:

            verify_status(test_case_number, status_tc_01)
            status_report_update_to_xls(sheet_name, status_tc_01, test_case_number)

            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_02 - User A add User B contact and send a message, "
                        "User B side contact added and Block UI should appears")
    def test_dc_02(self):
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "clarititriad9@yandex.com"
        UserB_password = "Welcome123$"
        UserB_name = "ClaritTriad9 Automation"
        generated_string = random_string(5)
        dc_message = "Tc_02_Message - " + generated_string
        test_case_number = "TC_02"
        sheet_name = "Direct Chat"
        status_tc_02 = None
        status_dict = {
            "TC_02": status_tc_02
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Add User B contact and Verify contact is Focused"):
                self.contactsPage.verify_contact_added_and_dc_focused(UserB_name)
                time.sleep(2)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_02 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received message along with New message strip"):
                Check2 = self.directChatPage1.verify_last_dc_message(dc_message)
                if not Check2:
                    pytest.fail("TC_02 - " + dc_message + " , This DC message is not available")

            with allure.step("Verify Block UI in User A DC tab from User B"):
                Check3 = self.directChatPage1.verify_block_ui_dc_tab()
                if Check1 and Check2 and Check3:
                    status_tc_02 = True
                    status_dict["TC_02"] = status_tc_02

            with allure.step("Block User B contact in User A side"):
                with allure.step("Verify User B contact present or not to Block"):
                    self.contactsPage.click_contacts_tab()
                    time.sleep(1)
                    self.contactsPage.block_contact(UserB_name)
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_02)
            status_report_update_to_xls(sheet_name, status_tc_02, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_04 - User A send a offline message to User B, "
                        "Then User B login to clariti and verify User A DC message")
    def test_dc_04(self):
        generated_string = random_string(5)
        dc_message = "Tc_04_Offline_Message - " + generated_string
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_04"
        sheet_name = "Direct Chat"
        status_tc_04 = None
        status_dict = {
            "TC_04": status_tc_04
        }
        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                time.sleep(1)
            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_04 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("Login to clariti User B"):
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received message along with New message strip"):
                Check2 = self.directChatPage1.verify_last_dc_message(dc_message)
                if Check2:
                    status_tc_04 = True
                    status_dict["TC_04"] = status_tc_04
                elif not Check2:
                    pytest.fail("TC_04 - " + dc_message + " , This DC message is not available")
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_04)
            status_report_update_to_xls(sheet_name, status_tc_04, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_05 - User A send a online message to User B, Then User B verify User A DC message")
    def test_dc_05(self):
        generated_string = random_string(5)
        dc_message = "Tc_05_Online_Message - " + generated_string
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_05"
        sheet_name = "Direct Chat"
        status_tc_05 = None
        status_dict = {
            "TC_05": status_tc_05
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_05 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received message along with New message strip"):
                Check2 = self.directChatPage1.verify_last_dc_message(dc_message)
                if Check2:
                    status_tc_05 = True
                    status_dict["TC_05"] = status_tc_05
                elif not Check2:
                    pytest.fail("TC_05 - " + dc_message + " , This DC message is not available")
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_05)
            status_report_update_to_xls(sheet_name, status_tc_05, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_06 - User A send a file to User B, Then User B verify User A DC file")
    def test_dc_06(self):
        FileName = "S_image.jpg"
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_06"
        sheet_name = "Direct Chat"
        status_tc_06 = None
        status_dict = {
            "TC_06": status_tc_06
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a File to user B"):
                self.directChatPage.click_attachment_icon_dc_file()
                upload_files("one", FileName, "")
                time.sleep(2)

            with allure.step("User A Verify the sent File present"):
                Check1 = self.directChatPage.verify_last_file_message(FileName)
                if not Check1:
                    pytest.fail("TC_06 - " + FileName + " , This DC File is not available")
                time.sleep(3)

            with allure.step("User B Verify File from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received File along with New message strip"):
                Check2 = self.directChatPage.verify_last_file_message(FileName)
                if Check2:
                    status_tc_06 = True
                    status_dict["TC_06"] = status_tc_06
                elif not Check2:
                    pytest.fail("TC_06 - " + FileName + " , This DC File is not available")
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_06)
            status_report_update_to_xls(sheet_name, status_tc_06, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_07 - User A send a file to User B, Then User A and user B verify file and open a file")
    def test_dc_07(self):
        FileName = "Akrotiri_town.jpg"
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_07"
        sheet_name = "Direct Chat"
        status_tc_07 = None
        status_dict = {
            "TC_07": status_tc_07
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a File to user B"):
                self.directChatPage.click_attachment_icon_dc_file()
                upload_files("one", FileName, "")
                time.sleep(2)

            with allure.step("User A Verify the sent File present"):
                Check1 = self.directChatPage.verify_last_file_message(FileName)
                if not Check1:
                    pytest.fail("TC_07 - " + FileName + " , This DC File is not available")
                time.sleep(3)

            with allure.step("User A View the file in Overlay"):
                self.directChatPage.click_dc_file(FileName)
                time.sleep(0.5)
                self.directChatPage.verify_file_viewer_overlay()
                time.sleep(1)
                self.directChatPage.close_file_overlay()

            with allure.step("User B Verify File from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received File along with New message strip"):
                Check1 = self.directChatPage.verify_last_file_message(FileName)
                if not Check1:
                    pytest.fail("TC_07 - " + FileName + " , This DC File is not available")
                # if Check1:
                #     status_tc_07= True
                #     status_dict["TC_07"] = status_tc_07
                # elif not Check1:
                #     pytest.fail("TC_07 - " + FileName + " , This DC File is not available")
                time.sleep(1)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B View the file in Overlay"):
                self.directChatPage1.click_dc_file(FileName)
                time.sleep(0.5)
                Check2 = self.directChatPage1.verify_file_viewer_overlay()
                if Check1 and Check2:
                    status_tc_07 = True
                    status_dict["TC_07"] = status_tc_07
                elif not Check2:
                    pytest.fail("TC_07 - " + FileName + " , This DC File is not available")
                time.sleep(1)
                self.directChatPage1.close_file_overlay()

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_07)
            status_report_update_to_xls(sheet_name, status_tc_07, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_08 - User A send a non-viewable file to User B, "
                        "Then User A and user B verify file and open a file and verify Download button")
    def test_dc_08(self):
        FileName = "ElementsManifest.xml"
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_08"
        sheet_name = "Direct Chat"
        status_tc_08 = None
        status_dict = {
            "TC_08": status_tc_08
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            self.contactsPage.click_contacts_tab()
            time.sleep(1)
            self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a File to user B"):
                self.directChatPage.click_attachment_icon_dc_file()
                upload_files("one", FileName, "")
                time.sleep(2)

            with allure.step("User A Verify the sent File present"):
                Check1 = self.directChatPage.verify_last_file_message(FileName)
                if not Check1:
                    pytest.fail("TC_08 - " + FileName + " , This DC File is not available")
                time.sleep(3)

            with allure.step("User A View the file in Overlay"):
                self.directChatPage.click_dc_file(FileName)
                time.sleep(0.5)
                self.directChatPage.verify_non_viewable_file()
                time.sleep(1)
                self.directChatPage.close_file_overlay()

            with allure.step("User B Verify File from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received File along with New message strip"):
                Check1 = self.directChatPage.verify_last_file_message(FileName)
                if not Check1:
                    pytest.fail("TC_08 - " + FileName + " , This DC File is not available")
                time.sleep(1)

            with allure.step("User B View the file in Overlay and Verify Download button exists!."):
                self.directChatPage1.click_dc_file(FileName)
                time.sleep(0.5)
                Check2 = self.directChatPage1.verify_non_viewable_file()
                if Check1 and Check2:
                    status_tc_08 = True
                    status_dict["TC_08"] = status_tc_08
                elif not Check2:
                    pytest.fail("TC_08 - " + FileName + " , Download Button is not visible fow Non-Viewable file")
                time.sleep(1)
                self.directChatPage1.close_file_overlay()

                with allure.step("Doing logout"):
                    self.homePage.click_logout()
                    self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_08)
            status_report_update_to_xls(sheet_name, status_tc_08, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_09 - User A send a message to User B and User B click reply icon "
        "and verify reply strip added in chat editor.\n"
        "TC_10 - User A send a message to User B and User B click reply icon and "
        "reply a message and verify reply strip in that message.")
    def test_dc_09_10(self):
        generated_string = random_string(5)
        dc_message = "Tc_09_10 - DC_Message - " + generated_string
        dc_message_reply = "Tc_10 - Reply_DC_Message - " + generated_string
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number9 = "TC_09"
        test_case_number10 = "TC_10"
        sheet_name = "Direct Chat"
        status_tc_09 = None
        status_tc_10 = None
        status_dict = {
            "TC_09": status_tc_09,
            "TC_10": status_tc_10
        }
        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_09, 10 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received message along with New message strip"):
                Check2 = self.directChatPage1.verify_last_dc_message(dc_message)
                if not Check2:
                    pytest.fail("TC_09, 10 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User B Reply to that message with Reference reply strip"):
                self.directChatPage1.click_reply_from_message(dc_message)
                time.sleep(0.5)
                self.directChatPage1.verify_reply_strip_chat_editor("message", dc_message)
                time.sleep(0.1)
                status_tc_09 = True
                self.directChatPage1.send_dc_message(dc_message_reply)
                time.sleep(2)
                Check3 = self.directChatPage.verify_reply_strip_message(dc_message_reply)
                if not Check3:
                    pytest.fail("TC_09, 10 - " + dc_message_reply + " , This DC message is not available")
                time.sleep(1)

            with allure.step("User A Verify the Received message with Reply strip"):
                Check4 = self.directChatPage.verify_reply_strip_message(dc_message_reply)
                if not Check4:
                    pytest.fail("TC_09, 10 - " + dc_message_reply + " , This DC message is not available")
                time.sleep(1)
                if Check2 and Check4:
                    status_tc_09 = True
                    status_tc_10 = True
                    status_dict["TC_09"] = status_tc_09
                    status_dict["TC_10"] = status_tc_10

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number9, status_tc_09)
            verify_status(test_case_number10, status_tc_10)
            status_report_update_to_xls(sheet_name, status_tc_09, test_case_number9)
            status_report_update_to_xls(sheet_name, status_tc_10, test_case_number10)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(
                    status is not None for status in status_dict.values()) else "partially pass" if any(
                    status is not None for status in status_dict.values()) else "fail"

                if overall_status == "fail" or overall_status == "partially pass":
                    error_message = f"Test case {overall_status}. "
                    if overall_status == "partially pass":
                        failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                        error_message += f"Failed test steps: {', '.join(failed_steps)}"
                    if overall_status == "fail":
                        failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                        error_message += f"Failed test steps: {', '.join(failed_steps)}"
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_11 - User A send a message to User B and User A forward the message to User C and verify "
        "User C verify message received with forward strip.")
    def test_dc_11(self):
        generated_string = random_string(5)
        dc_message = "Tc_11 - DC_Message - " + generated_string
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_name = "Triadqa11 Hey"
        UserC_email = "clarititest5@yandex.com"
        UserC_password = "Triad@#123"
        UserC_name = "ClaritTest5 Automation"
        test_case_number = "TC_11"
        sheet_name = "Direct Chat"
        status_tc_11 = None
        status_dict = {
            "TC_11": status_tc_11
        }
        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserC_email, UserC_password)
                time.sleep(1)
            with allure.step("User A Select User B contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_11 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User A Forward the message to User C"):
                self.directChatPage.click_forward_from_message(dc_message)
                time.sleep(0.5)
                self.directChatPage.click_forward_option()
                time.sleep(1)
                self.contactsPage.select_add_contact_from_overlay(UserC_name)
                time.sleep(2)

            with allure.step("User A Select User C contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserC_name)
                time.sleep(2)

            with allure.step("User A Verify the Sent message along with forward strip"):
                Check1 = self.directChatPage.verify_forward_strip(dc_message)

            with allure.step("User C Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User C Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User C Verify the Received message along with New message strip and forward strip"):
                Check2 = self.directChatPage1.verify_forward_strip(dc_message)
                if Check1 and Check2:
                    status_tc_11 = True
                    status_dict["TC_11"] = status_tc_11

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_11)
            status_report_update_to_xls(sheet_name, status_tc_11, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_12 - User A send a message to User B, Then Copy that message and send to user B again")
    def test_dc_12(self):
        generated_string = random_string(5)
        dc_message = "Tc_12_DC_Message" + generated_string
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_12"
        sheet_name = "Direct Chat"
        status_tc_12 = None
        status_dict = {
            "TC_12": status_tc_12
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)
            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_12 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User A copy the sent message and sent the copied message again"):
                Check2 = self.directChatPage.verify_copied_dc_message(dc_message, UserA_name, "sender")

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received message along with New message strip"):
                Check3 = self.directChatPage1.verify_copied_dc_message(dc_message, UserA_name, "receiver")
                if Check2 and Check3:
                    status_tc_12 = True
                    status_dict["TC_12"] = status_tc_12

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_12)
            status_report_update_to_xls(sheet_name, status_tc_12, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_13 - User A send a message to User B, User B verify User A DC message and again User A send another message, New Messages strip should updated from New message")
    def test_dc_13(self):
        generated_string = random_string(5)
        dc_message = "Tc_13_Message - " + generated_string
        dc_message1 = "Tc_13_Message_2nd_Message - " + generated_string
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_13"
        sheet_name = "Direct Chat"
        status_tc_13 = None
        status_dict = {
            "TC_13": status_tc_13
        }
        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message)
                if not Check1:
                    pytest.fail("TC_13 - " + dc_message + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(2)

            with allure.step("User B Verify the Received message along with New message strip"):
                Check2 = self.directChatPage1.verify_received_messages_with_new_messages_strip("one", dc_message)

            with allure.step("User A send another message to user B"):
                self.directChatPage.send_dc_message(dc_message1)
                time.sleep(1)

            with allure.step("User B Verify the Received message along with New Messages strip"):
                Check3 = self.directChatPage1.verify_received_messages_with_new_messages_strip("morethanone",
                                                                                               dc_message1)
                if Check2 and Check3:
                    status_tc_13 = True
                    status_dict["TC_13"] = status_tc_13

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_13)
            status_report_update_to_xls(sheet_name, status_tc_13, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_14 - User A send 15 messages to User B, User B verify User A DC messages as New messages strip "
        "appears and scroll to bottom icon appears and focused in new messages strip")
    def test_dc_14(self):
        generated_string = random_string(5)
        dc_message1 = "Tc_14_Message_1st_Message - " + generated_string
        dc_message2 = "Tc_14_Message_2nd_Message - " + random_string(5)
        dc_message3 = "Tc_14_Message_3rd_Message - " + random_string(5)
        dc_message4 = "Tc_14_Message_4th_Message - " + random_string(5)
        dc_message5 = "Tc_14_Message_5th_Message - " + random_string(5)
        dc_message6 = "Tc_14_Message_6th_Message - " + random_string(5)
        dc_message7 = "Tc_14_Message_7th_Message - " + random_string(5)
        dc_message8 = "Tc_14_Message_8th_Message - " + random_string(5)
        dc_message9 = "Tc_14_Message_9th_Message - " + random_string(5)
        dc_message10 = "Tc_14_Message_10th_Message - " + random_string(5)
        dc_message11 = "Tc_14_Message_11th_Message - " + random_string(5)
        dc_message12 = "Tc_14_Message_12th_Message - " + random_string(5)
        dc_message13 = "Tc_14_Message_13th_Message - " + random_string(5)
        dc_message14 = "Tc_14_Message_14th_Message - " + random_string(5)
        dc_message15 = "Tc_14_Message_15th_Message - " + random_string(5)

        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_14"
        sheet_name = "Direct Chat"
        status_tc_14 = None
        status_dict = {
            "TC_14": status_tc_14
        }
        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("Select contact"):
                self.contactsPage.click_contacts_tab()
                time.sleep(1)
                self.contactsPage.click_contact_using_scroll(UserB_name)

            with allure.step("User A send a message to user B"):
                self.directChatPage.send_dc_message(dc_message1)
                self.directChatPage.send_dc_message(dc_message2)
                self.directChatPage.send_dc_message(dc_message3)
                self.directChatPage.send_dc_message(dc_message4)
                self.directChatPage.send_dc_message(dc_message5)
                self.directChatPage.send_dc_message(dc_message6)
                self.directChatPage.send_dc_message(dc_message7)
                self.directChatPage.send_dc_message(dc_message8)
                self.directChatPage.send_dc_message(dc_message9)
                self.directChatPage.send_dc_message(dc_message10)
                self.directChatPage.send_dc_message(dc_message11)
                self.directChatPage.send_dc_message(dc_message12)
                self.directChatPage.send_dc_message(dc_message13)
                self.directChatPage.send_dc_message(dc_message14)
                self.directChatPage.send_dc_message(dc_message15)

            with allure.step("User A Verify the sent message present"):
                Check1 = self.directChatPage.verify_last_dc_message(dc_message15)
                if not Check1:
                    pytest.fail("TC_14 - " + dc_message15 + " , This DC message is not available")
                time.sleep(3)

            with allure.step("User B Verify message from user A with green indicator icon"):
                self.directChatPage1.verify_green_indicator_dc(UserA_name)

            with allure.step("User B Select User A contact"):
                self.directChatPage1.click_on_dc_contact(UserA_name)
                time.sleep(3)

            with allure.step("User B Verify the Received messages along with New Messages strip and focused with 1st "
                             "message and scroll to bottom icon"):
                Check3 = self.directChatPage1.verify_received_messages_with_new_messages_strip("morethanone",
                                                                                               dc_message1)
                Check4 = self.directChatPage1.verify_scroll_to_bottom_icon()
                NewMessageStrip = self.directChatPage1.new_messages_strip_return
                scrollBottom = self.directChatPage1.scroll_to_bottom_return
                if Check3 and Check4 and NewMessageStrip and scrollBottom:
                    print("New messages strip focused with 1st message and Scroll to Bottom icon appears.")
                    self.directChatPage1.check_scroll_to_bottom_icon()
                    status_tc_14 = True
                    status_dict["TC_14"] = status_tc_14

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            verify_status(test_case_number, status_tc_14)
            status_report_update_to_xls(sheet_name, status_tc_14, test_case_number)
            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)


class TestDemo(BaseTest1):
    def test_dc_001(self):
        UserA_email = "triadred50@rediffmail.com"
        UserA_password = "Welcome123$"
        UserA_name = "triad red50"
        UserB_email = "triadred51@rediffmail.com"
        UserB_password = "Welcome123$"
        UserB_name = "triad red51"
        test_case_number = "TC_01"
        sheet_name = "Direct Chat"
        status_tc_01 = None
        dc_message = "Message"

        with allure.step("Login to clariti:"):
            self.loginPage.clariti_sign_in(UserA_email, UserA_password)
        with allure.step("Select contacts tab"):
            self.contactsPage.click_contacts_tab()
            time.sleep(1)
        with allure.step("clicking contact"):
            self.contactsPage.click_contact_using_scroll(UserB_name)
        with allure.step("search Messages"):
            self.directChatPage.click_search_text_box()
            time.sleep(1)
            self.directChatPage.verify_search_text_box_focused()
            self.directChatPage.search_messages(dc_message)
            time.sleep(5)
        with allure.step("Click Logout"):
            self.homePage.click_logout()
