import datetime
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, TimeoutException, NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Clariti.pages.base_page import BasePage
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.locators import Locators


def take_element_screenshot(element, file_name):
    element.screenshot(file_name)


class MailPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self, driver, homePageInstance):
        super().__init__(driver)
        self.driver = driver
        self.home_page_instance = homePageInstance  # Store the HomePage instance

    # contexts_area = (By.CSS_SELECTOR, f"[class*='im-app-leftside-pane']")
    # home_tab_focus = (By.XPATH, ".//*[contains(text(), 'New Conversation')]")
    # new_strip = (By.CSS_SELECTOR, "[class*='im-tc-startnewcommstrip']")
    # table_body = (By.XPATH, '//*[contains(@id, "cdk-drop-list-")]')
    # rows = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-row'}']")
    # rows_loading = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-row row-loading'}']")
    # subject_class = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrivetablecell-textname'}']")
    # participant_class = (By.CSS_SELECTOR, f"[class*='{'im-sc-ll-participant-host'}']")
    # context_area = (By.CSS_SELECTOR, f"[class*='{'im-ct-items ps'}']")
    # mail_tab = (By.XPATH, "//div[@class='im-ct-menu-title' and text()='Mail ']")
    # mail_tab_tag = (By.XPATH, "//im-ct-emails")
    # operations_wrapper = (By.CSS_SELECTOR, f"[class*='{'im-da-th-operationsWrapper'}']")
    # go_back_icon = (By.XPATH, "//*[contains(@class,'im-td-cdrive-previousbreadcrumb')]")
    # header_area = (By.CSS_SELECTOR, f"[class*='{'im-da-cm-headeroperationsRoot'}']")
    # operation_icon = (By.CSS_SELECTOR, f"[class*='{'im-da-cm-headeroperationsIcon'}']")
    # route_dialog = (By.CLASS_NAME, "im-td-cdrivedetails-routeDialog")
    # add_button_spam = (By.CSS_SELECTOR, f"[class*='{'routingBasicAddBtn'}']")
    # mail_tab_detail_area = (By.CLASS_NAME, "im-td-cdrivedetailsRoot")
    # thread_area = (By.CSS_SELECTOR, f"[class*='{'im-da-th-ThreadBody-email'}']")
    # spam_text = (By.CSS_SELECTOR, f"[class*='{'im-da-em-spamText'}']")
    # singleton_icons = (By.CSS_SELECTOR, f"[class*='{'im-da-singletonoperations'}']")
    # unspam_restore_icon = (By.CSS_SELECTOR, f"[class*='{'im-da-th-trashOperationIcon'}']")
    # table_explorer = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrivetablayout-table'}']")
    # delete_icon_row_action = (By.CSS_SELECTOR, f"[class*='{'im-da-cm-drive-DeleteDrive'}']")
    # delete_tooltip_main_container = (By.CLASS_NAME, "cdk-overlay-container")
    # delete_button_tooltip_expected = "Mail belonging to a mail chain cannot be deleted"
    # delete_button_tooltip = (By.XPATH, "//*[contains(@id, 'cdk-overlay-')]/mat-tooltip-component/div")
    # mail_count = (By.XPATH, "//div[@class='im-ct-menu-title' and text()='Mail ']"
    #                         "//span[contains(@class, 'im-ct-cdrivemenu-unreadcount')]")
    # home_count = (By.XPATH, "//div[@class='im-ct-menu-title' and text()='Home ']"
    #                         "//span[contains(@class, 'im-ct-cdrivemenu-unreadcount')]")
    # mail_tab_ui = (By.XPATH, ".//*[contains(text(), 'Compose Mail')]")
    # trash_tab_filter = (By.CSS_SELECTOR, f"[class*='{'im-td-definedfilter-container'}']")
    # trash_tab_header = (By.XPATH, "//div[@class='im-td-cdrivetabheader-drive' and text()=' Trash ']")
    # table_row_loading = (By.CLASS_NAME, "loading-container ng-star-inserted")
    #
    # overlay_mail_draft = (By.CSS_SELECTOR, f"[class*='im-td-cdrive-detailsOverlay']")
    # detail_view_header_text = (By.CSS_SELECTOR, f"[class*='im-td-cdrivetabheader-drive']")
    # detail_view = (By.CSS_SELECTOR, f"[class*='im-td-cdrivetablayout-root']")
    # clariti_full_view = (By.CSS_SELECTOR, f"[class*='im-app-left-splitter']")
    # bring_mails_icon = (By.CSS_SELECTOR, f"[class*='im-ct-email-subtitle']")
    # overlay_container = (By.CSS_SELECTOR, f"[class*='im-td-detailsoverlay-container']")
    # configured_email_bring_mails_overlay = (By.CSS_SELECTOR, f"[class*='im-td-configuredcardcontainer']")
    # google_mail_card = (By.XPATH, "//*[@class='card-name' and contains(text(),'Google')]")
    # microsoft_mail_card = (By.XPATH, "//*[@class='card-name' and contains(text(),'Microsoft 365')]")
    # outlook_mail_card = (By.XPATH, "//*[@class='card-name' and contains(text(),'Outlook')]")
    # microsoft_email = (By.XPATH, "//input[@type='email']")
    # microsoft_email_next = (By.XPATH, "//input[@type='submit']")
    # microsoft_password = (By.XPATH, "//input[@name='passwd']")
    # microsoft_password_next = (By.XPATH, "//input[@type='submit']")
    # microsoft_signin_ui = (By.XPATH, "//*[@text()='Stay signed in?']")
    # microsoft_signin_button = (By.XPATH, "//input[@type='submit']")
    # overlay_mail_configure_loading = (By.CSS_SELECTOR,
    #                                   f"[class*='im-da-cm-progress-statusIconContainer ng-star-inserted']")
    # overlay_mail_item_row = (By.CSS_SELECTOR, f"[class*='im-td-cdrive-row']")
    # overlay_mail_item_table_body = (By.CSS_SELECTOR, f"[class*='im-td-cdrive-tablebody']")
    # date_seperator_row = (By.CSS_SELECTOR, f"[class*='{'im-td-Dateseparator'}']")
    # check_box_class = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrivetablecell-checkbox'}']")
    # bring_selected_mails_button = (By.CSS_SELECTOR, f"[class*='{'ok_button'}']")
    # overlay_header_text = (By.CSS_SELECTOR, f"[class*='breadcrumb-title']")
    # overlay_close_icon = (By.CSS_SELECTOR, f"[class*='im-td-overlayClose-icon']")
    #
    # connect_header_button_class = (By.CSS_SELECTOR, f"[class*='{'im-np-cm-integrationslist-optionheader'}']")
    # integration_card = (By.XPATH, ".//ancestor::im-np-cm-integrationscard")
    # connect_button = (By.CSS_SELECTOR, f"[class*='{'im-np-cm-integrationslist-connectbtn'}']")
    # profile_name_class = (By.CLASS_NAME, "im-np-hm-userNameSpan")
    # mail_preference = (By.CSS_SELECTOR, f"[class*='{'imEmailPreference'}']")
    # add_mail_configure_button = (By.XPATH, '//button/span[contains(text(),"Add ")]')
    # configured_email_card = (By.CSS_SELECTOR, f"[class*='im-np-cm-integrations-cardForAccount']")
    # mail_configured_ui = (By.CSS_SELECTOR, f"[class*='{'im-np-ep-configured-container'}']")
    # remove_account_button = (By.CSS_SELECTOR, f"[class*='im-rm-removeButton']")
    # yes_button_to_remove_account = (By.XPATH, "//button[contains(., 'Yes')]")
    # mail_preferences_main_ui = (By.CSS_SELECTOR, f"[class*='im-np-ep-manageAccountcontainer']")

    def click_mails_tab(self):
        ContextAreas = self.get_element(Locators.MailPage.CONTEXT_AREA)
        MailTabs = ContextAreas.find_element(*Locators.MailPage.MAIL_TAB)
        MailTabs.click()

    def click_reply_icon_1_user(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[0].click()

    def click_reply_icon_many_user(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        if len(OperationHeader) == 4:
            OperationHeader[3].click()
        elif len(OperationHeader) == 3:
            OperationHeader[2].click()
        time.sleep(2)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[3].click()

    def click_reply_all_icon(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[0].click()

    def click_resend(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[1].click()
        time.sleep(1)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[1].click()

    def click_delete_icon(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[2].click()

    def click_forward_icon_received(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        # print(len(OperationHeader))
        if len(OperationHeader) == 4:
            OperationHeader[3].click()
        elif len(OperationHeader) == 3:
            OperationHeader[2].click()
        time.sleep(2)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[2].click()

    def click_spam_icon(self):
        HeaderOperation = self.get_element(Locators.MailPage.HEADER_AREA)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        if len(OperationHeader) == 4:
            OperationHeader[3].click()
        elif len(OperationHeader) == 3:
            OperationHeader[2].click()
        time.sleep(1)
        OperationHeader = HeaderOperation.find_elements(*Locators.MailPage.OPERATION_ICON)
        OperationHeader[5].click()

    def click_add_in_spam_dialog(self):
        RouteDialogs = self.get_element(Locators.MailPage.ROUTE_DIALOG)
        AddButton = RouteDialogs.find_element(*Locators.MailPage.ADD_BUTTON_SPAM)
        AddButton.click()

    def verify_spammed_mail_text(self):
        DetailsView = self.get_element(Locators.MailPage.MAIL_TAB_DETAIL_AREA)
        ThreadBody = self.get_text(Locators.MailPage.SPAM_TEXT)
        print(ThreadBody)
        if "This email has been marked as Spam" in ThreadBody:
            self.screenshot_and_attach_report(Locators.MailPage.MAIL_TAB_DETAIL_AREA, "Spammed_mail", "Spammed Mail")
        else:
            print("Mail item is not spammed or spammed text is not visible,.")
            self.screenshot_and_attach_report(Locators.MailPage.MAIL_TAB_DETAIL_AREA, "Spammed_mail", "Spammed Mail UI Not appears")

    def click_restore_un_spam_icon(self):
        HeaderOperation = self.get_element(Locators.MailPage.SINGLETON_ICONS)
        OperationHeader = HeaderOperation.find_element(*Locators.MailPage.UN_SPAM_RESTORE_ICON)
        OperationHeader.click()

    def goback_tab(self):
        MailClick = self.get_element(Locators.MailPage.GO_BACK_ICON)
        MailClick.click()

    def wait_until_mail_tab_page(self):
        start_time = time.time()
        timeout = 10
        while time.time() - start_time < timeout:
            try:
                main_element = self.get_element(Locators.MailPage.MAIL_TAB_UI)
                if main_element.is_displayed:
                    print("Mail Page Navigated")
                    return True
                else:
                    print("Mail Page not Navigated")
                    time.sleep(1)  # Wait for the page to update after clicking
            except:
                WebDriverWait(self.driver, 1)
            time.sleep(0.5)  # Wait before checking again
        print("Mail page not loaded due some issues")
        return False

    def get_mail_tab_items(self, subject, participant):

        # Get the table body element
        table = self.get_element(Locators.MailPage.TABLE_BODY)
        time.sleep(1)
        rows = table.find_elements(*Locators.MailPage.ROWS)
        # print(len(rows))
        found_row = None
        for row in rows:
            dateSeparator = row.find_elements(*Locators.MailPage.DATE_SEPERATOR_ROW)
            if dateSeparator:
                # Skip rows with dateSeperator
                continue
            subject_cell = row.find_element(*Locators.MailPage.SUBJECT_CLASS)
            if subject_cell:
                if subject == subject_cell.text:
                    # print(subject_cell.text)
                    # Get the participant cell
                    participant_cell = row.find_element(*Locators.MailPage.PARTICIPANT_CLASS)
                    # Check if the subject and participant match
                    if participant in participant_cell.text:
                        # The row is found
                        found_row = subject_cell
                        # print(found_row.text)
                        break
        # Return the found row
        return found_row

    # Updated code with Date seperator row skip check
    # Dated on 22.10.2023
    def get_mail_tab_items_includes_seperator(self, subject, participant):
        # Get the table body element
        time.sleep(1)
        table = self.get_element(Locators.MailPage.TABLE_BODY)
        rows = table.find_elements(*Locators.MailPage.ROWS)
        # print(len(rows))
        found_row = None
        for row in rows:
            dateSeparator = row.find_elements(*Locators.MailPage.DATE_SEPERATOR_ROW)
            if dateSeparator:
                # Skip rows with dateSeperator
                continue
            subject_cell = row.find_element(*Locators.MailPage.SUBJECT_CLASS)
            if subject_cell:
                if subject == subject_cell.text:
                    # print(subject_cell.text)
                    # Get the participant cell
                    participant_cell = row.find_element(*Locators.MailPage.PARTICIPANT_CLASS)
                    # Check if the subject and participant match
                    if participant in participant_cell.text:
                        # The row is found
                        found_row = subject_cell
                        # print(found_row.text)
                        break
        # Return the found row
        return found_row

    def wait_until_homepage(self):
        start_time = time.time()
        timeout = 20
        while time.time() - start_time < timeout:
            try:
                # main_element = self.get_element(Locators.MailPage.HOME_TAB_FOCUS) or self.get_element(self.go_back_home_icon)
                parent_element = self.get_element(Locators.MailPage.NEW_STRIP)
                main_element = parent_element.find_element(*Locators.MailPage.HOME_TAB_FOCUS)

                if main_element.is_displayed:
                    print("Home Page Navigated")
                    return True
                else:
                    print("Home Page not Navigated")
                    time.sleep(1)  # Wait for the page to update after clicking
            except:
                WebDriverWait(self.driver, 1)
            time.sleep(0.5)  # Wait before checking again
        print("Home page not loaded due some issues")
        return False

    def wait_until_table_explore(self):
        start_time = time.time()
        timeout = 20
        while time.time() - start_time < timeout:
            try:
                # main_element = self.get_element(Locators.MailPage.HOME_TAB_FOCUS) or self.get_element(self.go_back_home_icon)
                main_element = self.get_element(Locators.MailPage.TABLE_EXPLORER)

                if main_element.is_displayed:
                    # print("Table Loaded")
                    return True
                else:
                    print("Table not Loaded")
                    time.sleep(1)  # Wait for the page to update after clicking
            except:
                WebDriverWait(self.driver, 1)
            time.sleep(0.5)  # Wait before checking again
        print("Table not loaded due some issues")
        return False

    def mail_send_validation(self, test_case_number):
        try:
            self.wait_until_homepage()
            time.sleep(0.5)
            assert True, " " + test_case_number + " Failed _ Mail sending failed"
        except AssertionError as e:
            print("Do logout")
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Assertion failed: Mail sending Failed {}".format(e))

    def wait_until_go_back_home_tab(self):

        self.wait_for_element(Locators.MailPage.GO_BACK_ICON)
        main_element = self.get_element(Locators.MailPage.GO_BACK_ICON)
        if main_element.is_displayed:
            print("Home Page Navigated")
            return True
        else:
            print("Home Page not Navigated")
            time.sleep(0.5)  # Wait for the page to update after clicking

    def mail_send_validation_without_mails_tab(self, test_case_number):
        try:
            self.wait_until_go_back_home_tab()
            time.sleep(0.5)
            assert True, " " + test_case_number + " Failed _ Mail sending failed"
        except AssertionError as e:
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Assertion failed: Mail sending Failed {}".format(e))

    def get_mail_item_and_verification(self, subject, contact_name, report_user_side, test_case_number):

        found_row = self.get_mail_tab_items(subject, contact_name)
        try:
            if found_row is not None and found_row.is_displayed():
                found_row.click()
                time.sleep(2)
                self.wait_for_element(Locators.MailPage.OPERATIONS_WRAPPER)
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Mail_present_in_mails_tab and expanded",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("* Mail item present in Home/Mails/Trash tab is passed *")
                log_message = "Mail item present in User " + report_user_side + " Home/Mails/Trash tab"
                allure.attach('<h3 style="color:green;">{}</h3>'.format(log_message),
                              name='User ' + report_user_side + '_mail_present_Verification_Passed',
                              attachment_type=allure.attachment_type.HTML)
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail_not_present_in_mails_tab",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("* Mail Item present in Home/Mails/Trash tab is Failed *")
                log_message = "Mail item not present in User " + report_user_side + " Home/Mails/Trash tab"
                allure.attach('<h3 style="color:red;">{}</h3>'.format(log_message),
                              name='User ' + report_user_side + '_mail_present_Verification_Failed',
                              attachment_type=allure.attachment_type.HTML)
                assert False

        except AssertionError as e:
            print("Item not available")
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Assertion failed " + test_case_number + ": Mail item not available {}".format(e))

    def verify_mail_threaded(self, subject, contact_name, report_user_side, test_case_number):
        found_row = self.get_mail_tab_items(subject, contact_name)
        time.sleep(1)
        found_row_full = found_row.find_element(By.XPATH, "./ancestor::tr")
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(found_row_full).perform()
        found_row_full = found_row.find_element(By.XPATH, "./ancestor::tr")
        delete_icon_class = found_row_full.find_element(*Locators.MailPage.DELETE_ICON_ROW_ACTION)
        action_chains.move_to_element(delete_icon_class).perform()
        time.sleep(2)
        delete_tooltip = self.get_text(Locators.MailPage.DELETE_BUTTON_TOOLTIP)
        print(delete_tooltip)
        try:
            if delete_tooltip == Locators.MailPage.DELETE_BUTTON_TOOLTIP_EXPECTED:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name='User_' + report_user_side + '_Delete_button_tooltip',
                              attachment_type=AttachmentType.PNG)
                log_message = "User " + report_user_side + "side Mail item threaded and verified by delete button is " \
                                                           "in disabled state"
                allure.attach('<h3 style="color:green;">{}</h3>'.format(log_message),
                              name='User_' + report_user_side + '_Mail_item_threaded_Verification_Passed',
                              attachment_type=allure.attachment_type.HTML)
                self.logger.info("* Mail item threaded and verified by tooltip is passed *")
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="UserB_Delete_button_tooltip_failed",
                              attachment_type=AttachmentType.PNG)
                log_message = ("User " + report_user_side +
                               "side Mail item not threaded and verified by delete button is in disabled state")
                allure.attach('<h3 style="color:red;">{}</h3>'.format(log_message),
                              name='User_' + report_user_side + '_Mail_item_threaded_Verification_Failed',
                              attachment_type=allure.attachment_type.HTML)
                self.logger.info("* Mail item threaded and verified by tooltip is Failed *")
                assert False

        except AssertionError as e:
            print("Delete Icon Enabled, Item not threaded,.")
            allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Assertion failed " + test_case_number +
                        ":  Mail not threaded, Verified by tooltip {}".format(e))

    def unread_count_mail(self, count_tab):
        try:
            ContextsAreas = self.get_element(Locators.MailPage.CONTEXTS_AREA)
            if count_tab == "mail":
                unread_count_mail = ContextsAreas.find_element(*Locators.MailPage.MAIL_COUNT)
                number_text = unread_count_mail.text
                count = number_text[1:-1]  # Remove the parentheses from the text.
                return count
            elif count_tab == "home":
                unread_count_home = ContextsAreas.find_element(*Locators.MailPage.HOME_COUNT)
                number_text = unread_count_home.text
                count = number_text[1:-1]  # Remove the parentheses from the text.
                return count
        except NoSuchElementException:
            count = str(0)
            oldCount = int(0)
            print(oldCount)
            return count

    def wait_until_polling_mail_received(self, count_tab):
        old_count = self.unread_count_mail(count_tab)
        old_count_int = int(old_count)
        print("old Count: " + old_count)
        start_time = time.time()
        timeout = 200
        while time.time() - start_time < timeout:
            try:
                new_count = self.unread_count_mail(count_tab)
                new_count_int = int(new_count)
                print("Count: " + new_count)
                if new_count_int > old_count_int:
                    print("Count Updated - New mail item received")
                    return True, new_count
                else:
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(current_time)
                    time.sleep(1)  # Wait for the page to update after clicking
            except:
                WebDriverWait(self.driver, 1)

            time.sleep(1)  # Wait before checking again

        print("Mail not received due to some issues")
        return False

    def trash_tab_ui(self):
        self.wait_for_element(Locators.MailPage.TRASH_TAB_HEADER)

    def verify_mail_tab_opened(self):
        Header = self.get_text(Locators.MailPage.DETAIL_VIEW_HEADER_TEXT)
        # print(Header)
        if Header == "Mail":
            print("Mail tab clickable and opened")
            # screenshot_path = ".//Screenshots/" + random_string(5) + " MailTabOpened.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.DETAIL_VIEW), screenshot_path)
            # allure.attach.file(screenshot_path, name=" Mail tab Clickable and Opened",
            #                    attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.DETAIL_VIEW, "MailTabOpened", "Mail tab Clickable and Opened")

            return True
        else:
            print("Mail tab not opened")
            # screenshot_path = ".//Screenshots/" + random_string(5) + " MailTabNotOpened.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.CLARITI_FULL_VIEW), screenshot_path)
            # allure.attach.file(screenshot_path, name=" Mail tab Not Clickable or Not Opened",
            #                    attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.CLARITI_FULL_VIEW, "MailTabNotOpened",
                                              "Mail tab not Clickable or not Opened")

            return False

    def verify_mail_tab_exists(self):
        try:
            MailTabContextsArea = self.get_element(Locators.MailPage.MAIL_TAB)
            if MailTabContextsArea:
                print("Mail tab Exists")
                # screenshot_path = ".//Screenshots/" + random_string(5) + "MailTab.png"
                # take_element_screenshot(self.get_element(Locators.MailPage.MAIL_TAB_TAG), screenshot_path)
                # allure.attach.file(screenshot_path, name=" Mail tab Present",
                #                    attachment_type=allure.attachment_type.PNG)
                self.screenshot_and_attach_report(Locators.MailPage.MAIL_TAB_TAG, "MailTab", "Mail tab Present")

        except:
            print("Mail tab Not Present,.")
            # screenshot_path = ".//Screenshots/" + random_string(5) + "MailTab.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.CONTEXTS_AREA), screenshot_path)
            # allure.attach.file(screenshot_path, name=" Mail tab Present", attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.CONTEXT_AREA, "MailTab", "Mail tab Present")

    def verify_bring_mails_exists(self):
        try:
            MailTabContextsArea = self.get_element(Locators.MailPage.BRING_MAILS_ICON)
            if MailTabContextsArea:
                print("Bring Mails icon Exists")
                # screenshot_path = ".//Screenshots/" + random_string(5) + "BringMails.png"
                # take_element_screenshot(self.get_element(Locators.MailPage.MAIL_TAB_TAG), screenshot_path)
                # allure.attach.file(screenshot_path, name=" Bring Mails tab Present",
                #                    attachment_type=allure.attachment_type.PNG)
                self.screenshot_and_attach_report(Locators.MailPage.MAIL_TAB_TAG, "BringMails", "Bring Mails tab Present")

                return True

        except:
            print("Bring Mails icon Not Present,.")
            # screenshot_path = ".//Screenshots/" + random_string(5) + " BringMails.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.CONTEXTS_AREA), screenshot_path)
            # allure.attach.file(screenshot_path, name=" Bring Mails tab not available",
            #                    attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.CONTEXT_AREA, "BringMails", "Bring Mails tab not available")

            return False

    def click_bring_mails(self):
        self.click(Locators.MailPage.BRING_MAILS_ICON)

    def verify_bring_mail_clicked(self):
        self.click_bring_mails()
        time.sleep(1)
        try:
            BringMailOverlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
            if BringMailOverlay.is_displayed():
                print("Bring Mails Overlay Opened")
                # screenshot_path = ".//Screenshots/" + random_string(5) + "BringMailsOpened.png"
                # take_element_screenshot(self.get_element(Locators.MailPage.DETAIL_VIEW), screenshot_path)
                # allure.attach.file(screenshot_path, name=" Bring Mails clicked and Overlay Opened ",
                #                    attachment_type=allure.attachment_type.PNG)
                self.screenshot_and_attach_report(Locators.MailPage.DETAIL_VIEW, "BringMailsOpened",
                                                  "Bring Mails clicked and Overlay Opened")
                return True
        except NoSuchElementException:
            print("Bring Mails Overlay Not opened")
            # screenshot_path = ".//Screenshots/" + random_string(5) + " BringMailsNotOpened.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.CLARITI_FULL_VIEW), screenshot_path)
            # allure.attach.file(screenshot_path, name="Bring Mails not clicked nor Overlay not Opened ",
            #                    attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.CLARITI_FULL_VIEW, "BringMailsNotOpened",
                                              "Bring Mails not clicked nor Overlay not Opened")
            return False

    def verify_configured_email_listed_in_bring_mails(self):
        # self.click_bring_mails()
        time.sleep(1)
        try:
            self.click_bring_mails()
            time.sleep(1)
            BringMailOverlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
            if BringMailOverlay.is_displayed():
                print("Bring Mails Overlay Opened")
                Configured_email_card = self.get_element(Locators.MailPage.CONFIGURED_EMAIL_BRING_MAILS_OVERLAY)
                if Configured_email_card.is_displayed():
                    print("Configured Email is listed in Overlay")
                    self.screenshot_and_attach_report(Locators.MailPage.DETAIL_VIEW, "ConfiguredEmailIsListedInOverlay",
                                                      "Verify configured email is listed in Overlay")
                return True
        except NoSuchElementException:
            print("Bring Mail option not available or Bring Mails Overlay Not opened or Configured Email is not listed in Overlay")
            self.screenshot_and_attach_report(Locators.MailPage.CLARITI_FULL_VIEW, "ConfiguredEmailIsListedInOverlay",
                                              "Verify configured email is listed in Overlay")
            return False

    def verify_bring_mails_header_text(self, configuredEmail):
        BringMailsHeaderText = self.get_text(Locators.MailPage.OVERLAY_HEADER_TEXT)
        if "Bring mails from " + configuredEmail == BringMailsHeaderText:
            print(configuredEmail + " - Mail Configured and Mails are listed ")
            # screenshot_path = ".//Screenshots/" + random_string(5) + "BringMailsOverlayHeaderText.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.OVERLAY_CONTAINER), screenshot_path)
            # allure.attach.file(screenshot_path, name=" Bring Mails Overlay Header Text with Configured Email ",
            #                    attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.OVERLAY_CONTAINER, "BringMailsOverlayHeaderText",
                                              "Bring Mails Overlay Header Text with Configured Email")
            return True
        else:
            print("Mail not Configured or Mails are not listed related to Configured Email")
            # screenshot_path = ".//Screenshots/" + random_string(5) + " BringMailsOverlayHeaderText.png"
            # take_element_screenshot(self.get_element(Locators.MailPage.CLARITI_FULL_VIEW), screenshot_path)
            # allure.attach.file(screenshot_path,
            #                    name="Bring Mails Overlay Header Text with Configured Email not Present ",
            #                    attachment_type=allure.attachment_type.PNG)
            self.screenshot_and_attach_report(Locators.MailPage.CLARITI_FULL_VIEW, "BringMailsOverlayHeaderText",
                                              "Bring Mails Overlay Header Text with Configured Email not Present")
            return False

    def close_overlay(self):
        self.click(Locators.MailPage.OVERLAY_CLOSE_ICON)

    def configure_outlook_bring_mails(self, email, password):
        try:
            BringMailOverlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
            BringMailOverlay.find_element(*Locators.MailPage.OUTLOOK_MAIL_CARD).click()
            self.outlook_mail_configuration(email, password)
            return True
        except:
            print("Configuration Failed")
            self.screenshot_and_attach_report(Locators.MailPage.CLARITI_FULL_VIEW, "ConfigurationFailed", "Configuration_failed")
            return False

    def outlook_mail_configuration(self, email, password):
        # Getting current window handle
        current_window = self.driver.current_window_handle

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
        self.send_keys(Locators.MailPage.MICROSOFT_EMAIL, email)

        # Click Next button in Enter email address page
        self.click(Locators.MailPage.MICROSOFT_EMAIL_NEXT)

        time.sleep(2)

        # Wait until password page opens
        self.wait_for_element(Locators.MailPage.MICROSOFT_PASSWORD)

        # Enter Gmail Password
        self.send_keys(Locators.MailPage.MICROSOFT_PASSWORD, password)

        # Click Next button in password page
        self.click(Locators.MailPage.MICROSOFT_PASSWORD_NEXT)
        time.sleep(2)
        self.click(Locators.MailPage.MICROSOFT_SIGNIN_BUTTON)

        # focusing to old window handle
        WebDriverWait(self.driver, 30).until(lambda driver: len(driver.window_handles) == len(window_handles) - 1)

        self.driver.switch_to.window(current_window)
        # BringMailOverlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
        # self.wait_for_element_disappears(Locators.MailPage.OVERLAY_MAIL_CONFIGURE_LOADING)
        # time.sleep(2)
        # self.wait_for_element(Locators.MailPage.OVERLAY_MAIL_ITEM_ROW)
        # while True:
        #     TableBody = BringMailOverlay.find_element(*self.OVERLAY_MAIL_ITEM_TABLE_BODY)
        #     Rows = TableBody.find_elements(*Locators.MailPage.OVERLAY_MAIL_ITEM_ROW)
        #     if len(Rows) > 2:
        #         print("Item Row is greater than 2.")
        #         break
        #     else:
        #         print("Item Row is not yet greater than 2. Waiting...")
        #         self.wait_for_all_element(Locators.MailPage.OVERLAY_MAIL_ITEM_ROW)

    # Select Bring Mails by Verify with subject name, say given subject,...
    # Dated on 22.10.2023
    def get_bring_mails_items(self, subject):
        BringMailOverlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
        table = self.get_element(Locators.MailPage.TABLE_BODY)
        rows = table.find_elements(*Locators.MailPage.ROWS)
        print(len(rows))
        selected_subjects = []
        for row in rows:
            subject_cell = row.find_element(*Locators.MailPage.SUBJECT_CLASS)
            if subject == subject_cell.text:
                print(subject_cell.text)
                CheckBox = row.find_element(*Locators.MailPage.CHECK_BOX_CLASS)
                CheckBox.click()
                subject_cell = row.find_element(*Locators.MailPage.SUBJECT_CLASS)
                subject = subject_cell.text
                selected_subjects.append(subject)
                print(subject)
                break

        BringSelectedMails = BringMailOverlay.find_element(*Locators.MailPage.BRING_SELECTED_MAILS_BUTTON)
        BringSelectedMails.click()
        self.wait_for_element_disappears(BringMailOverlay)
        print(1)
        time.sleep(5)

    # Select Bring Mails by given count to select 1 by 1,...
    # Dated on 22.10.2023
    def get_bring_mails_items_random(self, select_count):
        BringMailOverlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
        table = self.get_element(Locators.MailPage.TABLE_BODY)
        rows = table.find_elements(*Locators.MailPage.ROWS)
        print(len(rows))
        selected_subjects = []
        for row in rows:
            if select_count > 0:
                CheckBox = row.find_element(*Locators.MailPage.CHECK_BOX_CLASS)
                CheckBox.click()
                subject_cell = row.find_element(*Locators.MailPage.SUBJECT_CLASS)
                subject = subject_cell.text
                selected_subjects.append(subject)
                print(subject)
                select_count -= 1
        BringSelectedMails = BringMailOverlay.find_element(*Locators.MailPage.BRING_SELECTED_MAILS_BUTTON)
        BringSelectedMails.click()

        self.wait_for_element_disappears(BringMailOverlay)
        print(1)
        time.sleep(5)

    def wait_until_mail_send_overlay(self):
        try:
            main_element = self.get_element(Locators.MailPage.OVERLAY_MAIL_DRAFT)
            self.wait_for_element_disappears(main_element)
            print("Mail send and Overlay Draft Closed")

        except NoSuchElementException:
            print("Overlay Draft not opened")

    def mail_configuration(self, email, password):
        self.click(Locators.MailPage.PROFILE_NAME_CLASS)
        self.click(Locators.MailPage.MAIL_PREFERENCE)
        self.click(Locators.MailPage.ADD_MAIL_CONFIGURE_BUTTON)
        ConnectButton = self.get_elements(Locators.MailPage.CONNECT_HEADER_BUTTON_CLASS)
        time.sleep(1)
        for eachitem in ConnectButton:
            if eachitem.text == "Outlook":
                base_tr = eachitem.find_element(*Locators.MailPage.INTEGRATION_CARD)
                base_tr.find_element(*Locators.MailPage.CONNECT_BUTTON).click()
                time.sleep(1)
                self.outlook_mail_configuration(email, password)
                break
        self.wait_for_element(Locators.MailPage.MAIL_CONFIGURED_UI)

    def click_manage_button_configured_email(self, email_id):
        Configured_emails = self.get_elements(Locators.MailPage.CONFIGURED_EMAIL_CARD)
        for eachConfiguredEmail in Configured_emails:
            if email_id in eachConfiguredEmail.text:
                eachConfiguredEmail.find_element(*Locators.MailPage.CONNECT_BUTTON).click()
                break

    def click_remove_account_button(self):
        self.click(Locators.MailPage.REMOVE_ACCOUNT_BUTTON)

    def remove_configured_email(self, email_id):
        self.click(Locators.MailPage.PROFILE_NAME_CLASS)
        self.click(Locators.MailPage.MAIL_PREFERENCE)
        self.click_manage_button_configured_email(email_id)
        self.click_remove_account_button()
        self.click(Locators.MailPage.YES_BUTTON_TO_REMOVE_ACCOUNT)
        self.wait_for_element(Locators.MailPage.MAIL_PREFERENCES_MAIN_UI)

    def verify_close_mail_draft_overlay(self):
        self.close_overlay()
        self.click(Locators.MailPage.YES_BUTTON_TO_REMOVE_ACCOUNT)
        self.wait_for_element_disappears(Locators.MailPage.OVERLAY_CONTAINER)
        try:
            Overlay = self.get_element(Locators.MailPage.OVERLAY_CONTAINER)
            if Overlay.is_displayed():
                print("overlay mail draft still open")
                self.screenshot_and_attach_report(Locators.MailPage.DETAIL_VIEW, "MailDraftOpenedOverlay",
                                                  "Verify Compose Mail draft overlay closed or Not")
                return False

        except NoSuchElementException:
            print("overlay mail draft Closed")
            self.screenshot_and_attach_report(Locators.MailPage.DETAIL_VIEW, "MailDraftOverlayClosed",
                                              "Verify Compose Mail draft overlay closed")
            return True
