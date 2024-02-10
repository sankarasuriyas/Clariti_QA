import time
import allure
import pytest
from allure_commons.types import AttachmentType
from Clariti.pages.base_page import random_string, close_file_explorer, upload_files, \
    screenshot_and_attach_report_pyautogui
from Clariti.testscripts.base_test import BaseTest, BaseTest3, BaseTest1
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.utils import verify_status, status_report_update_to_xls


class TestPushMail2Users(BaseTest):
    logger = LogGen.loggen()

    # @pytest.mark.pushMail1
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_01 - User A send a Mail to User B, User B side validate count updated and "
        "select mails tab and select that received mail\n"
        "TC_02 - User A send a Mail to User B, User B side Reply to that mail and verify reply mail received in "
        "User A side and its merged or not\n"
        "TC_06 - User A send a Mail to User B, User B side validate count updated and select mails tab and "
        "select that received mail\n"
        "TC_07 - User A send a Mail to User B, User B delete the mail item and restore the mail and verify "
        "count updated in mails tab,.\n"
        "TC_08 - User A send a Mail to User B, User A resend the mail to user B, verify User B side both mails "
        "appears and count updated,."
    )
    def test_Push_TC_01_02_06_07_08(self):

        # global status_tc_01, status_tc_02, status_tc_06, status_tc_07, status_tc_08
        generated_string1 = random_string(5)
        generated_string6 = random_string(5)
        generated_string7 = random_string(5)
        generated_string2 = random_string(5)
        generated_string8 = random_string(5)

        subject_TC1 = "TC_01 Push - " + generated_string1
        subject_TC2 = "TC_02 Push - " + generated_string2
        subject_TC6 = "TC_06 Push - " + generated_string6
        subject_TC7 = "TC_07 Push - " + generated_string7
        subject_TC8 = "TC_08 Push - " + generated_string8

        message = "Hi, This is automated test mail for mail receive case"
        reply_message = "Hi, this is reply mail"
        login_email = "triadautomation1@aol.com"
        login_password = "Welcome123$#@!"
        UserA_name = "Triadqa1aol Automation"
        UserB_email = "clarititest4@yandex.com"
        UserB_configuredEmail = "triadautomationqa4@outlook.com"
        UserB_password = "Triad@#123"
        UserB_name = "Clariti test4"
        test_case_number1 = "TC_01"
        test_case_number2 = "TC_02"
        test_case_number6 = "TC_06"
        test_case_number7 = "TC_07"
        test_case_number8 = "TC_08"
        sheet_name = "Push Mails"
        local_status_tc_01 = None
        local_status_tc_06 = None
        local_status_tc_07 = None
        local_status_tc_02 = None
        local_status_tc_08 = None

        status_dict = {
            "TC_01": local_status_tc_01,
            "TC_02": local_status_tc_02,
            "TC_06": local_status_tc_06,
            "TC_07": local_status_tc_07,
            "TC_08": local_status_tc_08,
        }
        self.logger.info("* Mail test case TC_01 started *")

        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User A side"):
                # User A side old count
                old_count_A = self.homePage.unread_count("mail")
                old_count_int_A = int(old_count_A)
                allure.attach("User A Old Count in Mails tab: " + old_count_A, name="UserA_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                print("User A Old Count in Mails tab: " + old_count_A)
                self.logger.info("User A Old Count in Mails tab: " + old_count_A)

            with allure.step("Checking count after logged in User B side"):
                # User B side old count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User B Old Count in Mails tab: " + old_count_B)
                print("User B Old Count in Mails tab: " + old_count_B)

            # TC 1
            with allure.step("TC_1 - User A send the Mail to User B"):
                print("Running Mail Push TC 01")
                self.mailDraftPage.mail_send(subject_TC1, "TO", UserB_configuredEmail, "tab", message)

                with allure.step("Verify Mail sending in-progress in User A side"):
                    allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage.mail_send_validation(test_case_number1)
                time.sleep(1)

            # TC 2
            with allure.step("TC_2 - User A send the Mail to User B"):
                print("Running Mail Push TC 02")
                self.mailDraftPage.mail_send(subject_TC2, "TO", UserB_configuredEmail, "tab", message)

                with allure.step("Verify Mail sending in-progress in User A side"):
                    allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage.mail_send_validation(test_case_number2)
                time.sleep(1)

            # TC 6
            with allure.step("TC_6 - User A send the Mail to User B"):
                print("Running Mail Push TC 06")
                self.mailDraftPage.mail_send(subject_TC6, "TO", UserB_configuredEmail, "tab", message)

                with allure.step("Verify Mail sending in-progress in User A side"):
                    allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage.mail_send_validation(test_case_number6)
                time.sleep(1)

            # TC 7
            with allure.step("TC_7 - User A send the Mail to User B"):
                print("Running Mail Push TC 07")
                self.mailDraftPage.mail_send(subject_TC7, "TO", UserB_configuredEmail, "tab", message)

                with allure.step("Verify Mail sending in-progress in User A side"):
                    allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage.mail_send_validation(test_case_number7)
                time.sleep(1)

            # TC 8
            with allure.step("TC_8 - User A send the Mail to User B"):
                print("Running Mail Push TC 08")
                self.mailDraftPage.mail_send(subject_TC8, "TO", UserB_configuredEmail, "tab", message)
                with allure.step("Verify Mail sending in-progress in User A side"):
                    allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage.mail_send_validation(test_case_number8)
                    time.sleep(1)
                with allure.step("User A Resend the Mail to User B"):
                    self.mailPage.click_mails_tab()
                    time.sleep(1)
                    self.mailPage.get_mail_item_and_verification(subject_TC8, UserB_name, "A", test_case_number8)
                    time.sleep(1)
                    self.mailPage.click_resend()
                    time.sleep(1)
                    self.mailDraftPage.click_send_button()
                    with allure.step("TC_8 - Verify Resend Mail sending in-progress in User A side"):
                        allure.attach(self.driver.get_screenshot_as_png(), name="Mail_Re-sending_inprogress",
                                      attachment_type=AttachmentType.PNG)
                        self.mailPage.wait_until_mail_send_overlay()
                    time.sleep(1)

            with allure.step("TC_01 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Push TC 01")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.goback_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC1, UserB_name, "A", test_case_number1)
                self.mailPage.goback_tab()

            with allure.step("TC_02 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Push TC 02")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                time.sleep(0.5)
                self.mailPage.get_mail_item_and_verification(subject_TC2, UserB_name, "A", test_case_number2)
                self.mailPage.goback_tab()

            with allure.step("TC_06 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Push TC 06")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                # self.mailPage.click_mails_tab()
                time.sleep(0.5)
                self.mailPage.get_mail_item_and_verification(subject_TC6, UserB_name, "A", test_case_number6)
                self.mailPage.goback_tab()

            with allure.step("TC_07 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Push TC 07")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                #   self.mailPage.click_mails_tab()
                time.sleep(0.5)
                self.mailPage.get_mail_item_and_verification(subject_TC7, UserB_name, "A", test_case_number7)
                self.mailPage.goback_tab()

            with allure.step("TC_08 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Push TC 08")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                time.sleep(0.5)
                self.mailPage.get_mail_item_and_verification(subject_TC8, UserB_name, "A", test_case_number8)
                self.mailPage.goback_tab()

            with allure.step("Checking count in User B side after User A sent a Mail"):
                # User B side new count
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                allure.attach("User B New Count in Mails tab: " + new_count_B, name="UserB_New_Count",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User B New Count in Mails tab: " + new_count_B)
                print("User B New Count in Mails tab: " + new_count_B)

            with allure.step("Verify count updated in User B side and Mail received in Mails tab"):
                try:
                    if new_count_int_B > old_count_int_B + 5:
                        self.logger.info("* More than 5 new Mail Received *")
                        print("More than 5 new Mail Received")
                        self.mailPage1.click_mails_tab()
                    else:
                        self.logger.info("* Mail count is not updated and count failed *")
                        assert False
                except AssertionError as e:
                    print("Count not updated")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_01 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("TC_01 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Push TC 01")
                self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B", test_case_number1)
                self.mailPage1.goback_tab()
                time.sleep(1)
                local_status_tc_01 = True
                status_dict["TC_01"] = local_status_tc_01

            with allure.step("TC_02 _ Verify Mail Received in User B side and Reply to that Mail"):
                print("Running Mail Push TC 02")
                with allure.step("Verify Mail Item"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC2, UserA_name, "B", test_case_number2)
                with allure.step("Reply to that Received Mail"):
                    self.mailPage1.click_reply_icon_1_user()
                    time.sleep(1)
                    self.mailDraftPage1.body_content_message("overlay", reply_message)
                    self.mailDraftPage1.click_send_button()
                    with allure.step("Verify Mail reply in-progress in User B side"):
                        allure.attach(self.driver1.get_screenshot_as_png(), name="Mail_reply_sending_inprogress",
                                      attachment_type=AttachmentType.PNG)

                        self.mailPage1.wait_until_mail_send_overlay()
                        time.sleep(1)

                with allure.step("Verify Reply sent Mail item present in Mails tab in User B side"):
                    # self.mailPage1.click_mails_tab()
                    time.sleep(1)
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.get_mail_item_and_verification("Re: " + subject_TC2, UserA_name, "B",
                                                                  test_case_number2)

                with allure.step("Verify Mail item threaded in User B side"):
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.verify_mail_threaded(subject_TC2, UserA_name, "B", test_case_number2)
                    time.sleep(1)
                    self.homePage1.click_trash_tab()
                    self.mailPage1.click_mails_tab()

                with allure.step("Checking count in User A side after User B sent a Reply Mail"):

                    # User A side Verification
                    time.sleep(1)
                    new_count_A = self.homePage.unread_count("mail")
                    new_count_int_A = int(new_count_A)
                    allure.attach("User A New Count in Mails tab: " + new_count_A, name="UserA_New_Count",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("New Count in User A Mails tab: " + new_count_A)

                with allure.step("Verify count updated in User A side and Mail received in Mails tab"):
                    try:
                        if new_count_int_A > old_count_int_A:
                            print("Count updated")
                            time.sleep(1)
                            self.mailPage.get_mail_item_and_verification("Re: " + subject_TC2, UserB_name, "A",
                                                                         test_case_number2)
                        else:
                            self.logger.info("* Mail count is not updated and count failed *")
                            assert False
                    except AssertionError as e:
                        print("Count not updated")
                        allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                        pytest.fail("TC_02 Assertion failed: Mail tab Count not updated {}".format(e))

                with allure.step("Verify Mail item threaded in User A side"):
                    time.sleep(1)
                    self.mailPage.goback_tab()
                    time.sleep(1)
                    self.mailPage.verify_mail_threaded("Re: " + subject_TC2, UserB_name, "A", test_case_number2)
                    self.homePage.click_trash_tab()
                    self.mailPage.click_mails_tab()
                    local_status_tc_02 = True
                    status_dict["TC_02"] = local_status_tc_02

            with allure.step("TC_06 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Push TC 06")
                with allure.step("Delete that Received Mail"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC6, UserA_name, "B", test_case_number6)
                    self.mailPage1.click_delete_icon()
                    time.sleep(1)
                    # click trash tab
                    self.homePage1.click_trash_tab()
                    time.sleep(1)

                    # check mail in deleted tab
                    self.mailPage1.get_mail_item_and_verification(subject_TC6, UserA_name, "B", test_case_number6)
                    self.mailPage1.goback_tab()
                    self.mailPage1.click_mails_tab()
                    time.sleep(1)
                local_status_tc_06 = True
                status_dict["TC_06"] = local_status_tc_06

            with allure.step("TC_07 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Push TC 07")
                with allure.step("Delete that Received Mail"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC7, UserA_name, "B", test_case_number7)
                    self.mailPage1.click_delete_icon()
                    time.sleep(1)
                    # User B side new count
                    new_count_after_delete_B = self.homePage1.unread_count("mail")
                    new_count_after_delete_int_B = int(new_count_after_delete_B)
                    allure.attach("User B New Count in Mails tab: " + new_count_after_delete_B,
                                  name="User B new count after Delete a mail ",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("User B New Count in Mails tab after Mail deleted: " + new_count_after_delete_B)
                with allure.step("Verify Deleted mail in Trash tab"):
                    # click trash tab
                    self.homePage1.click_trash_tab()
                    time.sleep(1)
                    # check mail in deleted tab
                    self.mailPage1.get_mail_item_and_verification(subject_TC7, UserA_name, "B", test_case_number7)

                with allure.step("Restore the Deleted mail from Trash tab"):
                    self.mailPage1.click_restore_un_spam_icon()
                    self.mailPage1.wait_until_table_explore()
                    time.sleep(0.5)
                    with allure.step("Checking count in User B side after Restore the deleted Mail"):
                        # User B side new count after restore mail
                        new_count_after_restore_B = self.homePage1.unread_count("mail")
                        new_count_after_restore_int_B = int(new_count_after_restore_B)
                        allure.attach("User B New Count in Mails tab: " + new_count_after_restore_B,
                                      name="User B new count after restore the Deleted mail ",
                                      attachment_type=allure.attachment_type.TEXT)
                        self.logger.info(
                            "User B New Count in Mails tab after Mail restored: " + new_count_after_restore_B)
                    try:
                        if new_count_after_restore_int_B > new_count_after_delete_int_B:
                            self.mailPage1.click_mails_tab()
                            time.sleep(1)
                            self.mailPage1.get_mail_item_and_verification(
                                subject_TC7, UserA_name, "B", test_case_number7)
                            self.mailPage1.goback_tab()
                            local_status_tc_07 = True
                            status_dict["TC_07"] = local_status_tc_07

                        else:
                            self.logger.info("* Mail count is not updated and count failed *")
                            assert False
                    except AssertionError as e:
                        print("Item not present")
                        allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                        pytest.fail("TC_07 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("TC_08 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Push TC 08")

                with allure.step("Verify Both Mail Mail item Received in User B side"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC8, UserA_name, "B", test_case_number8)

                with allure.step("Verify Mail item threaded in User B side"):
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.verify_mail_threaded(subject_TC8, UserA_name, "B", test_case_number8)
                    local_status_tc_08 = True
                    status_dict["TC_08"] = local_status_tc_08

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            with allure.step("Each Test Case Status"):
                verify_status(test_case_number1, local_status_tc_01)
                verify_status(test_case_number2, local_status_tc_02)
                verify_status(test_case_number6, local_status_tc_06)
                verify_status(test_case_number7, local_status_tc_07)
                verify_status(test_case_number8, local_status_tc_08)
                status_report_update_to_xls(sheet_name, local_status_tc_01, test_case_number1)
                status_report_update_to_xls(sheet_name, local_status_tc_02, test_case_number2)
                status_report_update_to_xls(sheet_name, local_status_tc_06, test_case_number6)
                status_report_update_to_xls(sheet_name, local_status_tc_07, test_case_number7)
                status_report_update_to_xls(sheet_name, local_status_tc_08, test_case_number8)

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

        self.logger.info("* Mail test case TC_01,TC_02,TC_06,TC_07,TC_08 Ended *")


class TestPushMail3Users(BaseTest3):
    logger = LogGen.loggen()

    # @pytest.mark.pushMail1
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("User A send a Mail to User B and user C, Verify from both users mail received or not and "
                        "count updated or not,.")
    def test_TC_03(self):

        generated_string = random_string(5)
        subject = "TC_03 " + generated_string
        message = "Hi, This is automated test mail for 2 users"
        login_email = "triadautomation1@aol.com"
        login_password = "Welcome123$#@!"
        UserA_name = "Triadqa1aol Automation"
        # UserB_email = "triadautomationqa1@outlook.com"
        # UserB_password = "Welcome123$"
        # UserC_email = "triadqa2automation@outlook.com"
        # UserC_password = "Welcome123$"
        UserB_email = "clarititest4@yandex.com"
        UserB_configuredEmail = "triadautomationqa4@outlook.com"
        UserB_password = "Triad@#123"
        # UserB_name = "Clariti test4"
        # UserC_email = "triadqa4@yahoo.com"
        # UserC_password = "Welcome123$#@!~"
        # UserC_name = "Triadqa4yahoo Automation"
        UserC_email = "clarititriad3@yandex.com"
        UserC_configuredEmail = "triadqa2automation@outlook.com"
        UserC_password = "Welcome123$#@!"
        # UserC_name = "ClaritTriad3 Automation"
        test_case_number = "TC_03"
        sheet_name = "Push Mails"

        self.logger.info("* Mail test case TC_03 started *")
        local_status = None
        status_dict = {
            "TC_03": local_status
        }
        try:
            with allure.step("Login to clariti User A, User B and User C"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                self.loginPage2.clariti_sign_in(UserC_email, UserC_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User B side"):
                print("Running Mail Push TC 03")
                # User B side verification - getting unread count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User B Old Count in Mails tab: " + old_count_B)

            with allure.step("Checking count after logged in User C side"):
                # User C side verification - getting unread count
                old_count_C = self.homePage2.unread_count("mail")
                old_count_int_C = int(old_count_C)
                allure.attach("User C Old Count in Mails tab: " + old_count_C, name="UserC_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User C Old Count in Mails tab: " + old_count_C)

            # User A side case
            self.mailDraftPage.mail_send_2_users(subject, "TO", UserB_configuredEmail, UserC_configuredEmail, "tab",
                                                 message)

            with allure.step("Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number)

            time.sleep(1)
            with allure.step("Checking count in User B side after User A sent a Mail"):
                # User B side uses driver1
                time.sleep(2)
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                allure.attach("User B New Count in Mails tab: " + new_count_B, name="UserB_New_Count",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("New Count in User B Mails tab: " + new_count_B)

            # User B side Verification
            with allure.step("Verify count updated in User B side and Mail received in Mails tab"):
                try:
                    if new_count_int_B > old_count_int_B:
                        print("Count updated")
                        self.mailPage1.click_mails_tab()
                        time.sleep(1)
                        self.mailPage1.get_mail_item_and_verification(subject, UserA_name, "B", test_case_number)
                    else:
                        self.logger.info("* Mail count is not updated and count failed *")
                        assert False
                except AssertionError as e:
                    print("Item not present")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_02 Assertion failed: Mail tab Count not updated {}".format(e))

            # User C side Verification
            with allure.step("Checking count in User C side after User A sent a Mail"):
                time.sleep(2)
                new_count_C = self.homePage2.unread_count("mail")
                new_count_int_C = int(new_count_C)
                allure.attach("User C New Count in Mails tab: " + new_count_C, name="UserC_New_Count",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("New Count in User C Mails tab: " + new_count_C)

            with allure.step("Verify count updated in User C side and Mail received in Mails tab"):
                try:
                    if new_count_int_C > old_count_int_C:
                        print("Count updated")
                        self.mailPage2.click_mails_tab()
                        time.sleep(1)
                        self.mailPage2.get_mail_item_and_verification(subject, UserA_name, "C", test_case_number)
                        local_status = True
                        status_dict["TC_03"] = local_status

                    else:
                        self.logger.info("* Mail count is not updated and count failed *")
                        assert False
                except AssertionError as e:
                    print("Item not present")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_02 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()
                self.homePage2.click_logout()

        finally:
            with allure.step("Test Case Status"):
                verify_status(test_case_number, local_status)
                status_report_update_to_xls(sheet_name, local_status, test_case_number)

            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

        self.logger.info("* Mail test case TC_03 Ended *")

    # @pytest.mark.pushMail
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("User A send a Mail to User B and user C, User B Reply ALl to that mail and verify from both "
                        "sides mail received and becomes threaded,.")
    def test_TC_04(self):
        # global status

        generated_string = random_string(5)
        subject = "TC_04 " + generated_string
        message = "Hi, This is automated test mail for reply all case"
        reply_message = "This is reply message,.."
        login_email = "triadautomation1@aol.com"
        login_password = "Welcome123$#@!"
        UserA_name = "Triadqa1aol Automation"
        # UserB_name = "Triadqa1 outlookAutomation"
        # UserB_email = "triadautomationqa1@outlook.com"
        # UserB_password = "Welcome123$"
        # UserC_email = "triadqa2automation@outlook.com"
        # UserC_password = "Welcome123$"
        UserB_email = "clarititest4@yandex.com"
        UserB_configuredEmail = "triadautomationqa4@outlook.com"
        UserB_password = "Triad@#123"
        UserB_name = "Clariti test4"
        # UserC_email = "triadqa4@yahoo.com"
        # UserC_password = "Welcome123$#@!~"
        # UserC_name = "Triadqa4yahoo Automation"
        UserC_email = "clarititriad3@yandex.com"
        UserC_configuredEmail = "triadqa2automation@outlook.com"
        UserC_password = "Welcome123$#@!"
        # UserC_name = "ClaritTriad3 Automation"
        test_case_number = "TC_04"
        sheet_name = "Push Mails"

        self.logger.info("* Mail test case TC_04 started *")
        local_status = None
        status_dict = {
            "TC_04": local_status
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                self.loginPage2.clariti_sign_in(UserC_email, UserC_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User A side"):
                print("Running Mail Push TC 04")
                # User A side verification - getting unread count
                old_count_A = self.homePage.unread_count("mail")
                old_count_int_A = int(old_count_A)
                allure.attach("User A Old Count in Mails tab: " + old_count_A, name="UserA_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User A Old Count in Mails tab: " + old_count_A)

            with allure.step("Checking count after logged in User B side"):
                # User B side verification - getting unread count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User B Old Count in Mails tab: " + old_count_B)

            with allure.step("Checking count after logged in User C side"):
                # User C side verification - getting unread count
                old_count_C = self.homePage2.unread_count("mail")
                old_count_int_C = int(old_count_C)
                allure.attach("User C Old Count in Mails tab: " + old_count_C, name="UserC_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User C Old Count in Mails tab: " + old_count_C)

            # User A side case
            self.mailDraftPage.mail_send_2_users(subject, "TO", UserB_configuredEmail, UserC_configuredEmail, "tab",
                                                 message)

            with allure.step("Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number)

            time.sleep(1)
            with allure.step("Checking count in User B side after User A sent a Mail"):
                # User B side uses driver1
                time.sleep(2)
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                allure.attach("User B New Count in Mails tab: " + new_count_B, name="UserB_New_Count",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("New Count in User B Mails tab: " + new_count_B)

            # User B side Verification
            with allure.step("Verify count updated in User B side and Mail received in Mails tab"):
                try:
                    if new_count_int_B > old_count_int_B:
                        print("Count updated")
                        self.mailPage1.click_mails_tab()
                        time.sleep(1)
                        self.mailPage1.get_mail_item_and_verification(subject, UserA_name, "B", test_case_number)
                    else:
                        self.logger.info("* Mail count is not updated and count failed *")
                        assert False
                except AssertionError as e:
                    print("Item not present")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_02 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Reply All to that Received Mail"):

                time.sleep(1)
                self.mailPage1.click_reply_all_icon()
                time.sleep(1)
                self.mailDraftPage1.body_content_message("overlay", reply_message)
                self.mailDraftPage1.click_send_button()

                with allure.step("Verify Mail reply all in-progress in User B side"):
                    allure.attach(self.driver1.get_screenshot_as_png(), name="Mail_reply_all_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)

                    self.mailPage1.wait_until_mail_send_overlay()

            with allure.step("Verify Reply All Sent Mail item present in Mails tab from User B side"):

                # self.mailPage1.click_mails_tab()
                # time.sleep(1)
                self.mailPage1.goback_tab()
                time.sleep(1)
                self.mailPage1.get_mail_item_and_verification("Re: " + subject, UserA_name, "B", test_case_number)

            with allure.step("Verify Mail item threaded in User B side"):

                self.mailPage1.goback_tab()
                time.sleep(1)
                self.mailPage1.verify_mail_threaded(subject, UserA_name, "B", test_case_number)

            # User A side Verification
            with allure.step("Checking count in User A side after User B sent a Reply All Mail"):
                time.sleep(1)
                new_count_A = self.homePage.unread_count("mail")
                new_count_int_A = int(new_count_A)
                allure.attach("User A New Count in Mails tab: " + new_count_A,
                              name="User A new count after user B reply a mail",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("New Count in User A Mails tab: " + new_count_A)

            with allure.step("Verify count updated in User A side and Mail received in Mails tab"):
                try:
                    if new_count_int_A > old_count_int_A:
                        print("Count updated")
                        self.mailPage.click_mails_tab()
                        time.sleep(1)
                        self.mailPage.get_mail_item_and_verification("Re: " + subject, UserB_name, "A",
                                                                     test_case_number)
                    else:
                        self.logger.info("User A New Count in Mails tab: " + new_count_A)
                        assert False
                except AssertionError as e:
                    print("Count not updated")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_04 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Verify Mail item threaded in User A side"):
                time.sleep(1)
                self.mailPage.goback_tab()
                time.sleep(1)
                self.mailPage.verify_mail_threaded("Re: " + subject, UserB_name, "A", test_case_number)

            # User C side Verification
            with allure.step("Checking count in User C side after User B sent a Reply All Mail"):
                time.sleep(1)
                new_count_c = self.homePage2.unread_count("mail")
                new_count_int_C = int(new_count_c)
                allure.attach("User C New Count in Mails tab: " + new_count_c,
                              name="User C new count after user B reply a mail",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("New Count in User C Mails tab: " + new_count_c)

            with allure.step("Verify count updated in User C side and Mail received in Mails tab"):
                try:
                    if new_count_int_C > old_count_int_C:
                        print("Count updated")
                        self.mailPage2.click_mails_tab()
                        time.sleep(1)
                        self.mailPage2.get_mail_item_and_verification("Re: " + subject, UserB_name, "C",
                                                                      test_case_number)
                    else:
                        self.logger.info("User C New Count in Mails tab: " + new_count_c)
                        assert False
                except AssertionError as e:
                    print("Count not updated")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_04 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Verify Mail item threaded in User C side"):
                time.sleep(1)
                self.mailPage2.goback_tab()
                time.sleep(1)
                self.mailPage2.verify_mail_threaded(subject, UserA_name, "C", test_case_number)
                local_status = True
                status_dict["TC_04"] = local_status

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()
                self.homePage2.click_logout()

        finally:
            with allure.step("Test Case Status"):
                verify_status(test_case_number, local_status)
                status_report_update_to_xls(sheet_name, local_status, test_case_number)

            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

        self.logger.info("* Mail test case TC_04 Ended *")

    # @pytest.mark.pushMail1
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("User A send a Mail to User B, User B forward to User C and verify that mail received in user "
                        "C side and becomes threaded in user B side,.")
    def test_TC_05(self):
        # global status

        generated_string = random_string(5)
        subject = "TC_05 " + generated_string
        message = "Hi, This is automated test mail for forward case"
        reply_message = "This is reply message for forward case,.."
        login_email = "triadautomation1@aol.com"
        login_password = "Welcome123$#@!"
        UserA_name = "Triadqa1aol Automation"
        # UserB_name = "Triadqa1 outlookAutomation"
        # UserC_name = "Triadqa2 out Automation"
        # UserB_email = "triadautomationqa1@outlook.com"
        # UserB_password = "Welcome123$"
        # UserC_email = "triadqa2automation@outlook.com"
        # UserC_password = "Welcome123$"
        UserB_email = "clarititest4@yandex.com"
        UserB_configuredEmail = "triadautomationqa4@outlook.com"
        UserB_password = "Triad@#123"
        UserB_name = "Clariti test4"
        # UserC_email = "triadqa4@yahoo.com"
        # UserC_password = "Welcome123$#@!~"
        # UserC_name = "Triadqa4yahoo Automation"
        UserC_email = "clarititriad3@yandex.com"
        UserC_configuredEmail = "triadqa2automation@outlook.com"
        UserC_password = "Welcome123$#@!"
        UserC_name = "ClaritTriad3 Automation"
        test_case_number = "TC_05"
        sheet_name = "Push Mails"

        self.logger.info("* Mail test case TC_05 started *")
        local_status = None
        status_dict = {
            "TC_05": local_status
        }
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                self.loginPage2.clariti_sign_in(UserC_email, UserC_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User A side"):
                print("Running Mail Push TC 05")
                # User A side verification - getting unread count
                old_count_A = self.homePage.unread_count("mail")
                old_count_int_A = int(old_count_A)
                allure.attach("User A Old Count in Mails tab: " + old_count_A, name="UserA_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User A Old Count in Mails tab: " + old_count_A)

            with allure.step("Checking count after logged in User B side"):
                # User B side verification - getting unread count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User B Old Count in Mails tab: " + old_count_B)

            with allure.step("Checking count after logged in User C side"):
                # User C side verification - getting unread count
                old_count_C = self.homePage2.unread_count("mail")
                old_count_int_C = int(old_count_C)
                allure.attach("User C Old Count in Mails tab: " + old_count_C, name="UserC_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User C Old Count in Mails tab: " + old_count_C)

            # User A side case
            self.mailDraftPage.mail_send_2_users(subject, "TO", UserB_configuredEmail, UserC_configuredEmail, "tab",
                                                 message)

            with allure.step("Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number)

            time.sleep(1)
            with allure.step("Checking count in User B side after User A sent a Mail"):
                time.sleep(2)
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                allure.attach("User B New Count in Mails tab: " + new_count_B, name="UserB_New_Count",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("New Count in User B Mails tab: " + new_count_B)

            # User B side Verification
            with allure.step("Verify count updated in User B side and Mail received in Mails tab"):
                try:
                    if new_count_int_B > old_count_int_B:
                        print("Count updated")
                        self.mailPage1.click_mails_tab()
                        time.sleep(1)
                        self.mailPage1.get_mail_item_and_verification(subject, UserA_name, "B", test_case_number)
                    else:
                        self.logger.info("* Mail count is not updated and count failed *")
                        assert False
                except AssertionError as e:
                    print("Item not present")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_02 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Forward to that Received Mail"):

                time.sleep(1)
                self.mailPage1.click_forward_icon_received()
                time.sleep(1)
                self.mailDraftPage1.enter_to_address(UserC_configuredEmail)

                self.mailDraftPage1.body_content_message("overlay", reply_message)
                self.mailDraftPage1.click_send_button()

                with allure.step("Verify Mail Forward in-progress in User B side"):
                    allure.attach(self.driver1.get_screenshot_as_png(), name="Mail_Forward_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)

                    self.mailPage1.wait_until_mail_send_overlay()
                    with allure.step("Verify Forward Sent Mail item present in Mails tab from User B side"):
                        # self.mailPage1.click_mails_tab()
                        # time.sleep(1)
                        self.mailPage1.goback_tab()
                        time.sleep(1)
                        self.mailPage1.get_mail_item_and_verification("Fw: " + subject, UserC_name, "B",
                                                                      test_case_number)

            time.sleep(1)

            with allure.step("Verify Mail item threaded in User B side"):
                self.mailPage1.goback_tab()
                time.sleep(1)
                self.mailPage1.verify_mail_threaded(subject, UserA_name, "B", test_case_number)

            with allure.step("Checking count in User C side after User B forward a Mail"):
                # User C side uses driver2
                time.sleep(1)
                new_count_C = self.homePage2.unread_count("mail")
                new_count_int_C = int(new_count_C)
                allure.attach("User C New Count in Mails tab: " + new_count_C,
                              name="User C new count after user B forward a mail ",
                              attachment_type=allure.attachment_type.TEXT)
            with allure.step("Verify count updated in User C side and Mail received in Mails tab"):
                try:
                    if new_count_int_C > old_count_int_C:
                        print("Count updated")
                        self.mailPage2.click_mails_tab()
                        self.logger.info("User C New Count in Home tab: " + new_count_C)
                        self.mailPage2.get_mail_item_and_verification("Fw: " + subject, UserB_name, "C",
                                                                      test_case_number)
                        local_status = True
                        status_dict["TC_05"] = local_status
                    else:
                        self.logger.info("User C New Count in Mails tab: " + new_count_C)
                        assert False
                except AssertionError as e:
                    print("Item not present")
                    allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                    pytest.fail("TC_05 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()
                self.homePage2.click_logout()

        finally:
            with allure.step("Test Case Status"):
                verify_status(test_case_number, local_status)
                status_report_update_to_xls(sheet_name, local_status, test_case_number)

            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

        self.logger.info("* Mail test case TC_05 Ended *")


class TestPollingMail2users(BaseTest):
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "User A send a Mail to User B email id (Non contact), User B side mail received in polling sync for every 2 mins and validate count updated and select mails tab and select that received mail")
    def test_polling_TC_01_02_06_07(self):  # Includes TC_02, TC_06 and TC_07
        # global status_tc_01, status_tc_02, status_tc_06, status_tc_07
        generated_string = random_string(5)
        generated_string1 = random_string(5)
        generated_string2 = random_string(5)
        generated_string3 = random_string(5)

        subject_TC1 = "TC_01 Polling - " + generated_string
        subject_TC2 = "TC_02 Polling - " + generated_string1
        subject_TC6 = "TC_06 Polling - " + generated_string2
        subject_TC7 = "TC_07 Polling - " + generated_string3

        message = "Hi, This is automated test mail for mail receive case via Polling"
        reply_message = "Hi, this is reply mail"

        UserA_email = "triadqa3automation@yandex.com"
        # UserA_configuredEmail = "triadqa17@gmail.com"
        UserA_password = "Welcome123$#@!"
        UserA_name = "Triadqa3 Yandex"
        # UserB_email = "softwaretestingqa7011@outlook.com"
        # UserB_password = "Mithran1000@"
        # UserB_name = "Softwareuser 7011Automation"
        UserB_email = "triadqa3@yandex.com"
        UserB_configuredEmail = "triadautomationqa2@outlook.com"
        UserB_password = "Welcome123$#@!"
        UserB_name = "Triad Qa3Automation"
        test_case_number1 = "TC_01"
        test_case_number2 = "TC_02"
        test_case_number6 = "TC_06"
        test_case_number7 = "TC_07"
        self.logger.info("* Mail test case TC_01 ,TC_02, TC_06 and TC_07 started *")
        sheet_name = "Poll Mails"

        local_status_tc_01 = None
        local_status_tc_02 = None
        local_status_tc_06 = None
        local_status_tc_07 = None
        status_dict = {
            "TC_01": local_status_tc_01,
            "TC_02": local_status_tc_02,
            "TC_06": local_status_tc_06,
            "TC_07": local_status_tc_07
        }

        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User A side"):
                # User A side verification - getting unread count
                old_count_A = self.homePage.unread_count("mail")
                old_count_int_A = int(old_count_A)
                allure.attach("User A Old Count in Mails tab: " + old_count_A, name="UserA_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)

            self.logger.info("User A Old Count in Mails tab: " + old_count_A)

            with allure.step("Checking count after logged in User B side"):
                # User B side old count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User B Old Count in Mails tab: " + old_count_B)
                print("User B Old Count in Mails tab: " + old_count_B)

            # TC 1
            self.mailDraftPage.mail_send(subject_TC1, "TO", UserB_configuredEmail, "tab", message)

            with allure.step("TC_01 - Verify Mail sending in-progress in User A side"):
                print("Running Mail Poll TC 01")
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number1)
            time.sleep(3)

            # TC 2
            self.mailDraftPage.mail_send(subject_TC2, "TO", UserB_configuredEmail, "tab", message)
            print("Running Mail Poll TC 02")
            with allure.step("TC_02 - Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number2)
            time.sleep(3)

            # TC 6
            self.mailDraftPage.mail_send(subject_TC6, "TO", UserB_configuredEmail, "tab", message)
            print("Running Mail Poll TC 06")
            with allure.step("TC_06 - Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number6)
            time.sleep(3)

            # TC 7
            self.mailDraftPage.mail_send(subject_TC7, "TO", UserB_configuredEmail, "tab", message)
            print("Running Mail Poll TC 07")
            with allure.step("TC_07 - Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number7)

            with allure.step("TC_01 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Poll TC 01")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC1, UserB_name, "A", test_case_number1)
                self.mailPage.goback_tab()

            with allure.step("TC_02 - Verify Sent Mail item present in Mails tab from User A side"):
                print("Running Mail Poll TC 02")
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC2, UserB_name, "A", test_case_number2)
                self.mailPage.goback_tab()

            with allure.step("TC_06 - Verify Sent Mail item present in Mails tab from User A side"):
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                #   self.mailPage.click_mails_tab()
                print("Running Mail Poll TC 06")
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC6, UserB_name, "A", test_case_number6)
                self.mailPage.goback_tab()

            with allure.step("TC_07 - Verify Sent Mail item present in Mails tab from User A side"):
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                #   self.mailPage.click_mails_tab()
                print("Running Mail Poll TC 07")
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC7, UserB_name, "A", test_case_number7)
                self.mailPage.goback_tab()

            with allure.step("Waiting for Polling mail from user A in User B side and verify the count"):
                # self.mailPage1.wait_until_polling_mail_received("home")
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                if new_count_int_B > old_count_int_B + 3:
                    print("More than 3 new mail received")
                    allure.attach("User B New Count after mail received: " + new_count_B,
                                  name="UserB_count_after_received_polling_mail",
                                  attachment_type=allure.attachment_type.TEXT)
                else:
                    print("More than 3 new mail not received, so again wait for next sync")
                    self.mailPage1.wait_until_polling_mail_received("mail")
                    new_count_B = self.homePage1.unread_count("mail")
                    allure.attach("User B New Count after mail received: " + new_count_B,
                                  name="UserB_count_after_received_polling_mail",
                                  attachment_type=allure.attachment_type.TEXT)
                time.sleep(1)

            # TEST CASE 1
            with allure.step("TC_01 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Poll TC 01")
                self.mailPage1.click_mails_tab()
                time.sleep(1)
                self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B",
                                                              test_case_number1)
                self.mailPage1.goback_tab()
                time.sleep(1)
                local_status_tc_01 = True
                status_dict["TC_01"] = local_status_tc_01

            # TEST CASE 2
            with allure.step("TC_02 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Poll TC 02")
                with allure.step("Verify Mail present in Home tab"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC2, UserA_name, "B",
                                                                  test_case_number2)
                    # self.mailPage1.goback_tab()
                with allure.step("Reply to that Received Mail"):
                    self.mailPage1.click_reply_icon_1_user()
                    time.sleep(1)

                    self.mailDraftPage1.body_content_message("overlay", reply_message)
                    self.mailDraftPage1.click_send_button()
                with allure.step("Verify Mail reply in-progress in User B side"):
                    allure.attach(self.driver1.get_screenshot_as_png(), name="Mail_reply_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage1.wait_until_mail_send_overlay()

                with allure.step("Verify Reply sent Mail item present in Mails tab in User B side"):
                    # self.mailPage1.click_mails_tab()
                    # time.sleep(1)
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.get_mail_item_and_verification("Re: " + subject_TC2, UserA_name, "B",
                                                                  test_case_number2)

                with allure.step("Verify Mail item threaded in User B side"):
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.verify_mail_threaded(subject_TC2, UserA_name, "B", test_case_number2)

                with allure.step("Waiting for Polling reply mail from user B in User A side and verify the count"):
                    time.sleep(1)
                    check_count_A = self.homePage.unread_count("mail")
                    check_count_int_A = int(check_count_A)

                    if check_count_int_A == old_count_int_A:
                        self.mailPage.wait_until_polling_mail_received("mail")
                        new_count_A = self.homePage.unread_count("mail")
                        allure.attach("User A New Count after mail received: " + new_count_A,
                                      name="UserA_count_after_received_polling_reply_mail",
                                      attachment_type=allure.attachment_type.TEXT)
                        time.sleep(1)
                    elif check_count_int_A > old_count_int_A:
                        print("Count updated")
                    # goback_mails_tab(self.driver)

                with allure.step("Checking count in User A side after User B sent a Reply Mail"):
                    # User A side Verification
                    time.sleep(1)
                    new_count_A = self.homePage.unread_count("mail")
                    new_count_int_A = int(new_count_A)
                    allure.attach("User A New Count in Mails tab: " + new_count_A, name="UserA_New_Count",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("New Count in User A Mails tab: " + new_count_A)

                with allure.step("Verify count updated in User A side and Mail received in Mails tab"):
                    try:
                        if new_count_int_A > old_count_int_A:
                            print("Count updated")
                            # self.mailPage.click_mails_tab()
                            time.sleep(1)
                            self.mailPage.get_mail_item_and_verification("Re: " + subject_TC2, UserB_name,
                                                                         "A",
                                                                         test_case_number2)
                        else:
                            self.logger.info("* Mail count is not updated and count failed *")
                            assert False
                    except AssertionError as e:
                        print("Count not updated")
                        allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                        pytest.fail("TC_02 Assertion failed: Mail tab Count not updated {}".format(e))

                with allure.step("Verify Mail item threaded in User A side"):
                    time.sleep(1)
                    self.mailPage.goback_tab()
                    time.sleep(1)
                    self.mailPage.verify_mail_threaded("Re: " + subject_TC2, UserB_name, "A",
                                                       test_case_number2)
                time.sleep(1)
                local_status_tc_02 = True
                status_dict["TC_02"] = local_status_tc_02

            # TEST CASE 6
            with allure.step("TC_06 _ Verify count updated in User B side and Mail received in Mails tab"):
                print("Running Mail Poll TC 06")
                with allure.step("Verify Mail present in Home tab"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC6, UserA_name, "B",
                                                                  test_case_number6)
                    # self.mailPage1.goback_tab()
                    time.sleep(1)

                with allure.step("Delete that Received Mail"):
                    self.mailPage1.click_delete_icon()
                    time.sleep(1)
                    # click trash tab
                    self.homePage1.click_trash_tab()
                    time.sleep(1)

                with allure.step("Verify Mail present in Trash tab"):
                    # check mail in deleted tab
                    self.mailPage1.get_mail_item_and_verification(subject_TC6, UserA_name, "B",
                                                                  test_case_number6)
                    self.mailPage1.goback_tab()

                local_status_tc_06 = True
                status_dict["TC_06"] = local_status_tc_06

            # TEST CASE 7
            with allure.step("TC_07 _ Verify count updated in User B side and Mail received in Home tab"):
                print("Running Mail Poll TC 07")
                self.mailPage1.click_mails_tab()
                time.sleep(1)
                with allure.step("Verify Mail present in Home tab"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC7, UserA_name, "B",
                                                                  test_case_number7)

                with allure.step("Delete that Received Mail"):
                    self.mailPage1.click_delete_icon()
                    time.sleep(1)
                    # User B side new count after deleted the mail
                    new_count_after_delete_B = self.homePage1.unread_count("mail")
                    new_count_after_delete_int_B = int(new_count_after_delete_B)
                    allure.attach("User B New Count in Mails tab: " + new_count_after_delete_B,
                                  name="User B new count after Delete a mail ",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("User B New Count in Mails tab after Mail deleted: " + new_count_after_delete_B)

                    # click trash tab
                    self.homePage1.click_trash_tab()
                    time.sleep(1)
                with allure.step("Verify Mail present in Trash tab"):
                    # check mail in deleted tab
                    self.mailPage1.get_mail_item_and_verification(subject_TC7, UserA_name, "B",
                                                                  test_case_number7)

                with allure.step("Restore the Deleted mail from Trash tab"):
                    self.mailPage1.click_restore_un_spam_icon()
                    self.mailPage1.wait_until_table_explore()
                    time.sleep(0.5)

                with allure.step("Checking count in User B side after Restore the deleted Mail"):
                    # User B side new count after restore mail
                    new_count_after_restore_B = self.homePage1.unread_count("mail")
                    new_count_after_restore_int_B = int(new_count_after_restore_B)
                    allure.attach("User B New Count in Mails tab: " + new_count_after_restore_B,
                                  name="User B new count after restore the Deleted mail ",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info(
                        "User B New Count in Mails tab after Mail restored: " + new_count_after_restore_B)

                with allure.step("Verify Mail present in Home tab after Restore the deleted Mail"):

                    try:
                        if new_count_after_restore_int_B > new_count_after_delete_int_B:
                            self.mailPage1.click_mails_tab()
                            time.sleep(1)
                            self.mailPage1.get_mail_item_and_verification(subject_TC7, UserA_name, "B",
                                                                          test_case_number7)
                            local_status_tc_07 = True
                            status_dict["TC_07"] = local_status_tc_07
                        else:
                            self.logger.info("* Mail count is not updated and count failed *")
                            assert False
                    except AssertionError as e:
                        print("Item not present")
                        allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                        pytest.fail("TC_07 Assertion failed: Mail tab Count not updated {}".format(e))

                # self.mailPage1.goback_tab()
                time.sleep(1)
            # self.contactsPage.block_contact(UserB_name)
            # time.sleep(1)

            # self.contactsPage1.block_contact(UserA_name)
            # time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            with allure.step("Each Test Case Status"):
                verify_status(test_case_number1, local_status_tc_01)
                verify_status(test_case_number2, local_status_tc_02)
                verify_status(test_case_number6, local_status_tc_06)
                verify_status(test_case_number7, local_status_tc_07)
                status_report_update_to_xls(sheet_name, local_status_tc_01, test_case_number1)
                status_report_update_to_xls(sheet_name, local_status_tc_02, test_case_number2)
                status_report_update_to_xls(sheet_name, local_status_tc_06, test_case_number6)
                status_report_update_to_xls(sheet_name, local_status_tc_07, test_case_number7)

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

        self.logger.info("* Mail test case TC_01 Ended *")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "User A send a Mail to User B email id (Non contact), User B side mail received in polling sync for every 2 mins and validate count updated and select mails tab and select that received mail")
    def test_polling_TC_08(self):
        # global status_tc_08
        generated_string = random_string(5)
        subject_TC1 = "TC_08 Polling - " + generated_string
        message = "Hi, This is automated test mail for mail resend case via Polling"
        UserA_email = "triadqa3@aol.com"
        UserA_password = "Welcome123$#@!"
        UserA_name = "Triadqa3 AolAutomation"
        # UserB_email = "softwaretestingqa7011@outlook.com"
        # UserB_password = "Mithran1000@"
        # UserB_name = "Softwareuser 7011Automation"
        UserB_email = "triadqa3@yandex.com"
        UserB_configuredEmail = "triadautomationqa2@outlook.com"
        UserB_password = "Welcome123$#@!"
        UserB_name = "Triad Qa3Automation"
        test_case_number1 = "TC_08"
        self.logger.info("* Mail test case TC_08 started *")
        sheet_name = "Poll Mails"
        local_status_tc_08 = None
        status_dict = {
            "TC_08": local_status_tc_08
        }

        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User B side"):
                print("Running Mail Poll TC 08")
                # User B side old count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User B Old Count in Mails tab: " + old_count_B)
                print("User B Old Count in Mails tab: " + old_count_B)

            self.mailDraftPage.mail_send(subject_TC1, "TO", UserB_configuredEmail, "tab", message)

            with allure.step("Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number1)

            with allure.step("Verify Sent Mail item present in Mails tab from User A side"):
                time.sleep(1)
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC1, UserB_name, "A", test_case_number1)

            with allure.step("User A Resend the Mail to User B"):
                time.sleep(1)
                self.mailPage.click_resend()
                time.sleep(1)
                self.mailDraftPage.click_send_button()

                with allure.step("Verify Mail sending in-progress in User A side"):
                    allure.attach(self.driver.get_screenshot_as_png(), name="Mail_Re-sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage.wait_until_mail_send_overlay()
                time.sleep(1)

            with allure.step("Waiting for Polling mail from user A in User B side and verify the count"):
                # self.mailPage1.wait_until_polling_mail_received("home")
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                if new_count_int_B > old_count_int_B + 1:
                    print("More than 1 new mail received")
                    allure.attach("User B New Count after mail received: " + new_count_B,
                                  name="UserB_count_after_received_polling_mail",
                                  attachment_type=allure.attachment_type.TEXT)
                else:
                    print("More than 1 new mail not received, so again wait for next sync")
                    self.mailPage1.wait_until_polling_mail_received("mail")
                    new_count_B = self.homePage1.unread_count("mail")
                    allure.attach("User B New Count after mail received: " + new_count_B,
                                  name="UserB_count_after_received_polling_mail",
                                  attachment_type=allure.attachment_type.TEXT)
                time.sleep(1)
            with allure.step("Verify count updated in User B side and Mail received in Mails tab"):
                # try:

                #    if new_count_int_B in [old_count_int_B + 1, old_count_int_B + 2, old_count_int_B + 3, old_count_int_B + 4]:
                self.mailPage1.click_mails_tab()
                time.sleep(1)
                self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B", test_case_number1)
                #     else:
                #         self.logger.info("* Mail count is not updated and count failed *")
                #         assert False
                # except AssertionError as e:
                #     print("Item not present")
                #     allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                #     pytest.fail("TC_08 Assertion failed: Mail tab Count not updated {}".format(e))

            with allure.step("Verify Mail item threaded in User B side"):
                self.mailPage1.goback_tab()
                time.sleep(1)
                self.mailPage1.verify_mail_threaded(subject_TC1, UserA_name, "B", test_case_number1)
                local_status_tc_08 = True
                status_dict["TC_08"] = local_status_tc_08
            # self.contactsPage.block_contact(UserB_name)
            # time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            with allure.step("Test Case Status"):
                verify_status(test_case_number1, local_status_tc_08)
                status_report_update_to_xls(sheet_name, local_status_tc_08, test_case_number1)

            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("User A send a Mail to User B email id (Non contact), User B side mail received in polling "
                        "and check spam icon and spam that Mail and unspam the mail adn Verify")
    def test_polling_TC_09(self):
        # global status_tc_09
        generated_string = random_string(5)
        subject_TC1 = "TC_09 Polling - " + generated_string
        message = "Hi, This is automated test mail for Spam case via Polling"
        UserA_email = "triadqa3@aol.com"
        UserA_password = "Welcome123$#@!"
        UserA_name = "Triadqa3 AolAutomation"
        # UserB_email = "triadqa8@outlook.com"
        # UserB_password = "Welcome123$"
        # UserB_name = "Triad QA8out"
        UserB_email = "clarititest3@yandex.com"
        UserB_configuredEmail = "triadautomationqa3@outlook.com"
        UserB_password = "Triad@#123"
        UserB_name = "Clariti test3"
        test_case_number1 = "TC_09"
        self.logger.info("* Mail test case TC_09 started *")
        sheet_name = "Poll Mails"
        local_status_tc_09 = None
        status_dict = {
            "TC_09": local_status_tc_09
        }

        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                time.sleep(1)

            with allure.step("Checking count after logged in User B side"):
                print("Running Mail Poll TC 09")
                # User B side old count
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User B Old Count in Mails tab: " + old_count_B)
                print("User B Old Count in Mails tab: " + old_count_B)

            self.mailDraftPage.mail_send(subject_TC1, "TO", UserB_configuredEmail, "tab", message)

            with allure.step("Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number1)

            with allure.step("Verify Sent Mail item present in Mails tab from User A side"):
                time.sleep(1)
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC1, UserB_name, "A", test_case_number1)

            with allure.step("Waiting for Polling mail from user A in User B side and verify the count"):
                # self.mailPage1.wait_until_polling_mail_received("mail")
                new_count_B = self.homePage1.unread_count("mail")
                new_count_int_B = int(new_count_B)
                print("User B new Count in Mails tab: " + old_count_B)
                print("More than 3 new mail received")
                allure.attach("User B New Count after mail received: " + new_count_B,
                              name="UserB_count_after_received_polling_mail",
                              attachment_type=allure.attachment_type.TEXT)

                self.mailPage1.click_mails_tab()
                time.sleep(1)

            with allure.step("Verify count updated in User B side and Mail received in Mails tab"):
                if new_count_int_B > old_count_int_B:
                    print("More than 1 new mail received")
                    allure.attach("User B New Count after mail received: " + new_count_B,
                                  name="UserB_count_after_received_polling_mail",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B", test_case_number1)

                else:
                    print("More than 1 new mail not received, so again wait for next sync")
                    self.mailPage1.wait_until_polling_mail_received("mail")
                    new_count_B = self.homePage1.unread_count("mail")
                    allure.attach("User B New Count after mail received: " + new_count_B,
                                  name="UserB_count_after_received_polling_mail",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B", test_case_number1)
                time.sleep(1)

            with allure.step("Spam the Received mail"):
                self.mailPage1.click_spam_icon()
                time.sleep(1)
                self.mailPage1.click_add_in_spam_dialog()
                self.mailPage1.wait_until_mail_tab_page()

            with allure.step("Verify Spammed mail in Trash tab"):
                # click trash tab
                self.homePage1.click_trash_tab()
                time.sleep(3)
                # check mail in deleted tab
                self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B", test_case_number1)
                self.mailPage1.verify_spammed_mail_text()

            with allure.step("Un-spam mail from Trash tab"):
                self.mailPage1.click_restore_un_spam_icon()
                # self.mailPage1.trash_tab_ui()
                time.sleep(2)
                self.mailPage1.click_mails_tab()
                time.sleep(1)

                with allure.step("Verify Un-spammed mail moved into Mails tab"):
                    time.sleep(1)
                    self.mailPage1.get_mail_item_and_verification(subject_TC1, UserA_name, "B", test_case_number1)
                    local_status_tc_09 = True
                    status_dict["TC_09"] = local_status_tc_09
            # self.contactsPage.block_contact(UserB_name)
            # time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()

        finally:
            with allure.step("Test Case Status"):
                verify_status(test_case_number1, local_status_tc_09)
                status_report_update_to_xls(sheet_name, local_status_tc_09, test_case_number1)

            with allure.step("Overall Status"):
                overall_status = "pass" if all(status is not None for status in status_dict.values()) else "fail"
                if overall_status == "fail":
                    error_message = "Test case failed. Failed test steps: "
                    failed_steps = [test_case for test_case, status in status_dict.items() if status is None]
                    error_message += ", ".join(failed_steps)
                    pytest.fail(error_message)

        self.logger.info("* Mail Polling test case TC_09 Ended *")


class TestPollingMail3users(BaseTest3):
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_03 - User A send a Mail to User B and user C(non_contacts), Verify from both users mail received or not and count updated or not,.\n"
        "TC_04 - User A send a Mail to User B and user C(non_contacts), User B Reply All to that mail and Verify from both users mail received or not and count updated or not,.\n"
        "TC_05 - User A send a Mail to User B and user C(non_contacts), User B forward to User C and Verify from both users mail received or not and count updated or not,.\n"
    )
    def test_polling_TC_03_04_05(self):  # Includes TC_04, TC_05
        # global status_tc_03, status_tc_04, status_tc_05
        generated_string = random_string(5)
        generated_string1 = random_string(5)
        generated_string2 = random_string(5)

        subject_TC3 = "TC_03 Polling - " + generated_string
        subject_TC4 = "TC_04 Polling - " + generated_string1
        subject_TC5 = "TC_05 Polling - " + generated_string2

        message = "Hi, This is automated test mail for mail receive case via Polling"
        reply_message = "Hi, this is reply mail"

        UserA_email = "triadqa3automation@yandex.com"
        # UserA_configuredEmail = "triadqa17@gmail.com"
        UserA_password = "Welcome123$#@!"
        UserA_name = "Triadqa3 Yandex"
        # UserB_name = "Softwareuser 7011Automation"
        # UserB_Dname = "Softwareuser 7011"
        # UserB_email = "softwaretestingqa7011@outlook.com"
        # UserB_password = "Mithran1000@"
        UserB_email = "triadqa3@yandex.com"
        UserB_configuredEmail = "triadautomationqa2@outlook.com"
        UserB_password = "Welcome123$#@!"
        UserB_name = "Triad Qa3Automation"
        UserB_BrowserName = "TriadAutomation QA3"
        # UserC_email = "triadqa8@outlook.com"
        # UserC_password = "Welcome123$"
        # UserC_name = "Triad QA8out"
        UserC_email = "clarititest3@yandex.com"
        UserC_configuredEmail = "triadautomationqa3@outlook.com"
        UserC_password = "Triad@#123"
        UserC_name = "Clariti test3"
        test_case_number3 = "TC_03"
        test_case_number4 = "TC_04"
        test_case_number5 = "TC_05"
        self.logger.info("* Mail test case TC_03 ,TC_04 and TC_05 started *")
        sheet_name = "Poll Mails"

        local_status_tc_03 = None
        local_status_tc_04 = None
        local_status_tc_05 = None
        status_dict = {
            "TC_03": local_status_tc_03,
            "TC_04": local_status_tc_04,
            "TC_05": local_status_tc_05
        }

        try:
            with allure.step("Login to clariti User A and User B and User C"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                self.loginPage1.clariti_sign_in(UserB_email, UserB_password)
                self.loginPage2.clariti_sign_in(UserC_email, UserC_password)
                time.sleep(1)

            # User A side verification - getting unread count
            with allure.step("Checking count after logged in User A side"):
                old_count_A = self.homePage.unread_count("mail")
                old_count_int_A = int(old_count_A)
                allure.attach("User A Old Count in Mails tab: " + old_count_A, name="UserA_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User A Old Count in Mails tab: " + old_count_A)
                print("User A Old Count in Mails tab: " + old_count_A)

            # User B side verification - getting unread count
            with allure.step("Checking count after logged in User B side"):
                old_count_B = self.homePage1.unread_count("mail")
                old_count_int_B = int(old_count_B)
                allure.attach("User B Old Count in Mails tab: " + old_count_B, name="UserB_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User B Old Count in Mails tab: " + old_count_B)
                print("User B Old Count in Mails tab: " + old_count_B)

            # User C side verification - getting unread count
            with allure.step("Checking count after logged in User C side"):
                old_count_C = self.homePage2.unread_count("mail")
                old_count_int_C = int(old_count_C)
                allure.attach("User C Old Count in Mails tab: " + old_count_C, name="UserC_count_after_logged_in",
                              attachment_type=allure.attachment_type.TEXT)
                self.logger.info("User C Old Count in Mails tab: " + old_count_C)
                print("User C Old Count in Mails tab: " + old_count_C)

            # TC 3
            self.mailDraftPage.mail_send_2_users(subject_TC3, "TO", UserB_configuredEmail, UserC_configuredEmail,
                                                 "tab", message)
            print("Running Mail Poll TC 03")
            with allure.step("TC_03 - Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number3)
            time.sleep(3)

            # TC 4
            self.mailDraftPage.mail_send_2_users(subject_TC4, "TO", UserB_configuredEmail, UserC_configuredEmail,
                                                 "tab", message)
            print("Running Mail Poll TC 04")
            with allure.step("TC_04 - Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number4)
            time.sleep(3)

            # TC 5
            self.mailDraftPage.mail_send_2_users(subject_TC5, "TO", UserB_configuredEmail, UserC_configuredEmail,
                                                 "tab", message)
            print("Running Mail Poll TC 05")
            with allure.step("TC_05 - Verify Mail sending in-progress in User A side"):
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_sending_inprogress",
                              attachment_type=AttachmentType.PNG)
                self.mailPage.mail_send_validation(test_case_number5)
            time.sleep(3)

            with allure.step("TC_03 - Verify Sent Mail item present in Mails tab from User A side"):
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC3, UserB_name, "A", test_case_number3)
                self.mailPage.goback_tab()

            with allure.step("TC_04 - Verify Sent Mail item present in Mails tab from User A side"):
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC4, UserB_name, "A", test_case_number4)
                self.mailPage.goback_tab()

            with allure.step("TC_05 - Verify Sent Mail item present in Mails tab from User A side"):
                # allure.attach("Clicked Mails tab", name="Action", attachment_type=allure.attachment_type.TEXT)
                #   self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailPage.get_mail_item_and_verification(subject_TC5, UserB_name, "A", test_case_number5)
                self.mailPage.goback_tab()

            # User B side case TC 03 - "User A send a Mail to User B and user C(non_contacts), Verify from both users
            # mail received or not and count updated or not,."

            with allure.step("TC_03 _ Verify count updated in User B and User C side and Mail received in Mails tab"):
                print("Running Mail Poll TC 03")
                with allure.step("Waiting for Polling mail from user A in User B side and verify the count"):
                    print("User B waiting for Polling mail")
                    # self.mailPage1.wait_until_polling_mail_received("home")
                    new_count_B = self.homePage1.unread_count("mail")
                    new_count_int_B = int(new_count_B)
                    # if old_count_int_B + 2 < new_count_int_B:
                    #     print("More than 2 new mail received")
                    #     allure.attach("User B New Count after mail received: " + new_count_B,
                    #                   name="UserB_count_after_received_polling_mail",
                    #                   attachment_type=allure.attachment_type.TEXT)
                    # else:
                    #     print("More than 2 new mail not received, so again wait for next sync")
                    #     self.mailPage1.wait_until_polling_mail_received("home")
                    #     new_count_B = self.homePage1.unread_count("home")
                    #     allure.attach("User B New Count after mail received: " + new_count_B,
                    #                   name="UserB_count_after_received_polling_mail",
                    #                   attachment_type=allure.attachment_type.TEXT)
                    if new_count_int_B > old_count_int_B + 2:
                        print("More than 2 new mail received")
                        allure.attach("User B New Count after mail received: " + new_count_B,
                                      name="UserB_count_after_received_polling_mail",
                                      attachment_type=allure.attachment_type.TEXT)
                    else:
                        print("More than 2 new mail not received, so again wait for next sync")
                        self.mailPage1.wait_until_polling_mail_received("mail")
                        new_count_B = self.homePage1.unread_count("mail")
                        allure.attach("User B New Count after mail received: " + new_count_B,
                                      name="UserB_count_after_received_polling_mail",
                                      attachment_type=allure.attachment_type.TEXT)
                    time.sleep(1)

                with allure.step("User B side - Verification"):
                    self.mailPage1.click_mails_tab()
                    time.sleep(1)
                    self.mailPage1.get_mail_item_and_verification(subject_TC3, UserA_name, "B",
                                                                  test_case_number3)
                    self.mailPage1.goback_tab()
                    time.sleep(1)

                with allure.step("Waiting for Polling mail from user A in User C side and verify the count"):
                    print("User C waiting for Polling mail")
                    self.mailPage2.click_mails_tab()
                    new_count_C = self.homePage2.unread_count("mail")
                    new_count_int_C = int(new_count_C)
                    if old_count_int_C + 2 < new_count_int_C:
                        print("More than 2 new mail received")
                        allure.attach("User C New Count after mail received: " + new_count_C,
                                      name="UserC_count_after_received_polling_mail",
                                      attachment_type=allure.attachment_type.TEXT)
                    elif old_count_int_C == new_count_int_C:
                        print("More than 2 new mail not received, so again wait for next sync")
                        self.mailPage2.wait_until_polling_mail_received("mail")
                        new_count_C = self.homePage2.unread_count("mail")
                        allure.attach("User C New Count after mail received: " + new_count_C,
                                      name="UserC_count_after_received_polling_mail",
                                      attachment_type=allure.attachment_type.TEXT)
                    else:
                        print("More than 2 new mail not received, so again wait for next sync")
                        self.mailPage2.wait_until_polling_mail_received("mail")
                        new_count_C = self.homePage2.unread_count("mail")
                        allure.attach("User C New Count after mail received: " + new_count_C,
                                      name="UserC_count_after_received_polling_mail",
                                      attachment_type=allure.attachment_type.TEXT)
                    time.sleep(1)

                with allure.step("User C side - Verification"):
                    self.mailPage2.get_mail_item_and_verification(subject_TC3, UserA_name, "C", test_case_number3)
                    self.mailPage2.goback_tab()
                    # self.homePage2.click_home_tab()
                    time.sleep(1)
                local_status_tc_03 = True
                status_dict["TC_03"] = local_status_tc_03

            # TEST CASE 4 - "User A send a Mail to User B and user C(non_contacts), User B Reply All to that mail and Verify
            # from both users mail received or not and count updated or not,."

            with allure.step(
                    "TC_04 _ Verify count updated in User B side and Mail received in Mails tab then Reply All and Verified in User A and User C"):
                print("Running Mail Poll TC 04")
                # User C side verification - getting unread count
                with allure.step("Checking count in User C after testcase 3 completed"):
                    old_count_C_after_tc3 = self.homePage2.unread_count("mail")
                    old_count_int_C_after_tc3 = int(old_count_C_after_tc3)
                    allure.attach("User C Old Count in Mails tab: " + old_count_C_after_tc3,
                                  name="UserC_count_after_TC_3",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("User C Old Count in Mails tab after TC3: " + old_count_C_after_tc3)
                    print("User C Old Count in Mails tab after TC3: " + old_count_C_after_tc3)

                with allure.step("Verify Mail present in Home tab"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC4, UserA_name, "B",
                                                                  test_case_number4)
                    # self.mailPage1.goback_tab()
                with allure.step("Reply to that Received Mail"):
                    self.mailPage1.click_reply_all_icon()
                    time.sleep(1)

                    self.mailDraftPage1.body_content_message("overlay", reply_message)
                    self.mailDraftPage1.click_send_button()
                with allure.step("Verify Mail reply in-progress in User B side"):
                    allure.attach(self.driver1.get_screenshot_as_png(), name="Mail_reply_sending_inprogress",
                                  attachment_type=AttachmentType.PNG)
                    self.mailPage1.wait_until_mail_send_overlay()

                with allure.step("Verify Reply All sent Mail item present in Mails tab in User B side"):
                    # self.mailPage1.click_mails_tab()
                    # time.sleep(1)
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.get_mail_item_and_verification("Re: " + subject_TC4, UserA_name, "B",
                                                                  test_case_number4)

                with allure.step("Verify Mail item threaded in User B side"):
                    self.mailPage1.goback_tab()
                    time.sleep(1)
                    self.mailPage1.verify_mail_threaded(subject_TC4, UserA_name, "B", test_case_number4)

                with allure.step("User A side - Verification"):
                    print("User A waiting for Polling mail")
                    with allure.step("Waiting for Polling reply mail from user B in User A side and verify the count"):
                        time.sleep(1)
                        check_count_A = self.homePage.unread_count("mail")
                        check_count_int_A = int(check_count_A)

                        if check_count_int_A == old_count_int_A:
                            self.mailPage.wait_until_polling_mail_received("mail")
                            new_count_A = self.homePage.unread_count("mail")
                            # allure.attach("User A New Count after mail received: " + new_count_A,name="UserA_count_after_received_polling_reply_mail",attachment_type=allure.attachment_type.TEXT)
                            time.sleep(1)
                        elif check_count_int_A > old_count_int_A:
                            print("Count updated")
                        # goback_mails_tab(self.driver)

                    with allure.step("Checking count in User A side after User B sent a Reply Mail"):
                        # User A side Verification
                        time.sleep(1)
                        new_count_A = self.homePage.unread_count("mail")
                        new_count_int_A = int(new_count_A)
                        allure.attach("User A New Count in Mails tab: " + new_count_A, name="UserA_New_Count",
                                      attachment_type=allure.attachment_type.TEXT)
                        self.logger.info("New Count in User A Mails tab: " + new_count_A)
                        time.sleep(0.5)

                    with allure.step("Verify count updated in User A side and Mail received in Mails tab"):
                        try:
                            if new_count_int_A > old_count_int_A:
                                print("Count updated")
                                # self.mailPage.click_mails_tab()
                                time.sleep(1)
                                self.mailPage.get_mail_item_and_verification("Re: " + subject_TC4,
                                                                             UserB_name, "A",
                                                                             test_case_number4)
                            else:
                                self.logger.info("* Mail count is not updated and count failed *")
                                assert False
                        except AssertionError as e:
                            print("Count not updated")
                            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
                            pytest.fail("TC_04 Assertion failed: Mail tab Count not updated {}".format(e))

                    with allure.step("Verify Mail item threaded in User A side"):
                        time.sleep(1)
                        self.mailPage.goback_tab()
                        time.sleep(1)
                        self.mailPage.verify_mail_threaded("Re: " + subject_TC4, UserB_name, "A",
                                                           test_case_number4)
                    time.sleep(1)

                with allure.step("User C side - Verification"):
                    print("User C waiting for Polling mail")

                    with allure.step("Waiting for Polling reply mail from user B in User C side and verify the count"):
                        time.sleep(1)
                        check_count_C = self.homePage2.unread_count("mail")
                        check_count_int_C = int(check_count_C)
                        print("New count in User C after User B send a reply ALl mail: " + check_count_C)
                        if old_count_int_C_after_tc3 < check_count_int_C:
                            print("New count in User C after User B send a reply ALl mail")
                            print("3 Mails Received and 1 mail already read for case 4: " + check_count_C)

                            # self.mailPage2.wait_until_polling_mail_received("mail")
                            new_count_C = self.homePage2.unread_count("mail")
                            allure.attach("User C New Count after mail received: " + new_count_C,
                                          name="UserC_count_after_received_polling_reply_mail",
                                          attachment_type=allure.attachment_type.TEXT)
                            time.sleep(1)
                        elif old_count_int_C_after_tc3 >= check_count_int_C:
                            print("3 Mails Received: " + check_count_C)
                            self.mailPage2.wait_until_polling_mail_received("mail")
                            new_count_C = self.homePage2.unread_count("mail")
                            allure.attach("User C New Count after mail received: " + new_count_C,
                                          name="UserC_count_after_received_polling_reply_mail",
                                          attachment_type=allure.attachment_type.TEXT)
                            time.sleep(1)
                            # elif check_count_int_C > old_count_int_C_after_tc3 + 1:
                            #     print("More than 3 Mails Received: " + check_count_C)
                            time.sleep(1)

                        # goback_mails_tab(self.driver)

                    with allure.step("Checking count in User C side after User B sent a Reply Mail"):
                        # User A side Verification
                        time.sleep(1)
                        new_count_C = self.homePage2.unread_count("mail")
                        new_count_int_C = int(new_count_C)
                        allure.attach("User C New Count in Mails tab: " + new_count_C, name="UserC_New_Count",
                                      attachment_type=allure.attachment_type.TEXT)
                        self.logger.info("New Count in User C Mails tab: " + new_count_C)

                    with allure.step("Verify count updated in User C side and Mail received in Mails tab"):
                        try:
                            if old_count_int_C_after_tc3 < new_count_int_C:
                                print("Count updated- More than 3 Mails Received")
                                # self.mailPage2.click_mails_tab()
                                time.sleep(1)
                                self.mailPage2.get_mail_item_and_verification("Re: " + subject_TC4, UserB_BrowserName,
                                                                              "C",
                                                                              test_case_number4)
                            else:
                                self.logger.info("* Mail count is not updated and count failed *")
                                assert False
                        except AssertionError as e:
                            print("Count not updated")
                            allure.attach(str(e), name="Assertion Error",
                                          attachment_type=allure.attachment_type.TEXT)
                            pytest.fail("TC_04 Assertion failed: Mail tab Count not updated {}".format(e))

                    with allure.step("Verify Mail item threaded in User A side"):
                        time.sleep(1)
                        self.mailPage2.goback_tab()
                        time.sleep(1)
                        self.mailPage2.verify_mail_threaded("Re: " + subject_TC4, UserB_BrowserName, "C",
                                                            test_case_number4)
                        self.homePage2.click_home_tab()
                        self.mailPage2.click_mails_tab()
                    time.sleep(1)

                local_status_tc_04 = True
                status_dict["TC_04"] = local_status_tc_04

            # TEST CASE 5 - "User A send a Mail to User B and user C(non_contacts), User B forward to User C and Verify from
            # both users mail received or not and count updated or not,.")

            with allure.step(
                    "TC_05 _ Verify count updated in User B side and Mail received in Mails tab then Forward to user C"):
                print("Running Mail Poll TC 05")
                self.homePage1.click_trash_tab()
                self.mailPage1.click_mails_tab()
                time.sleep(1)

                # User C side verification - getting unread count
                with allure.step("Checking count in User C after testcase 3 completed"):
                    old_count_C_after_tc4 = self.homePage2.unread_count("mail")
                    old_count_int_C_after_tc4 = int(old_count_C_after_tc4)
                    allure.attach("User C Old Count in Mails tab: " + old_count_C_after_tc4,
                                  name="UserC_count_after_TC_4",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("User C Old Count in Mails tab: " + old_count_C_after_tc4)
                    print("User C Old Count in Mails tab: " + old_count_C_after_tc4)

                with allure.step("Verify Mail present in Home tab"):
                    self.mailPage1.get_mail_item_and_verification(subject_TC5, UserA_name, "B",
                                                                  test_case_number5)
                    # self.mailPage1.goback_tab()
                    time.sleep(1)

                with allure.step("User B Forward to that Received Mail"):
                    time.sleep(1)
                    self.mailPage1.click_forward_icon_received()
                    time.sleep(1)
                    self.mailDraftPage1.enter_to_address(UserC_configuredEmail)
                    self.mailDraftPage1.body_content_message("overlay", reply_message)
                    self.mailDraftPage1.click_send_button()

                    with allure.step("Verify Mail forward in-progress in User B side"):
                        allure.attach(self.driver1.get_screenshot_as_png(), name="Mail_forward_sending_inprogress",
                                      attachment_type=AttachmentType.PNG)

                        self.mailPage1.wait_until_mail_send_overlay()

                    with allure.step("Verify Forward Sent Mail item present in Mails tab from User B side"):
                        # self.mailPage1.click_mails_tab()
                        # time.sleep(1)
                        self.mailPage1.goback_tab()
                        time.sleep(1)
                        self.mailPage1.get_mail_item_and_verification("Fw: " + subject_TC5, UserC_name, "B",
                                                                      test_case_number5)

                time.sleep(1)

                with allure.step("Verify Mail item threaded in User B side"):
                    self.mailPage1.goback_tab()
                    time.sleep(2)
                    self.mailPage1.verify_mail_threaded(subject_TC5, UserA_name, "B", test_case_number5)

                with allure.step("User C side - Verification"):
                    print("User C waiting for Polling mail")

                    with allure.step(
                            "Waiting for Polling forward mail from user B in User C side and verify the count"):
                        time.sleep(1)
                        check_count_C = self.homePage2.unread_count("mail")
                        check_count_int_C = int(check_count_C)

                        if check_count_int_C == old_count_int_C_after_tc4 + 1:
                            print("New count in User C after User B send a forward mail")
                            # self.mailPage2.wait_until_polling_mail_received("mail")
                            new_count_C = self.homePage2.unread_count("mail")
                            allure.attach("User A New Count after mail received: " + new_count_C,
                                          name="UserA_count_after_received_polling_reply_mail",
                                          attachment_type=allure.attachment_type.TEXT)

                            time.sleep(1)
                        elif check_count_int_C < old_count_int_C_after_tc4 + 1:
                            print("4 Mails Received: " + check_count_C)
                            self.mailPage2.wait_until_polling_mail_received("mail")
                            new_count_C = self.homePage2.unread_count("mail")
                            allure.attach("User C New Count after mail received: " + new_count_C,
                                          name="UserC_count_after_received_polling_reply_mail",
                                          attachment_type=allure.attachment_type.TEXT)
                            time.sleep(1)
                        elif check_count_int_C > old_count_int_C_after_tc4 + 1:
                            print("More than 4 Mails Received: " + check_count_C)
                            time.sleep(1)
                    with allure.step("Checking count in User C side after User B sent a Forward Mail"):
                        # User C side Verification
                        time.sleep(1)
                        new_count_C = self.homePage2.unread_count("mail")
                        new_count_int_C = int(new_count_C)
                        allure.attach("User C New Count in Mails tab: " + new_count_C, name="UserC_New_Count",
                                      attachment_type=allure.attachment_type.TEXT)
                        self.logger.info("New Count in User C Mails tab: " + new_count_C)

                    with allure.step("Verify count updated in User C side and Mail received in Mails tab"):
                        try:
                            if new_count_int_C > old_count_int_C_after_tc4:
                                print("Count updated - More than 3 Mails Received")
                                # self.mailPage2.click_mails_tab()
                                time.sleep(2)
                                self.mailPage2.get_mail_item_and_verification("Fw: " + subject_TC5, UserB_BrowserName,
                                                                              "C",
                                                                              test_case_number5)
                            else:
                                self.logger.info("* Mail count is not updated and count failed *")
                                assert False
                        except AssertionError as e:
                            print("Count not updated")
                            allure.attach(str(e), name="Assertion Error",
                                          attachment_type=allure.attachment_type.TEXT)
                            pytest.fail("TC_05 Assertion failed: Mail tab Count not updated {}".format(e))

                    with allure.step("Verify Mail item threaded in User C side"):
                        time.sleep(1)
                        self.mailPage2.goback_tab()
                        time.sleep(1)
                        self.mailPage2.verify_mail_threaded("Fw: " + subject_TC5, UserB_BrowserName, "C",
                                                            test_case_number5)
                    time.sleep(1)

                    local_status_tc_05 = True
                    status_dict["TC_05"] = local_status_tc_05

            # self.contactsPage.block_contact(UserB_name)
            # time.sleep(1)
            # self.homePage.click_trash_tab()
            # self.contactsPage.block_contact(UserC_name)
            # time.sleep(1)
            # self.contactsPage1.block_contact(UserA_name)
            # time.sleep(1)
            # self.homePage1.click_trash_tab()
            # self.contactsPage1.block_contact(UserC_name)
            # time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()
                self.homePage1.click_logout()
                self.homePage2.click_logout()

        finally:
            verify_status(test_case_number3, local_status_tc_03)
            verify_status(test_case_number4, local_status_tc_04)
            verify_status(test_case_number5, local_status_tc_05)
            status_report_update_to_xls(sheet_name, local_status_tc_03, test_case_number3)
            status_report_update_to_xls(sheet_name, local_status_tc_04, test_case_number4)
            status_report_update_to_xls(sheet_name, local_status_tc_05, test_case_number5)

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

        self.logger.info("* Mail test case TC_03, TC_04 and TC_05 Ended *")


class TestMailBasicCases(BaseTest1):
    logger = LogGen.loggen()

    # @pytest.mark.pushMail1
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_01 - Login/Signup to clariti and Verify Mails and Bring Mails option are available\n"
        "TC_02 - Check whether the Mails menu is clickable\n"
        "TC_03 - Check whether the Bring Mails menu is clickable\n"
        "TC_04 - Configure email in Bring Mails and verify respective configured emails are listed\n"
        "TC_05 - Check whether Compose Mail option is available in Conversation tab or not\n"
        "TC_06 - Check whether Compose Mail option is available in Mail tab or not, before configure email address\n"
        "TC_08 - Check whether the draft is formed after click Compose Mail with out email configuration\n"
        "TC_09 - Check the Email icon, draft text & no subject label\n"
        "TC_10 - Check the New Mail is displayed in draft header\n"
        "TC_11 - Check whether the Cursor focus is blinking on subject field\n"
        "TC_12 - Check whether the placeholder text is displayed\n"
        "TC_13 - Check the subject field allow user to enter text\n"
        "TC_14 - Check whether '+' button (Add from your contacts) is clickable\n"
        "TC_15 - Check whether the proper alert is displayed while adding Clariti Support contact in To address\n"
        "TC_16 - Check whether Search Contact and email addresses field is working.\n"
        "TC_17 - Check the selected contact/email address is added in To/CC/BCC field\n"
        "TC_18 - Check the Remove option is working correctly after adding email address in field\n"
        "TC_19 - Check whether Attach Files icon is working perfectly and window should open\n"
        "TC_20 - Check whether file attachments are added to draft\n"
        "TC_21 - Check Remove attachment is working correctly after adding attachments\n"
        "TC_22 - Check whether proper alert message is added when user try to add more than 10 attachment\n"
        "TC_23 - Check whether the Thumbnail icon of file attachment is displaying properly\n"
        "TC_24 - Check whether Cancel upload option is working fine while uploading a file\n"
        "TC_25 - Check whether Show editor toolbar icon is displayed\n"
        "TC_26 - Check whether Show editor toolbar icon is clickable.\n"
        "TC_27 - Check whether all the action icons in toolbar are clickable - TC_28, TC_29, TC_34, TC_35 Covered.\n"
        "TC_30 - Check whether all actions are reflected in entered text -  TC_31, TC_32 and TC_33 Covered\n"
        "TC_36 - Click on Insert Image option\n"
        "TC_37 - Check whether the selected image is added to the mail body\n"
        "TC_38 - Check whether the image is clickable\n"
        "TC_39 - Check whether the resize icon is available or not\n"
        "TC_40 - Check whether the resize is working properly\n"
        "TC_41 - Check whether the delete operation is working or not\n"
        "TC_42 -  Check whether the Backspace key is working properly\n"
        "TC_43 - Check whether Insert Hyperlink is working correctly\n"
        "TC_44 - Check whether the cursor is in default position\n"
        "TC_45 - Check whether the field is allow to enter input\n"
        "TC_46 - Check whether the Enter URL field is allow to enter input\n"
        "TC_47 -  Check whether the insert button is in disabled state\n"
        "TC_48 - Check whether the Insert button turns enabled\n"
        "TC_49 - Check whether not a valid URL alert is displayed or not\n"
        "TC_50 - Check whether the preview link is displayed properly if both the fields are entered\n"
        "TC_51 - Check whether the preview link is working properly\n"
        "TC_52 - Check whether the Preview link is displayed if the text field is empty\n"
        "TC_53 - Check whether the Signature is working correctly\n"
        "TC_66 - Check the info icon for a newly signed up account\n"
    )
    def test_draftCasesBeforeMailConfigured(self):

        # global status_tc_01, status_tc_02, status_tc_03, status_tc_04, status_tc_05, status_tc_06, status_tc_08, status_tc_09

        login_email = "Triadqa4automation@yandex.com"
        login_password = "Welcome123$#@!"
        user_B_name = "Triadqa1aol Automation"
        # UserA_name = "Triadqa4Yandex Automation"
        # outlook_emailConfig = "triadqa1@outlook.com"
        # outlook_password = "Welcome123$"
        subject = "TC_13-" + random_string(3)
        test_case_number1 = "TC_001"
        test_case_number2 = "TC_002"
        test_case_number3 = "TC_003"
        # test_case_number4 = "TC_004"
        test_case_number5 = "TC_005"
        test_case_number6 = "TC_006"
        test_case_number8 = "TC_008"
        test_case_number9 = "TC_009"
        test_case_number10 = "TC_010"
        test_case_number11 = "TC_011"
        test_case_number12 = "TC_012"
        test_case_number13 = "TC_013"
        test_case_number14 = "TC_014"
        test_case_number15 = "TC_015"
        test_case_number16 = "TC_016"
        test_case_number17 = "TC_017"
        test_case_number18 = "TC_018"
        test_case_number19 = "TC_019"
        test_case_number20 = "TC_020"
        test_case_number21 = "TC_021"
        test_case_number22 = "TC_022"
        test_case_number23 = "TC_023"
        test_case_number24 = "TC_024"
        test_case_number25 = "TC_025"
        test_case_number26 = "TC_026"
        test_case_number27 = "TC_027"
        test_case_number28 = "TC_028"
        test_case_number29 = "TC_029"
        test_case_number30 = "TC_030"
        test_case_number31 = "TC_031"
        test_case_number32 = "TC_032"
        test_case_number33 = "TC_033"
        test_case_number34 = "TC_034"
        test_case_number35 = "TC_035"
        test_case_number36 = "TC_036"
        test_case_number37 = "TC_037"
        test_case_number38 = "TC_038"
        test_case_number39 = "TC_039"
        test_case_number40 = "TC_040"
        test_case_number41 = "TC_041"
        test_case_number42 = "TC_042"
        test_case_number43 = "TC_043"
        test_case_number44 = "TC_044"
        test_case_number45 = "TC_045"
        test_case_number46 = "TC_046"
        test_case_number47 = "TC_047"
        test_case_number48 = "TC_048"
        test_case_number49 = "TC_049"
        test_case_number50 = "TC_050"
        test_case_number51 = "TC_051"
        test_case_number52 = "TC_052"
        test_case_number53 = "TC_053"
        test_case_number66 = "TC_066"
        # test_case_number54 = "TC_054"
        # test_case_number55 = "TC_055"

        sheet_name = "BasicMailCases"
        self.logger.info("* Draft test case TC_01 started *")

        local_status_tc_01 = None
        local_status_tc_02 = None
        local_status_tc_03 = None
        # local_status_tc_04 = None
        local_status_tc_05 = None
        local_status_tc_06 = None
        local_status_tc_08 = None
        local_status_tc_09 = None
        local_status_tc_10 = None
        local_status_tc_11 = None
        local_status_tc_12 = None
        local_status_tc_13 = None
        local_status_tc_14 = None
        local_status_tc_15 = None
        local_status_tc_16 = None
        local_status_tc_17 = None
        local_status_tc_18 = None
        local_status_tc_19 = None
        local_status_tc_20 = None
        local_status_tc_21 = None
        local_status_tc_22 = None
        local_status_tc_23 = None
        local_status_tc_24 = None
        local_status_tc_25 = None
        local_status_tc_26 = None
        local_status_tc_27 = None
        local_status_tc_28 = None
        local_status_tc_29 = None
        local_status_tc_30 = None
        local_status_tc_31 = None
        local_status_tc_32 = None
        local_status_tc_33 = None
        local_status_tc_34 = None
        local_status_tc_35 = None
        local_status_tc_36 = None
        local_status_tc_37 = None
        local_status_tc_38 = None
        local_status_tc_39 = None
        local_status_tc_40 = None
        local_status_tc_41 = None
        local_status_tc_42 = None
        local_status_tc_43 = None
        local_status_tc_44 = None
        local_status_tc_45 = None
        local_status_tc_46 = None
        local_status_tc_47 = None
        local_status_tc_48 = None
        local_status_tc_49 = None
        local_status_tc_50 = None
        local_status_tc_51 = None
        local_status_tc_52 = None
        local_status_tc_53 = None
        local_status_tc_66 = None
        # local_status_tc_54 = None
        # local_status_tc_55 = None

        status_dict = {
            "TC_001": local_status_tc_01,
            "TC_002": local_status_tc_02,
            "TC_003": local_status_tc_03,
            # "TC_004": local_status_tc_04,
            "TC_005": local_status_tc_05,
            "TC_006": local_status_tc_06,
            "TC_008": local_status_tc_08,
            "TC_009": local_status_tc_09,
            "TC_010": local_status_tc_10,
            "TC_011": local_status_tc_11,
            "TC_012": local_status_tc_12,
            "TC_013": local_status_tc_13,
            "TC_014": local_status_tc_14,
            "TC_015": local_status_tc_15,
            "TC_016": local_status_tc_16,
            "TC_017": local_status_tc_17,
            "TC_018": local_status_tc_18,
            "TC_019": local_status_tc_19,
            "TC_020": local_status_tc_20,
            "TC_021": local_status_tc_21,
            "TC_022": local_status_tc_22,
            "TC_023": local_status_tc_23,
            "TC_024": local_status_tc_24,
            "TC_025": local_status_tc_25,
            "TC_026": local_status_tc_26,
            "TC_027": local_status_tc_27,
            "TC_028": local_status_tc_28,
            "TC_029": local_status_tc_29,
            "TC_030": local_status_tc_30,
            "TC_031": local_status_tc_31,
            "TC_032": local_status_tc_32,
            "TC_033": local_status_tc_33,
            "TC_034": local_status_tc_34,
            "TC_035": local_status_tc_35,
            "TC_036": local_status_tc_36,
            "TC_037": local_status_tc_37,
            "TC_038": local_status_tc_38,
            "TC_039": local_status_tc_39,
            "TC_040": local_status_tc_40,
            "TC_041": local_status_tc_41,
            "TC_042": local_status_tc_42,
            "TC_043": local_status_tc_43,
            "TC_044": local_status_tc_44,
            "TC_045": local_status_tc_45,
            "TC_046": local_status_tc_46,
            "TC_047": local_status_tc_47,
            "TC_048": local_status_tc_48,
            "TC_049": local_status_tc_49,
            "TC_050": local_status_tc_50,
            "TC_051": local_status_tc_51,
            "TC_052": local_status_tc_52,
            "TC_053": local_status_tc_53,
            "TC_066": local_status_tc_66
        }

        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                time.sleep(1)

            # TC 1
            print("Running Mail Draft TC 01")
            with allure.step("TC_1 - Verify Mail tab and Bring Mails are Present in SIGNIN Case"):
                # time.sleep(10)
                self.mailPage.verify_mail_tab_exists()
                time.sleep(0.5)
                Check = self.mailPage.verify_bring_mails_exists()
                if Check:
                    local_status_tc_01 = True
                    status_dict["TC_001"] = local_status_tc_01

            # TC 2
            print("Running Mail Draft TC 02")
            with allure.step("TC_2 - Verify Mail tab is clickable"):
                self.mailPage.click_mails_tab()
                time.sleep(1)
                Check = self.mailPage.verify_mail_tab_opened()
                if Check:
                    local_status_tc_02 = True
                    status_dict["TC_002"] = local_status_tc_02

            # TC 3
            print("Running Mail Draft TC 03")
            with allure.step("TC_3 - Verify Bring Mails tab is clickable"):
                Check = self.mailPage.verify_bring_mail_clicked()
                if Check:
                    local_status_tc_03 = True
                    status_dict["TC_003"] = local_status_tc_03

            # TC 4
            # with allure.step("TC_4 - Configure Email Address and Verify configured email address in overlay"):
            #     Check = self.mailPage.configure_outlook_bring_mails(outlook_emailConfig, outlook_password)
            #     if Check:
            #         time.sleep(1)
            #         Check1 = self.mailPage.verify_bring_mails_header_text(outlook_emailConfig)
            #         if Check1:
            #             time.sleep(1)
            #             self.mailPage.close_overlay()
            #             local_status_tc_04 = True
            #             status_dict["TC_004"] = local_status_tc_04

            # TC 5
            print("Running Mail Draft TC 05")
            with allure.step("TC_5 - Verify Compose Mail Option available in Conversation tab for Fresh Accounts."):
                self.homePage.click_home_tab()
                time.sleep(1)
                Check = self.homePage.verify_compose_mail_button("conversations")
                if Check:
                    local_status_tc_05 = True
                    status_dict["TC_005"] = local_status_tc_05

            # TC 6
            print("Running Mail Draft TC 06")
            with allure.step(
                    "TC_6 - Verify Compose Mail Option available in Mails tab for Fresh Accounts Before Configure Email Id."):
                self.mailPage.click_mails_tab()
                time.sleep(1)
                Check = self.homePage.verify_compose_mail_button("mail")
                if Check:
                    local_status_tc_06 = True
                    status_dict["TC_006"] = local_status_tc_06

            # TC 8
            print("Running Mail Draft TC 08")
            with allure.step(
                    "TC_8 - Verify Draft Formed after clicking Compose Mail Option Before Configure Email Id."):
                self.mailDraftPage.click_compose_mail_button()
                Check = self.mailDraftPage.verify_draft_opened()
                if Check:
                    local_status_tc_08 = True
                    status_dict["TC_008"] = local_status_tc_08
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 9
            print("Running Mail Draft TC 09")
            with allure.step("TC_9 - Verify Draft Text , No subject text and Mail draft icon in Opened Draft"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_draft_subject_text_context_area()
                if Check:
                    local_status_tc_09 = True
                    status_dict["TC_009"] = local_status_tc_09
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 10
            print("Running Mail Draft TC 10")
            with allure.step("TC_10 - Verify New Mail text in Mail Draft header in Opened Draft"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_draft_header_text()
                if Check:
                    local_status_tc_10 = True
                    status_dict["TC_010"] = local_status_tc_10
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 11
            print("Running Mail Draft TC 11")
            with allure.step("TC_11 - Verify Cursor is focused in subject Field"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_cursor_active_subject()
                if Check:
                    local_status_tc_11 = True
                    status_dict["TC_011"] = local_status_tc_11
                    time.sleep(1)

            # TC 12
            print("Running Mail Draft TC 12")
            with allure.step("TC_12 - Verify subject Field PlaceHolder "):
                Check = self.mailDraftPage.verify_subject_placeholder_text()
                if Check:
                    local_status_tc_12 = True
                    status_dict["TC_012"] = local_status_tc_12
                    # self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 13
            print("Running Mail Draft TC 13")
            with allure.step(
                    "TC_13 - Verify Able to enter in subject Field and Entered Name updated in contexts area Draft "):
                Check = self.mailDraftPage.enter_subject_and_verify_contexts_area(subject)
                if Check:
                    local_status_tc_13 = True
                    status_dict["TC_013"] = local_status_tc_13
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 14
            print("Running Mail Draft TC 14")
            with allure.step(
                    "TC_14 - Verify Able to Click + icon in To field and Verify Add participant to To window appears "):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_add_participant_dialog(field="To")
                if Check:
                    local_status_tc_14 = True
                    status_dict["TC_014"] = local_status_tc_14
                    self.mailPage.close_overlay()
                    time.sleep(0.5)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 15
            print("Running Mail Draft TC 15")
            with allure.step(
                    "TC_15 - Verify Upgrade Alert appears while adding Clariti Support contact from Add contact Dialog in Draft"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_add_participant_dialog("To")
                time.sleep(2)
                # self.contactsPage.contact_selection_dialog("Clariti Support")
                Check = self.contactsPage.select_add_contact_from_overlay("Clariti Support")
                time.sleep(1)
                if Check:
                    local_status_tc_15 = True
                    status_dict["TC_015"] = local_status_tc_15
                    self.mailDraftPage.close_upgrade_dialog()
                    time.sleep(1)
                    self.mailPage.close_overlay()
                    time.sleep(0.5)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 16
            print("Running Mail Draft TC 16")
            with allure.step("TC_16 - Verify Search Contact and email addresses field is working"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_add_participant_dialog("To")
                time.sleep(1)
                Check = self.mailDraftPage.verify_search_contact_results_add_participant(user_B_name)
                if Check:
                    local_status_tc_16 = True
                    status_dict["TC_016"] = local_status_tc_16
                    self.mailPage.close_overlay()
                    time.sleep(1)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 17
            print("Running Mail Draft TC 17")
            with allure.step("TC_17 - Verify the selected contact/email address is added in To/CC/BCC field"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_add_participant_dialog("To")
                time.sleep(1)
                self.mailDraftPage.enter_search_contact_results_add_participant(user_B_name)
                self.contactsPage.select_add_contact_from_overlay(user_B_name)
                time.sleep(1)
                Check = self.mailDraftPage.verify_contact_name_added_field(user_B_name)
                if Check:
                    local_status_tc_17 = True
                    status_dict["TC_017"] = local_status_tc_17
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 18
            print("Running Mail Draft TC 18")
            with allure.step("TC_18 - Verify the added contact able to remove"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_add_participant_dialog("To")
                time.sleep(1)
                self.mailDraftPage.enter_search_contact_results_add_participant(user_B_name)
                self.contactsPage.select_add_contact_from_overlay(user_B_name)
                time.sleep(1)
                self.mailDraftPage.verify_contact_name_added_field(user_B_name)
                time.sleep(1)
                Check = self.mailDraftPage.remove_added_contact()
                if Check:
                    local_status_tc_18 = True
                    status_dict["TC_018"] = local_status_tc_18
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 19
            print("Running Mail Draft TC 19")
            with allure.step(
                    "TC_19 - Verify Attach Files icon is working perfectly, Attach Files window should open verify by Screenshot"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_file_explorer_opened()
                time.sleep(1)
                if Check:
                    local_status_tc_19 = True
                    status_dict["TC_019"] = local_status_tc_19
                    close_file_explorer()
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)
            # TC 20
            print("Running Mail Draft TC 20")
            with allure.step("TC_20 - Verify file attachments are added to draft."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.verify_file_explorer_opened()
                upload_files("one", "ClaritiReport.html", "")
                time.sleep(2)
                Check = self.mailDraftPage.verify_file_attachment_added()
                if Check:
                    local_status_tc_20 = True
                    status_dict["TC_020"] = local_status_tc_20
                    close_file_explorer()
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 21
            print("Running Mail Draft TC 21")
            with allure.step("TC_21 - Verify Attached Files are Removed Successfully"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.verify_file_explorer_opened()
                upload_files("one", "ClaritiReport.html", "")
                time.sleep(1)
                Check = self.mailDraftPage.remove_file_attachment("ClaritiReport.html")
                if Check:
                    local_status_tc_21 = True
                    status_dict["TC_021"] = local_status_tc_21
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 22
            print("Running Mail Draft TC 22")
            with allure.step(
                    "TC_22 - Verify proper alert message is added when user try to add more than 10 attachment."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.verify_file_explorer_opened()
                upload_files("many", "", "mail")
                Check = self.mailDraftPage.verify_max_10_files_alert()
                if Check:
                    local_status_tc_22 = True
                    status_dict["TC_022"] = local_status_tc_22
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 23
            print("Running Mail Draft TC 23")
            with allure.step("TC_23 - Verify Thumbnail icon of file attachment is displaying properly."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.verify_file_explorer_opened()
                upload_files("one", "ClaritiReport.html", "")
                time.sleep(1)
                Check = self.mailDraftPage.verify_file_attachment_added_icons()
                if Check:
                    local_status_tc_23 = True
                    status_dict["TC_023"] = local_status_tc_23
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 24
            print("Running Mail Draft TC 24")
            with allure.step("TC_24 - Verify Cancel upload option is working fine."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.verify_file_explorer_opened()
                upload_files("one", "Sample15mbfile.pdf", "")
                time.sleep(1)
                Check = self.mailDraftPage.cancel_uploading_files()
                if Check:
                    local_status_tc_24 = True
                    status_dict["TC_024"] = local_status_tc_24
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 25
            print("Running Mail Draft TC 25")
            with allure.step("TC_25 - Verify Show editor toolbar icon appears or not"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_show_editor_toolbar_displayed()
                if Check:
                    local_status_tc_25 = True
                    status_dict["TC_025"] = local_status_tc_25
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 26
            print("Running Mail Draft TC 26")
            with allure.step("TC_26 - Verify Show editor toolbar icon is clickable and Editor should opened"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_editor_toolbar_opened()
                if Check:
                    local_status_tc_26 = True
                    status_dict["TC_026"] = local_status_tc_26
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 27 Covered TC 28 and 29
            print("Running Mail Draft TC 27")
            with allure.step(
                    "TC_27, TC_28, TC_29, TC_34, TC_35 - Verify All Editor Toolbar Button is Hovered and Clickable"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.verify_editor_toolbar_opened()
                Check = self.mailDraftPage.verify_all_editor_action_hover_clickable()
                if Check:
                    local_status_tc_27 = True
                    local_status_tc_28 = True
                    local_status_tc_29 = True
                    local_status_tc_34 = True
                    local_status_tc_35 = True
                    status_dict["TC_027"] = local_status_tc_27
                    status_dict["TC_028"] = local_status_tc_28
                    status_dict["TC_029"] = local_status_tc_29
                    status_dict["TC_034"] = local_status_tc_34
                    status_dict["TC_035"] = local_status_tc_35

                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 30 Covered TC 31 TC 32 and TC 33
            print("Running Mail Draft TC 30")
            with allure.step("TC_30, TC_31, TC_32, TC_33  - Verify Styles are reflected in entered text from toolbar"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(2)
                self.mailDraftPage.enter_body_content("draft_message")
                Check1 = self.mailDraftPage.verify_body_draft_text_style_bold()
                self.mailDraftPage.click_disable_bold()
                time.sleep(1)
                Check2 = self.mailDraftPage.verify_body_draft_text_style_italic()
                self.mailDraftPage.click_disable_italic()
                time.sleep(1)
                Check3 = self.mailDraftPage.verify_body_draft_text_style_strike_through()
                self.mailDraftPage.click_disable_strike()
                time.sleep(1)
                Check4 = self.mailDraftPage.verify_body_draft_text_style_under_line()
                self.mailDraftPage.click_disable_under_line()
                time.sleep(1)
                Check5 = self.mailDraftPage.verify_body_draft_text_style_bullet_list()
                self.mailDraftPage.click_disable_bullet_list()
                time.sleep(1)
                Check6 = self.mailDraftPage.verify_body_draft_text_style_numbered_list()
                self.mailDraftPage.click_disable_numbered_list()
                time.sleep(1)
                Check7 = self.mailDraftPage.verify_body_draft_text_style_indent()
                time.sleep(1)
                Check8 = self.mailDraftPage.verify_body_draft_text_style_reduce_indent()
                time.sleep(1)
                Check9 = self.mailDraftPage.verify_body_draft_text_style_center()
                time.sleep(1)
                Check10 = self.mailDraftPage.verify_body_draft_text_style_right()
                time.sleep(1)
                Check11 = self.mailDraftPage.verify_body_draft_text_style_left()
                time.sleep(1)
                Check12 = self.mailDraftPage.verify_body_draft_text_style_colour()
                time.sleep(1)
                if Check1 and Check2 and Check3 and Check4 and Check5 and Check6 and Check7 and Check8 and Check9 and Check10 and Check11 and Check12:
                    local_status_tc_30 = True
                    local_status_tc_31 = True
                    local_status_tc_32 = True
                    local_status_tc_33 = True
                    status_dict["TC_030"] = local_status_tc_30
                    status_dict["TC_031"] = local_status_tc_31
                    status_dict["TC_032"] = local_status_tc_32
                    status_dict["TC_033"] = local_status_tc_33
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            # TC 36, TC 37 and TC 38
            print("Running Mail Draft TC 36")
            with allure.step(
                    "TC_36,TC_37, TC_38 - Verify Click on Insert Image option and Check whether the selected image is added to the mail body and verify its clickable and focused"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_insert_image_in_draft()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_insert_image_is_clickable()
                if Check and Check1:
                    local_status_tc_36 = True
                    local_status_tc_37 = True
                    local_status_tc_38 = True
                    status_dict["TC_036"] = local_status_tc_36
                    status_dict["TC_037"] = local_status_tc_37
                    status_dict["TC_038"] = local_status_tc_38
                    time.sleep(1)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 39 and TC 40
            print("Running Mail Draft TC 40")
            with allure.step("TC_39, TC_40 - Verify Inline Image is resized or not"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_resize_insert_image_in_draft()
                if Check:
                    local_status_tc_40 = True
                    local_status_tc_39 = True
                    status_dict["TC_039"] = local_status_tc_39
                    status_dict["TC_040"] = local_status_tc_40
                    time.sleep(1)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 41
            print("Running Mail Draft TC 41")
            with allure.step(
                    "TC_41 - Verify delete operation is working or not in Inline Image and Inline should not deleted."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_delete_backspace_operation_inline_image("delete")
                if Check:
                    local_status_tc_41 = True
                    status_dict["TC_041"] = local_status_tc_41
                    time.sleep(1)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 42
            print("Running Mail Draft TC 42")
            with allure.step(
                    "TC_42 - Verify backspace operation is working or not in Inline Image and Inline should be deleted."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_delete_backspace_operation_inline_image("backspace")
                if Check:
                    local_status_tc_42 = True
                    status_dict["TC_042"] = local_status_tc_42
                    time.sleep(1)
                    self.mailDraftPage.close_mail_draft()
                    time.sleep(1)

            # TC 49
            print("Running Mail Draft TC 49")
            with allure.step("TC_49 - Verify Not a valid alert appears or not"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                self.mailDraftPage.verify_hyperlink_dialog_opened()
                time.sleep(0.5)
                self.mailDraftPage.enter_hyperlink_url("clarit")
                time.sleep(0.5)
                Check = self.mailDraftPage.verify_not_a_valid_url_alert()
                if Check:
                    local_status_tc_49 = True
                    status_dict["TC_049"] = local_status_tc_49
                    time.sleep(1)
                self.mailDraftPage.click_close_icon_hyperlink()
                time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            # TC 43, TC 44, TC 45, TC 46, TC 47, TC_48, TC 50
            print("Running Mail Draft TC 43 to 50")
            with allure.step(
                    "TC_50 - Verify Hyperlink dialog opened and Text to be displayed focused, Able to enter in Text and Url field and Insert Button is in Enabled state."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_hyperlink_dialog_opened()
                time.sleep(0.5)
                Check2 = self.mailDraftPage.verify_insert_button_disabled()
                time.sleep(0.5)
                Check3 = self.mailDraftPage.verify_hyperlink_dialog_Text_to_be_displayed_textbox_focused()
                time.sleep(0.5)
                Check4 = self.mailDraftPage.verify_hyperlink_text_to_be_displayed("URL Hyperlink Text")
                time.sleep(0.5)
                Check5 = self.mailDraftPage.verify_hyperlink_url("https://clariti.app/")
                time.sleep(0.5)
                Check6 = self.mailDraftPage.verify_insert_button_enabled()
                time.sleep(0.5)
                Check7 = self.mailDraftPage.verify_hyperlink_preview_text()
                time.sleep(1)
                if Check1 and Check2 and Check3 and Check4 and Check5 and Check6 and Check7:
                    local_status_tc_43 = True
                    local_status_tc_44 = True
                    local_status_tc_45 = True
                    local_status_tc_46 = True
                    local_status_tc_47 = True
                    local_status_tc_48 = True
                    local_status_tc_50 = True
                    status_dict["TC_043"] = local_status_tc_43
                    status_dict["TC_044"] = local_status_tc_44
                    status_dict["TC_045"] = local_status_tc_45
                    status_dict["TC_046"] = local_status_tc_46
                    status_dict["TC_047"] = local_status_tc_47
                    status_dict["TC_048"] = local_status_tc_48
                    status_dict["TC_050"] = local_status_tc_50
                    time.sleep(1)
                self.mailDraftPage.click_close_icon_hyperlink()
                time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(2)

            print("Running Mail Draft TC 51")
            with allure.step("TC_51 - Verify whether the preview link is working properly."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_hyperlink_dialog_opened()
                time.sleep(0.5)
                Check2 = self.mailDraftPage.verify_hyperlink_text_to_be_displayed("Clariti Website Page")
                time.sleep(0.5)
                Check3 = self.mailDraftPage.verify_hyperlink_url("https://clariti.app/")
                time.sleep(1)
                Check4 = self.mailDraftPage.verify_hyperlink_clicked_new_tab()
                time.sleep(1)
                if Check1 and Check2 and Check3 and Check4:
                    local_status_tc_51 = True
                    status_dict["TC_051"] = local_status_tc_51
                    time.sleep(1)
                self.mailDraftPage.click_close_icon_hyperlink()
                time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 52")
            with allure.step(
                    "TC_52 - Verify whether the Preview link is displayed if the text field is empty and link should work"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_hyperlink_dialog_opened()
                time.sleep(0.5)
                Check2 = self.mailDraftPage.verify_hyperlink_text_to_be_displayed("Clariti Website Page")
                time.sleep(0.5)
                Check3 = self.mailDraftPage.verify_hyperlink_url("https://clariti.app/")
                time.sleep(1)
                Check4 = self.mailDraftPage.clear_entered_text_text_to_be_displayed()
                time.sleep(1)
                Check5 = self.mailDraftPage.verify_hyperlink_preview_text()
                time.sleep(1)
                Check6 = self.mailDraftPage.verify_hyperlink_clicked_new_tab()
                time.sleep(1)
                if Check1 and Check2 and Check3 and Check4 and Check5 and Check6:
                    local_status_tc_52 = True
                    status_dict["TC_052"] = local_status_tc_52
                    time.sleep(1)
                self.mailDraftPage.click_close_icon_hyperlink()
                time.sleep(1)
                self.mailDraftPage.close_mail_draft()

            print("Running Mail Draft TC 53")
            with allure.step("TC_53 - Verify Signature is working correctly and window should open."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_signature_dialog_opened()
                time.sleep(1)
                if Check:
                    local_status_tc_53 = True
                    status_dict["TC_053"] = local_status_tc_53
                    time.sleep(1)
                self.mailDraftPage.click_close_icon_hyperlink()
                time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            # TC 66
            print("Running Mail Draft TC 66")
            with allure.step("TC_66 - Verify send Mail enabled with Premium subscription alert"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_send_mail_enabled_with_premium()
                if Check:
                    local_status_tc_66 = True
                    status_dict["TC_066"] = local_status_tc_66
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()

        finally:
            with allure.step("Each Case Status"):
                verify_status(test_case_number1, local_status_tc_01)
                verify_status(test_case_number2, local_status_tc_02)
                verify_status(test_case_number3, local_status_tc_03)
                # verify_status(test_case_number4, local_status_tc_04)
                verify_status(test_case_number5, local_status_tc_05)
                verify_status(test_case_number6, local_status_tc_06)
                verify_status(test_case_number8, local_status_tc_08)
                verify_status(test_case_number9, local_status_tc_09)
                verify_status(test_case_number10, local_status_tc_10)
                verify_status(test_case_number11, local_status_tc_11)
                verify_status(test_case_number12, local_status_tc_12)
                verify_status(test_case_number13, local_status_tc_13)
                verify_status(test_case_number14, local_status_tc_14)
                verify_status(test_case_number15, local_status_tc_15)
                verify_status(test_case_number16, local_status_tc_16)
                verify_status(test_case_number17, local_status_tc_17)
                verify_status(test_case_number18, local_status_tc_18)
                verify_status(test_case_number19, local_status_tc_19)
                verify_status(test_case_number20, local_status_tc_20)
                verify_status(test_case_number21, local_status_tc_21)
                verify_status(test_case_number22, local_status_tc_22)
                verify_status(test_case_number23, local_status_tc_23)
                verify_status(test_case_number24, local_status_tc_24)
                verify_status(test_case_number25, local_status_tc_25)
                verify_status(test_case_number26, local_status_tc_26)
                verify_status(test_case_number27, local_status_tc_27)
                verify_status(test_case_number28, local_status_tc_28)
                verify_status(test_case_number29, local_status_tc_29)
                verify_status(test_case_number30, local_status_tc_30)
                verify_status(test_case_number31, local_status_tc_31)
                verify_status(test_case_number32, local_status_tc_32)
                verify_status(test_case_number33, local_status_tc_33)
                verify_status(test_case_number34, local_status_tc_34)
                verify_status(test_case_number35, local_status_tc_35)
                verify_status(test_case_number36, local_status_tc_36)
                verify_status(test_case_number37, local_status_tc_37)
                verify_status(test_case_number38, local_status_tc_38)
                verify_status(test_case_number39, local_status_tc_39)
                verify_status(test_case_number40, local_status_tc_40)
                verify_status(test_case_number41, local_status_tc_41)
                verify_status(test_case_number42, local_status_tc_42)
                verify_status(test_case_number43, local_status_tc_43)
                verify_status(test_case_number44, local_status_tc_44)
                verify_status(test_case_number45, local_status_tc_45)
                verify_status(test_case_number46, local_status_tc_46)
                verify_status(test_case_number47, local_status_tc_47)
                verify_status(test_case_number48, local_status_tc_48)
                verify_status(test_case_number49, local_status_tc_49)
                verify_status(test_case_number50, local_status_tc_50)
                verify_status(test_case_number51, local_status_tc_51)
                verify_status(test_case_number52, local_status_tc_52)
                verify_status(test_case_number52, local_status_tc_53)
                verify_status(test_case_number66, local_status_tc_66)
                status_report_update_to_xls(sheet_name, local_status_tc_01, test_case_number1)
                status_report_update_to_xls(sheet_name, local_status_tc_02, test_case_number2)
                status_report_update_to_xls(sheet_name, local_status_tc_03, test_case_number3)
                # status_report_update_to_xls(sheet_name, local_status_04, test_case_number4)
                status_report_update_to_xls(sheet_name, local_status_tc_05, test_case_number5)
                status_report_update_to_xls(sheet_name, local_status_tc_06, test_case_number6)
                status_report_update_to_xls(sheet_name, local_status_tc_08, test_case_number8)
                status_report_update_to_xls(sheet_name, local_status_tc_09, test_case_number9)
                status_report_update_to_xls(sheet_name, local_status_tc_10, test_case_number10)
                status_report_update_to_xls(sheet_name, local_status_tc_11, test_case_number11)
                status_report_update_to_xls(sheet_name, local_status_tc_12, test_case_number12)
                status_report_update_to_xls(sheet_name, local_status_tc_13, test_case_number13)
                status_report_update_to_xls(sheet_name, local_status_tc_14, test_case_number14)
                status_report_update_to_xls(sheet_name, local_status_tc_15, test_case_number15)
                status_report_update_to_xls(sheet_name, local_status_tc_16, test_case_number16)
                status_report_update_to_xls(sheet_name, local_status_tc_17, test_case_number17)
                status_report_update_to_xls(sheet_name, local_status_tc_18, test_case_number18)
                status_report_update_to_xls(sheet_name, local_status_tc_19, test_case_number19)
                status_report_update_to_xls(sheet_name, local_status_tc_20, test_case_number20)
                status_report_update_to_xls(sheet_name, local_status_tc_21, test_case_number21)
                status_report_update_to_xls(sheet_name, local_status_tc_22, test_case_number22)
                status_report_update_to_xls(sheet_name, local_status_tc_23, test_case_number23)
                status_report_update_to_xls(sheet_name, local_status_tc_24, test_case_number24)
                status_report_update_to_xls(sheet_name, local_status_tc_25, test_case_number25)
                status_report_update_to_xls(sheet_name, local_status_tc_26, test_case_number26)
                status_report_update_to_xls(sheet_name, local_status_tc_27, test_case_number27)
                status_report_update_to_xls(sheet_name, local_status_tc_28, test_case_number28)
                status_report_update_to_xls(sheet_name, local_status_tc_29, test_case_number29)
                status_report_update_to_xls(sheet_name, local_status_tc_30, test_case_number30)
                status_report_update_to_xls(sheet_name, local_status_tc_31, test_case_number31)
                status_report_update_to_xls(sheet_name, local_status_tc_32, test_case_number32)
                status_report_update_to_xls(sheet_name, local_status_tc_33, test_case_number33)
                status_report_update_to_xls(sheet_name, local_status_tc_34, test_case_number34)
                status_report_update_to_xls(sheet_name, local_status_tc_35, test_case_number35)
                status_report_update_to_xls(sheet_name, local_status_tc_36, test_case_number36)
                status_report_update_to_xls(sheet_name, local_status_tc_37, test_case_number37)
                status_report_update_to_xls(sheet_name, local_status_tc_38, test_case_number38)
                status_report_update_to_xls(sheet_name, local_status_tc_39, test_case_number39)
                status_report_update_to_xls(sheet_name, local_status_tc_40, test_case_number40)
                status_report_update_to_xls(sheet_name, local_status_tc_41, test_case_number41)
                status_report_update_to_xls(sheet_name, local_status_tc_42, test_case_number42)
                status_report_update_to_xls(sheet_name, local_status_tc_43, test_case_number43)
                status_report_update_to_xls(sheet_name, local_status_tc_44, test_case_number44)
                status_report_update_to_xls(sheet_name, local_status_tc_45, test_case_number45)
                status_report_update_to_xls(sheet_name, local_status_tc_46, test_case_number46)
                status_report_update_to_xls(sheet_name, local_status_tc_47, test_case_number47)
                status_report_update_to_xls(sheet_name, local_status_tc_48, test_case_number48)
                status_report_update_to_xls(sheet_name, local_status_tc_49, test_case_number49)
                status_report_update_to_xls(sheet_name, local_status_tc_50, test_case_number50)
                status_report_update_to_xls(sheet_name, local_status_tc_51, test_case_number51)
                status_report_update_to_xls(sheet_name, local_status_tc_52, test_case_number52)
                status_report_update_to_xls(sheet_name, local_status_tc_53, test_case_number53)
                status_report_update_to_xls(sheet_name, local_status_tc_66, test_case_number66)

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

        self.logger.info("* Draft test case TC_01 Ended *")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_07 - Check whether Compose Mail option is available in Mail tab or not, after configure email address\n"
        "TC_54 - Check whether the Signature is working correctly\n"
        "TC_55 - Check whether Add this signature to all mails is checked by default.\n"
        "TC_56 - Check whether it is able to uncheck.\n"
        "TC_57 - Check whether the Apply button is working properly\n"
        "TC_58 - Check whether the newly added signature is displayed in mail draft.\n"
        "TC_59 - Click on three dots in Insert Signature window and 2 options should appear\n"
        "TC_60 - Check whether the Close button is displayed and working properly\n"
        "TC_61 - Check whether Reply to is working properly\n"
        "TC_62 - Check whether cursor focus is default.\n"
        "TC_63 - Check whether the Save button is in disabled state\n"
        "TC_64 - Check whether the proper validation is done for email address\n"
        "TC_65 - Check whether the proper validation is done for email address and Added address should display in right side bottom corner\n"
        "TC_69 - Check whether the info icon is displayed after configure email address\n"
        "TC_70 - Check whether the Subject is empty info dis-appeared after enter the subject name\n"
        "TC_71 - Check the info icon gets disappeared after added recipient\n"
        "TC_72 - Check whether the Send button is in disabled state while info icon is displayed\n"
        "TC_73 - Check whether the mail will be sent using is displayed after configure more than 1 email address\n"
        "TC_74 - Check whether it gets disappeared after remove the additional configured emails\n"
        "TC_75 - Check whether the drop-down is working in mail will be sent using option\n"
        "TC_76 - Check whether drop-down configured email is selectable\n"
        "TC_77 - Check whether the draft is opening as an overlay\n"
        "TC_78 - Check whether the pop-out icon is working properly\n"
        "TC_79 - Check whether the email draft is discarded from the overlay\n"
        "TC_80 - Check whether the mail draft overlay is retained after shifting tabs\n"

    )
    def test_draftCasesAfterMailConfigured(self):

        # global status_tc_07, status_tc_02, status_tc_03, status_tc_04, status_tc_05, status_tc_06, status_tc_08, status_tc_09

        login_email = "triadqa6@yandex.com"
        login_password = "Welcome123$#@!"
        # UserA_name = "Triadqa6Yandex Automation"
        subject = "For TC_77_80- " + random_string(3)
        subject1 = "For TC_78- " + random_string(3)
        User_B_email = "triadqa3@gmail.com"
        message = "Sample Mail to create a conversation"
        user_B_name = "Triadqa1aol Automation"
        # test_case_number4 = "TC_004"
        test_case_number7 = "TC_007"
        test_case_number54 = "TC_054"
        test_case_number55 = "TC_055"
        test_case_number56 = "TC_056"
        test_case_number57 = "TC_057"
        test_case_number58 = "TC_058"
        test_case_number59 = "TC_059"
        test_case_number60 = "TC_060"
        test_case_number61 = "TC_061"
        test_case_number62 = "TC_062"
        test_case_number63 = "TC_063"
        test_case_number64 = "TC_064"
        test_case_number65 = "TC_065"
        test_case_number69 = "TC_069"
        test_case_number70 = "TC_070"
        test_case_number71 = "TC_071"
        test_case_number72 = "TC_072"
        test_case_number73 = "TC_073"
        test_case_number74 = "TC_074"
        test_case_number75 = "TC_075"
        test_case_number76 = "TC_076"
        test_case_number77 = "TC_077"
        test_case_number78 = "TC_078"
        test_case_number79 = "TC_079"
        test_case_number80 = "TC_080"

        sheet_name = "BasicMailCases"
        self.logger.info("* Draft test case TC_01 started *")

        # local_status_tc_04 = None
        local_status_tc_07 = None
        local_status_tc_54 = None
        local_status_tc_55 = None
        local_status_tc_56 = None
        local_status_tc_57 = None
        local_status_tc_58 = None
        local_status_tc_59 = None
        local_status_tc_60 = None
        local_status_tc_61 = None
        local_status_tc_62 = None
        local_status_tc_63 = None
        local_status_tc_64 = None
        local_status_tc_65 = None
        local_status_tc_69 = None
        local_status_tc_70 = None
        local_status_tc_71 = None
        local_status_tc_72 = None
        local_status_tc_73 = None
        local_status_tc_74 = None
        local_status_tc_75 = None
        local_status_tc_76 = None
        local_status_tc_77 = None
        local_status_tc_78 = None
        local_status_tc_79 = None
        local_status_tc_80 = None

        status_dict = {
            # "TC_004": local_status_tc_04,
            "TC_007": local_status_tc_07,
            "TC_054": local_status_tc_54,
            "TC_055": local_status_tc_55,
            "TC_056": local_status_tc_56,
            "TC_057": local_status_tc_57,
            "TC_058": local_status_tc_58,
            "TC_059": local_status_tc_59,
            "TC_060": local_status_tc_60,
            "TC_061": local_status_tc_61,
            "TC_062": local_status_tc_62,
            "TC_063": local_status_tc_63,
            "TC_064": local_status_tc_64,
            "TC_065": local_status_tc_65,
            "TC_069": local_status_tc_69,
            "TC_070": local_status_tc_70,
            "TC_071": local_status_tc_71,
            "TC_072": local_status_tc_72,
            "TC_073": local_status_tc_73,
            "TC_074": local_status_tc_74,
            "TC_075": local_status_tc_75,
            "TC_076": local_status_tc_76,
            "TC_077": local_status_tc_77,
            "TC_078": local_status_tc_78,
            "TC_079": local_status_tc_79,
            "TC_080": local_status_tc_80
        }

        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                time.sleep(1)

            # TC 4
            # print("Running Mail Draft TC 04")
            # with allure.step(
            #         "TC_4 - Verify configured email id is showing in Bring Mails Overlay,."):
            #     Check = self.mailPage.verify_configured_email_listed_in_bring_mails()
            #     time.sleep(1)
            #     if Check:
            #         local_status_tc_04 = True
            #         status_dict["TC_004"] = local_status_tc_04
            #         self.mailPage.close_overlay()
            #         time.sleep(1)
            # TC 7
            print("Running Mail Draft TC 07")
            with allure.step(
                    "TC_7 - Verify Compose Mail Option available in Mails tab for Fresh Accounts After Configure Email Id."):
                self.mailPage.click_mails_tab()
                time.sleep(1)
                Check = self.homePage.verify_compose_mail_button("mail")
                if Check:
                    local_status_tc_07 = True
                    status_dict["TC_007"] = local_status_tc_07

            print("Running Mail Draft TC 54 to 57")
            with allure.step(
                    "TC_54, TC_55, TC_56, TC_57 - Verify the default signature is displayed or not.. and verify checkbox selection and Apply Button"):
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_default_signature()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_add_this_signature_for_all_mails_enabled()
                time.sleep(1)
                Check2 = self.mailDraftPage.verify_add_this_signature_for_all_mails_uncheck()
                time.sleep(1)
                Check3 = self.mailDraftPage.verify_signature_dialog_closed_apply()
                time.sleep(1)
                if Check and Check1 and Check2 and Check3:
                    local_status_tc_54 = True
                    local_status_tc_55 = True
                    local_status_tc_56 = True
                    local_status_tc_57 = True
                    status_dict["TC_054"] = local_status_tc_54
                    status_dict["TC_055"] = local_status_tc_55
                    status_dict["TC_056"] = local_status_tc_56
                    status_dict["TC_057"] = local_status_tc_57
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 58")
            with allure.step("TC_58 - Verify  the newly added signature is displayed in mail draft"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                self.mailDraftPage.click_editor_signature()
                time.sleep(1)
                Check = self.mailDraftPage.change_default_signature_and_verify()
                time.sleep(1)
                if Check:
                    local_status_tc_58 = True
                    status_dict["TC_058"] = local_status_tc_58
                    time.sleep(1)

                    # Current code until Issue FIX
                    self.mailDraftPage.click_editor_signature()
                    time.sleep(1)
                    self.mailDraftPage.clear_unwanted_signature()
                    self.mailDraftPage.click_Apply_button_signature()
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 59, 60")
            with allure.step(
                    "TC_59 , TC_60 - Verify the Insert Image and Hyperlink Option are showing under More from Signature Dialog and CLose Button is working or not"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                self.mailDraftPage.click_editor_signature()
                time.sleep(1)
                Check = self.mailDraftPage.verify_more_actions_in_signature_dialog()
                time.sleep(1)
                if Check:
                    local_status_tc_59 = True
                    status_dict["TC_059"] = local_status_tc_59
                    time.sleep(0.5)
                    self.mailDraftPage.click_close_icon_hyperlink()
                    screenshot_and_attach_report_pyautogui("SignatureDialogClosed", "Verify Signature Dialog Closed")
                    local_status_tc_60 = True
                    status_dict["TC_060"] = local_status_tc_60
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 61 to 64")
            with allure.step(
                    "TC_61, TC_62, TC_63, TC_64 - Verify the Reply To dialog opened and cursor focused and save button is in disabled and enter valid email address alert.."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_reply_to_dialog_opened()
                time.sleep(1)
                Check2 = self.mailDraftPage.verify_hyperlink_dialog_Text_to_be_displayed_textbox_focused()
                time.sleep(1)
                Check3 = self.mailDraftPage.verify_insert_button_disabled()
                time.sleep(1)
                Check4 = self.mailDraftPage.verify_enter_valid_email_address_alert_reply_to()
                time.sleep(1)
                if Check1 and Check2 and Check3 and Check4:
                    local_status_tc_61 = True
                    local_status_tc_62 = True
                    local_status_tc_63 = True
                    local_status_tc_64 = True
                    status_dict["TC_061"] = local_status_tc_61
                    status_dict["TC_062"] = local_status_tc_62
                    status_dict["TC_063"] = local_status_tc_63
                    status_dict["TC_064"] = local_status_tc_64
                    time.sleep(1)
                    self.mailDraftPage.click_close_icon_hyperlink()
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 65")
            with allure.step("TC_65 - Verify the reply to email added in draft in right bottom.."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                self.mailDraftPage.click_reply_to_option()
                time.sleep(1)
                Check = self.mailDraftPage.verify_reply_for_this_email_sent_to_email("triadqa1@outlook.com")
                time.sleep(1)
                if Check:
                    local_status_tc_65 = True
                    status_dict["TC_065"] = local_status_tc_65
                    time.sleep(0.5)
                    self.mailDraftPage.click_reply_to_option()
                    time.sleep(0.5)
                    self.mailDraftPage.clear_reply_to_email()
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            # TC 69
            print("Running Mail Draft TC 69")
            with allure.step(
                    "TC_69 - Verify the info icon is displayed after configure email address and At least one recipient is required & Subject is empty info should appear"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                Check = self.mailDraftPage.verify_info_icon_alert_draft_both_messages("both")
                if Check:
                    local_status_tc_69 = True
                    status_dict["TC_069"] = local_status_tc_69
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            # TC 70, TC 72
            print("Running Mail Draft TC 70, 72")
            with allure.step(
                    "TC_70, TC_72 - Verify the Subject is empty info dis-appeared after enter the subject name and Send Button is in Disabled state"):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.enter_subject(random_string(5))
                time.sleep(1)
                Check = self.mailDraftPage.verify_info_icon_alert_draft_both_messages("recipient")
                Check1 = self.mailDraftPage.verify_send_button_disabled_state()
                if Check and Check1:
                    local_status_tc_70 = True
                    local_status_tc_72 = True
                    status_dict["TC_070"] = local_status_tc_70
                    status_dict["TC_072"] = local_status_tc_72
                else:
                    print("TC70172 FAILED")

                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            # TC 71
            print("Running Mail Draft TC 71")
            with allure.step(
                    "TC_71 - Verify the the Recipient required info dis-appeared after add recipient."):
                #  self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                time.sleep(1)
                self.mailDraftPage.verify_add_participant_dialog(field="To")
                time.sleep(1)
                self.contactsPage.select_contact_from_overlay(user_B_name)
                time.sleep(1)
                Check = self.mailDraftPage.verify_info_icon_alert_draft_both_messages("subject")
                if Check:
                    local_status_tc_71 = True
                    status_dict["TC_071"] = local_status_tc_71
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 73 to 76")
            with allure.step(
                    "TC_73, TC_74, TC_75, TC_76 - Verify sent using displayed after configured new email and able to select and it should disappears once configured email removed."):
                # self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.verify_mail_will_be_sent_using_not_appears()
                time.sleep(1)
                self.mailPage.mail_configuration("triadqa7@outlook.com", "Welcome123$#@!")
                self.homePage.click_profile_name()
                Check1 = self.mailDraftPage.verify_mail_will_be_sent_using()
                Check2 = self.mailDraftPage.verify_click_mail_sent_using_dropdown()
                Check3 = self.mailDraftPage.verify_select_configured_mail_dropdown()
                # Remove for Re Run Case:
                time.sleep(1)
                self.mailDraftPage.click_mail_sent_using_dropdown()
                self.mailDraftPage.select_configured_mail_dropdown()
                self.mailPage.remove_configured_email("triadqa7@outlook.com")
                self.homePage.click_profile_name()
                time.sleep(1)
                Check4 = self.mailDraftPage.verify_mail_will_be_sent_using_not_appears()
                if Check1 and Check2 and Check3 and Check4:
                    local_status_tc_73 = True
                    local_status_tc_74 = True
                    local_status_tc_75 = True
                    local_status_tc_76 = True
                    status_dict["TC_073"] = local_status_tc_73
                    status_dict["TC_074"] = local_status_tc_74
                    status_dict["TC_075"] = local_status_tc_75
                    status_dict["TC_076"] = local_status_tc_76
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            print("Running Mail Draft TC 77, 79, 80")
            with allure.step(
                    "TC_77, TC_79, TC_80 - Verify Compose Mail draft opened in overlay from conversation and retained after tab shift and discard from overlay"):
                self.homePage.click_home_tab()
                time.sleep(1)
                self.homePage.compose_mail_to_create_conversation()
                self.mailDraftPage.sending_mail_after_draft_opened(subject, "TO", User_B_email, "tab", message)
                self.mailPage.mail_send_validation(test_case_number77)
                time.sleep(1)
                self.homePage.select_conversation_in_home_tab(subject)
                time.sleep(1)
                self.homePage.click_compose_mail_inside_conversation()
                Check1 = self.homePage.verify_compose_mail_draft_overlay_opened()
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.homePage.click_home_tab()
                time.sleep(1)
                Check2 = self.homePage.verify_compose_mail_draft_overlay_opened()
                Check3 = self.mailPage.verify_close_mail_draft_overlay()
                self.homePage.click_go_back_icon()
                time.sleep(1)
                if Check1 and Check2 and Check3:
                    local_status_tc_77 = True
                    local_status_tc_79 = True
                    local_status_tc_80 = True
                    status_dict["TC_077"] = local_status_tc_77
                    status_dict["TC_079"] = local_status_tc_79
                    status_dict["TC_080"] = local_status_tc_80

            print("Running Mail Draft TC 78")
            with allure.step(
                    "TC_78 - Verify pop out icon is working in mail draft overlay and opened as draft"):
                self.homePage.compose_mail_to_create_conversation()
                time.sleep(1)
                self.mailDraftPage.sending_mail_after_draft_opened(subject1, "TO", User_B_email, "tab", message)
                self.mailPage.mail_send_validation(test_case_number71)
                time.sleep(1)
                self.homePage.select_conversation_in_home_tab(subject1)
                time.sleep(1)
                self.homePage.click_compose_mail_inside_conversation()
                self.homePage.click_pop_out_mail_draft_from_overlay()
                time.sleep(1)
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                Check = self.mailDraftPage.verify_draft_opened_mail_configured()
                time.sleep(1)
                if Check:
                    local_status_tc_78 = True
                    status_dict["TC_078"] = local_status_tc_78
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()

        finally:
            with allure.step("Each Case Status"):

                # verify_status(test_case_number4, local_status_tc_04)
                verify_status(test_case_number7, local_status_tc_07)
                verify_status(test_case_number54, local_status_tc_54)
                verify_status(test_case_number55, local_status_tc_55)
                verify_status(test_case_number56, local_status_tc_56)
                verify_status(test_case_number57, local_status_tc_57)
                verify_status(test_case_number58, local_status_tc_58)
                verify_status(test_case_number59, local_status_tc_59)
                verify_status(test_case_number60, local_status_tc_60)
                verify_status(test_case_number61, local_status_tc_61)
                verify_status(test_case_number62, local_status_tc_62)
                verify_status(test_case_number63, local_status_tc_63)
                verify_status(test_case_number64, local_status_tc_64)
                verify_status(test_case_number65, local_status_tc_65)
                verify_status(test_case_number69, local_status_tc_69)
                verify_status(test_case_number70, local_status_tc_70)
                verify_status(test_case_number71, local_status_tc_71)
                verify_status(test_case_number72, local_status_tc_72)
                verify_status(test_case_number73, local_status_tc_73)
                verify_status(test_case_number74, local_status_tc_74)
                verify_status(test_case_number75, local_status_tc_75)
                verify_status(test_case_number76, local_status_tc_76)
                verify_status(test_case_number77, local_status_tc_77)
                verify_status(test_case_number78, local_status_tc_78)
                verify_status(test_case_number79, local_status_tc_79)
                verify_status(test_case_number80, local_status_tc_80)
                # status_report_update_to_xls(sheet_name, local_status_tc_04, test_case_number4)
                status_report_update_to_xls(sheet_name, local_status_tc_07, test_case_number7)
                status_report_update_to_xls(sheet_name, local_status_tc_54, test_case_number54)
                status_report_update_to_xls(sheet_name, local_status_tc_55, test_case_number55)
                status_report_update_to_xls(sheet_name, local_status_tc_56, test_case_number56)
                status_report_update_to_xls(sheet_name, local_status_tc_57, test_case_number57)
                status_report_update_to_xls(sheet_name, local_status_tc_58, test_case_number58)
                status_report_update_to_xls(sheet_name, local_status_tc_59, test_case_number59)
                status_report_update_to_xls(sheet_name, local_status_tc_60, test_case_number60)
                status_report_update_to_xls(sheet_name, local_status_tc_61, test_case_number61)
                status_report_update_to_xls(sheet_name, local_status_tc_62, test_case_number62)
                status_report_update_to_xls(sheet_name, local_status_tc_63, test_case_number63)
                status_report_update_to_xls(sheet_name, local_status_tc_64, test_case_number64)
                status_report_update_to_xls(sheet_name, local_status_tc_65, test_case_number65)
                status_report_update_to_xls(sheet_name, local_status_tc_69, test_case_number69)
                status_report_update_to_xls(sheet_name, local_status_tc_70, test_case_number70)
                status_report_update_to_xls(sheet_name, local_status_tc_71, test_case_number71)
                status_report_update_to_xls(sheet_name, local_status_tc_72, test_case_number72)
                status_report_update_to_xls(sheet_name, local_status_tc_73, test_case_number73)
                status_report_update_to_xls(sheet_name, local_status_tc_74, test_case_number74)
                status_report_update_to_xls(sheet_name, local_status_tc_75, test_case_number75)
                status_report_update_to_xls(sheet_name, local_status_tc_76, test_case_number76)
                status_report_update_to_xls(sheet_name, local_status_tc_77, test_case_number77)
                status_report_update_to_xls(sheet_name, local_status_tc_78, test_case_number78)
                status_report_update_to_xls(sheet_name, local_status_tc_79, test_case_number79)
                status_report_update_to_xls(sheet_name, local_status_tc_80, test_case_number80)

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
        self.logger.info("* Draft test case TC_01 Ended *")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_67 - Check the info icon for a Premium account with out email configuration\n"
        "TC_68 - Check whether Add button is working\n"
    )
    def test_draftCasesBeforeMailConfiguredPremium(self):

        # global status_tc_07, status_tc_02, status_tc_03, status_tc_04, status_tc_05, status_tc_06, status_tc_08, status_tc_09

        login_email = "clarititest5@yandex.com"
        login_password = "Triad@#123"
        # UserA_name = "ClaritTest5 Automation"
        test_case_number67 = "TC_067"
        test_case_number68 = "TC_068"

        sheet_name = "BasicMailCases"
        self.logger.info("* Draft test case TC_01 started *")

        local_status_tc_67 = None
        local_status_tc_68 = None

        status_dict = {
            "TC_067": local_status_tc_67,
            "TC_068": local_status_tc_68,
        }

        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(login_email, login_password)
                time.sleep(1)

            # TC 68
            print("Running Mail Draft TC 67, 68")
            with allure.step(
                    "TC_68 - Verify Add Mails to send mails alert and Navigated to Add Mails UI when clicks Add"):
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened()
                Check = self.mailDraftPage.verify_add_mail_to_send_mails()
                Check1 = self.mailDraftPage.verify_add_mail_ui_clicking_add_mails()
                if Check and Check1:
                    local_status_tc_67 = True
                    local_status_tc_68 = True
                    status_dict["TC_067"] = local_status_tc_67
                    status_dict["TC_068"] = local_status_tc_68
                self.homePage.click_profile_name()
                time.sleep(0.5)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()

        finally:
            with allure.step("Each Case Status"):

                verify_status(test_case_number67, local_status_tc_67)
                verify_status(test_case_number68, local_status_tc_68)

                status_report_update_to_xls(sheet_name, local_status_tc_67, test_case_number67)
                status_report_update_to_xls(sheet_name, local_status_tc_68, test_case_number68)

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
        self.logger.info("* Draft test case TC_01 Ended *")


class TestMailDraftCasess(BaseTest1):
    logger = LogGen.loggen()

    # @pytest.mark.pushMail1
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "TC_01 - User A send a Mail to User B, User B side validate count updated and select mails tab and select that received mail\n"
        "TC_02 - User A send a Mail to User B, User B side Reply to that mail and verify reply mail received in User A side and its merged or not\n"
        "TC_06 - User A send a Mail to User B, User B side validate count updated and select mails tab and select that received mail\n"
        "TC_07 - User A send a Mail to User B, User B delete the mail item and restore the mail and verify count updated in mails tab,.\n"
        "TC_08 - User A send a Mail to User B, User A resend the mail to user B, verify User B side both mails appears and count updated,."
    )
    def test_TC_01(self):

        # global status_tc_07, status_tc_02, status_tc_03, status_tc_04, status_tc_05, status_tc_06, status_tc_08, status_tc_09

        login_email = "triadqa6@yandex.com"
        login_password = "Welcome123$#@!"
        UserA_name = "Triadqa6Yandex Automation"
        subject = random_string(3)
        subject1 = random_string(3)
        checkSubject = subject
        User_B_email = "triadqa1@aol.com"
        message = "Test Demo mail"
        user_B_name = "Triadqa1aol Automation"
        test_case_number7 = "TC_007"
        test_case_number54 = "TC_054"
        test_case_number55 = "TC_055"
        test_case_number56 = "TC_056"
        test_case_number57 = "TC_057"
        test_case_number58 = "TC_058"
        test_case_number59 = "TC_059"
        test_case_number60 = "TC_060"
        test_case_number61 = "TC_061"
        test_case_number62 = "TC_062"
        test_case_number63 = "TC_063"
        test_case_number64 = "TC_064"
        test_case_number65 = "TC_065"
        test_case_number69 = "TC_069"
        test_case_number70 = "TC_070"
        test_case_number71 = "TC_071"

        sheet_name = "BasicMailCases"
        self.logger.info("* Draft test case TC_01 started *")

        local_status_tc_54 = None
        local_status_tc_55 = None
        local_status_tc_56 = None
        local_status_tc_57 = None

        status_dict = {
            "TC_054": local_status_tc_54,
            "TC_055": local_status_tc_55,
            "TC_056": local_status_tc_56,
            "TC_057": local_status_tc_57,
        }

        try:
            with allure.step("Login to clariti User A"):
                self.loginPage.clariti_sign_in(login_email, "")
                time.sleep(1)

            with allure.step(
                    "TC_54, TC_55, TC_56, TC_57 - Verify the default signature is displayed or not.. and verify checkbox selection and Apply Button"):
                time.sleep(1)
                self.mailPage.click_mails_tab()
                time.sleep(1)
                self.mailDraftPage.click_compose_mail_button()
                self.mailDraftPage.wait_for_draft_opened_mail_configured()
                self.mailDraftPage.click_show_editor_toolbar_icon()
                time.sleep(1)
                Check = self.mailDraftPage.verify_default_signature()
                time.sleep(1)
                Check1 = self.mailDraftPage.verify_add_this_signature_for_all_mails_enabled()
                time.sleep(1)
                Check2 = self.mailDraftPage.verify_add_this_signature_for_all_mails_uncheck()
                time.sleep(1)
                Check3 = self.mailDraftPage.verify_signature_dialog_closed_apply()
                time.sleep(1)
                if Check and Check1 and Check2 and Check3:
                    local_status_tc_54 = True
                    local_status_tc_55 = True
                    local_status_tc_56 = True
                    local_status_tc_57 = True
                    status_dict["TC_054"] = local_status_tc_54
                    status_dict["TC_055"] = local_status_tc_55
                    status_dict["TC_056"] = local_status_tc_56
                    status_dict["TC_057"] = local_status_tc_57
                    time.sleep(1)
                self.mailDraftPage.close_mail_draft()
                time.sleep(1)

            with allure.step("Doing logout"):
                self.homePage.click_logout()

        finally:
            with allure.step("Each Case Status"):

                verify_status(test_case_number54, local_status_tc_54)
                verify_status(test_case_number55, local_status_tc_55)
                verify_status(test_case_number56, local_status_tc_56)
                verify_status(test_case_number57, local_status_tc_57)

                status_report_update_to_xls(sheet_name, local_status_tc_54, test_case_number54)
                status_report_update_to_xls(sheet_name, local_status_tc_55, test_case_number55)
                status_report_update_to_xls(sheet_name, local_status_tc_56, test_case_number56)
                status_report_update_to_xls(sheet_name, local_status_tc_57, test_case_number57)

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
        self.logger.info("* Draft test case TC_01 Ended *")
