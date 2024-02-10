import time
import allure
import pytest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Clariti.pages.base_page import BasePage, take_element_screenshot, random_string
from Clariti.utilities.locators import Locators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home_tab(self):
        ContextAreas = self.get_element(Locators.HomePage.CONTEXT_AREA)
        HomeTabs = ContextAreas.find_element(*Locators.HomePage.HOME_TAB)
        HomeTabs.click()

    def click_profile_name(self):
        self.click(Locators.HomePage.PROFILE_NAME_CONTAINER)

    def click_logout(self):
        self.click(Locators.HomePage.PROFILE_NAME_CONTAINER)
        time.sleep(1)
        M = self.get_element(Locators.HomePage.LOGOUT_AREA)
        logouts = M.find_element(*Locators.HomePage.LOGOUT)
        logouts.click()
        try:
            self.wait_for_element(Locators.HomePage.LOGIN_PAGE_VERIFICATION)
        except TimeoutException:
            pass

    def unread_count(self, count_tab):
        try:
            ContextsAreas = self.get_element(Locators.HomePage.CONTEXTS_AREA)
            if count_tab == "mail":
                unread_count_mail = ContextsAreas.find_element(*Locators.HomePage.MAIL_COUNT)
                number_text = unread_count_mail.text
                count = number_text[1:-1]  # Remove the parentheses from the text.
                oldCount = int(count)
                return count
            elif count_tab == "home":
                unread_count_home = ContextsAreas.find_element(*Locators.HomePage.HOME_COUNT)
                number_text = unread_count_home.text
                count = number_text[1:-1]  # Remove the parentheses from the text.
                oldCount = int(count)
                return count
        except NoSuchElementException:
            count = str(0)
            oldCount = int(0)
            print(oldCount)
            return count

    def click_trash_tab(self):
        ContextAreas = self.get_element(Locators.HomePage.CONTEXT_AREA)
        TrashTab = ContextAreas.find_element(*Locators.HomePage.TRASH_TAB)
        TrashTab.click()

    def create_new_conversation(self, subject):
        self.click(Locators.HomePage.NEW_CONVERSATION_BUTTON)
        self.send_keys(Locators.HomePage.CONVERSATION_SUBJECT_TEXT_BOX, subject)
        self.click(Locators.HomePage.START_CONVERSATION_BUTTON)

    def start_chat(self):
        self.click(Locators.HomePage.NAVIGATION_PANEL_CHAT)

    def chat_item_continuous_view(self, expected_message):
        # screenshot_path = ".//Screenshots/LastDCFile.png"
        ContinuousView = self.get_element(Locators.HomePage.CONVERSATION_CONTINUOUS_VIEW)
        # ItemList =ContinuousView.find_elements(*Locators.HomePage.ITEM_LIST_CONTINUOUS_VIEW)
        Messages = ContinuousView.find_elements(*Locators.HomePage.MESSAGE_CONTINUES_VIEW)
        found_message = None

        for eachItem in reversed(Messages):
            if eachItem.text == expected_message:
                found_message = eachItem
                print("Last sent message " + eachItem.text + " exists")
                Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                action_chains = ActionChains(self.driver)
                action_chains.move_to_element(Message_item).perform()
                # take_element_screenshot(Message_item, screenshot_path)
                return found_message
        if found_message:
            print("Last sent message exists")
        elif found_message is None:
            print("Last sent message " + expected_message + " not exists")
            # take_element_screenshot(DctabMessageArea, screenshot_path)
            pytest.fail("Last Sent GC message Not Found")

    def active_ip_close(self, expected_ip):
        Active = self.get_element(Locators.HomePage.ACTIVE_CHATS_UNDER_HOME)
        ActiveItem = Active.find_elements(*Locators.HomePage.ACTIVE_CHAT_ITEM_UNDER_HOME)
        print(len(ActiveItem))
        for item in reversed(ActiveItem):
            SubjectIpChat = item.find_element(*Locators.HomePage.ACTIVE_CHAT_SUBJECT_CLASS)
            print(SubjectIpChat.text)
            if SubjectIpChat.text == expected_ip:
                action_chains = ActionChains(self.driver)
                action_chains.move_to_element(item).perform()
                item.click()
                CloseIcon = item.find_element(*Locators.HomePage.ACTIVE_CHAT_CLOSE_ICON)
                CloseIcon.click()
                break

    def verify_compose_mail_button(self, tab):
        if tab == "conversations":
            StartNewItem = self.get_text(Locators.HomePage.NEW_CONVERSATION_MAIL_STRIP_HEADER)
            if "Compose Mail" not in StartNewItem:
                print("Compose Mail icon not present in Conversation tab")
                self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW_HEADER, "VerifyComposeMailInConversation",
                                                  "Verify Compose Mail Icon not Available in Conversation tab for New "
                                                  "accounts")
                return True
            else:
                print("Compose Mail icon appears")
                self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW_HEADER, "VerifyComposeMailInConversation",
                                                  "Verify Compose Mail Icon not Available in Conversation tab for New "
                                                  "accounts")
                return False
                # pytest.fail("Compose Mail Icon appears in Conversation tab for Fresh SignedUp Accounts")
        if tab == "mail":
            StartNewItem = self.get_text(Locators.HomePage.NEW_CONVERSATION_MAIL_STRIP_HEADER)
            if "Compose Mail" in StartNewItem:
                print("Compose Mail icon present in Mails tab")
                self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW_HEADER, "VerifyComposeMailInMail",
                                                  "Verify Compose Mail Icon Available in Mail tab for New accounts")
                return True
            else:
                print("Compose Mail icon not appears")
                self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW_HEADER, "VerifyComposeMailInMail",
                                                  "Verify Compose Mail Icon Available in Mail tab for New accounts")
                return False

    def compose_mail_to_create_conversation(self):
        self.click(Locators.HomePage.NEW_CONVERSATION_BUTTON)
        time.sleep(1)
        # self.send_keys(Locators.HomePage.CONVERSATION_SUBJECT_TEXT_BOX, "Conversation "+random_string(5))
        self.click(Locators.HomePage.COMPOSE_MAIL_ACTION_BUTTON)
        # self.wait_for_element(Locators.HomePage.OVERLAY_CONTAINER)

    def click_compose_mail_inside_conversation(self):
        self.click(Locators.HomePage.COMPOSE_MAIL_ACTION_BUTTON)

    def verify_compose_mail_draft_overlay_opened(self):
        try:
            Overlay = self.get_element(Locators.HomePage.OVERLAY_CONTAINER)
            if Overlay.is_displayed():
                print("Mail Draft Opened in Overlay")
                time.sleep(1)
                self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW, "MailDraftOpenedOverlay",
                                                  "Verify Compose Mail draft opened/Retained in Overlay")
                return True
        except NoSuchElementException:
            print("Mail Draft Not Opened in Overlay")
            self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW, "MailDraftNotOpenedOverlay",
                                              "Verify Compose Mail draft opened/Retained in Overlay or Not")
            return False

    def click_go_back_icon(self):
        self.click(Locators.HomePage.GO_BACK_ICON)

    def click_pop_out_mail_draft_from_overlay(self):
        self.click(Locators.HomePage.POP_OUT_MAIL_DRAFT)

    def get_home_tab_items_includes_seperator(self, subject):
        # Get the table body element
        time.sleep(1)
        table = self.get_element(Locators.HomePage.TABLE_BODY)
        rows = table.find_elements(*Locators.HomePage.ROWS)
        # print(len(rows))
        found_row = None
        for row in rows:
            dateSeparator = row.find_elements(*Locators.HomePage.DATE_SEPARATOR_ROW)
            if dateSeparator:
                # Skip rows with dateSeperator
                continue
            subject_cell = row.find_element(*Locators.HomePage.SUBJECT_CLASS)
            if subject_cell:
                if subject == subject_cell.text:
                    # print(subject_cell.text)
                    # The row is found
                    found_row = subject_cell
                    # print(found_row.text)
                    break
        # Return the found row
        return found_row

    def select_conversation_in_home_tab(self, subject):
        try:
            found_row = self.get_home_tab_items_includes_seperator(subject)
            if found_row:
                self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW, "ConversationFound",
                                                  "Verify Conversation created in home tab")
                print("Conversation Found")
                found_row.click()
        except NoSuchElementException:
            print("Conversation Not Found")
            self.screenshot_and_attach_report(Locators.HomePage.DETAIL_VIEW, "ConversationNotFound",
                                              "Verify Conversation created in home tab or Not")