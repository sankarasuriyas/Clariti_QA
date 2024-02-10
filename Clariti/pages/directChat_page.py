import datetime
from datetime import datetime
import os
import time
import pytest
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController, Button
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Clariti.pages.base_page import BasePage, wait_for_file_explorer_open
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.locators import Locators


class DirectChatPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.Keys = None
        self.driver = driver

    # direct_chat_tab = Locators.DirectChatPage.DIRECT_CHAT_TAB
    # overlay_show_actions = Locators.DirectChatPage.OVERLAY_SHOW_ACTIONS
    # dc_tab_layout_area = Locators.DirectChatPage.DC_TAB_LAYOUT_AREA
    # messages_area = Locators.DirectChatPage.MESSAGES_AREA
    # message_lists = Locators.DirectChatPage.MESSAGE_LISTS
    # direct_chat_area = Locators.DirectChatPage.DIRECT_CHAT_AREA
    # pinned_contacts_area = Locators.DirectChatPage.PINNED_CONTACTS_AREA
    # dc_contact_direct_chat = Locators.DirectChatPage.DC_CONTACT_DIRECT_CHAT
    # dc_contact_name_direct_chat = Locators.DirectChatPage.DC_CONTACT_NAME_DIRECT_CHAT
    # dc_contact_green_indicator_direct_chat = Locators.DirectChatPage.DC_CONTACT_GREEN_INDICATOR_DIRECT_CHAT
    # dc_contacts_under_direct_chat = Locators.DirectChatPage.DC_CONTACTS_UNDER_DIRECT_CHAT
    # dc_contacts_area = Locators.DirectChatPage.DC_CONTACTS_AREA
    # dc_contact_name_area = Locators.DirectChatPage.DC_CONTACT_NAME_AREA
    # dc_header = Locators.DirectChatPage.DC_HEADER
    # chat_editor = Locators.DirectChatPage.CHAT_EDITOR
    # dc_tab_layout = Locators.DirectChatPage.DC_TAB_LAYOUT
    # dc_message_area = Locators.DirectChatPage.DC_MESSAGE_AREA
    # dc_message = Locators.DirectChatPage.DC_MESSAGE
    # dc_file = Locators.DirectChatPage.DC_FILE
    # svg_icons = Locators.DirectChatPage.SVG_ICONS
    # svg_icon_contact_row_action = Locators.DirectChatPage.SVG_ICON_CONTACT_ROW_ACTION
    # block_ui_dc = Locators.DirectChatPage.BLOCK_UI_DC
    # reply_icon_dc_message = Locators.DirectChatPage.REPLY_ICON_DC_MESSAGE
    # green_indicator_status_icon = Locators.DirectChatPage.GREEN_INDICATOR_STATUS_ICON
    # unread_new_messages_strip = Locators.DirectChatPage.UNREAD_NEW_MESSAGES_STRIP
    # file_overlay = Locators.DirectChatPage.FILE_OVERLAY
    # file_main_overlay = Locators.DirectChatPage.FILE_MAIN_OVERLAY
    # close_icon_overlay = Locators.DirectChatPage.CLOSE_ICON_OVERLAY
    # no_preview_available = Locators.DirectChatPage.NO_PREVIEW_AVAILABLE
    # file_download_button = Locators.DirectChatPage.FILE_DOWNLOAD_BUTTON
    # iframe_element_class = Locators.DirectChatPage.IFRAME_ELEMENT_CLASS
    # iframe_element_preparing_clariti_viewer = Locators.DirectChatPage.IFRAME_ELEMENT_PREPARING_CLARITI_VIEWER
    # iframe_element_file_container = Locators.DirectChatPage.IFRAME_ELEMENT_FILE_CONTAINER
    # unsupported_file_area = Locators.DirectChatPage.UNSUPPORTED_FILE_AREA
    # download_button_file_overlay = Locators.DirectChatPage.DOWNLOAD_BUTTON_FILE_OVERLAY
    # input_area = Locators.DirectChatPage.INPUT_AREA
    # reference_strip_area = Locators.DirectChatPage.REFERENCE_STRIP_AREA
    # reference_strip_container = Locators.DirectChatPage.REFERENCE_STRIP_CONTAINER
    # reference_strip_message_text = Locators.DirectChatPage.REFERENCE_STRIP_MESSAGE_TEXT
    # reference_strip_file_text = Locators.DirectChatPage.REFERENCE_STRIP_FILE_TEXT
    # show_actions_icon = Locators.DirectChatPage.SHOW_ACTIONS_ICON
    # reply_button_show_action = Locators.DirectChatPage.REPLY_BUTTON_SHOW_ACTION
    # forward_button_show_action = Locators.DirectChatPage.FORWARD_BUTTON_SHOW_ACTION
    # copy_button_show_acton = Locators.DirectChatPage.COPY_BUTTON_SHOW_ACTION
    # forward_button_dialog = Locators.DirectChatPage.FORWARD_BUTTON_DIALOG
    # forwarded_strip_message = Locators.DirectChatPage.FORWARDED_STRIP_MESSAGE
    # get_name_message = Locators.DirectChatPage.GET_NAME_MESSAGE
    # get_time_message = Locators.DirectChatPage.GET_TIME_MESSAGE
    # get_time_hover_message = Locators.DirectChatPage.GET_TIME_HOVER_MESSAGE
    # scroll_to_bottom_icon = Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON
    # new_message_strip = Locators.DirectChatPage.NEW_MESSAGE_STRIP
    # mat_icons = Locators.DirectChatPage.MAT_ICONS

    def select_dc_contact_direct_chat(self, dc_contact):
        DcContactArea = self.get_element(Locators.DirectChatPage.PINNED_CONTACTS_AREA)
        DcContactlist = DcContactArea.find_elements(*Locators.DirectChatPage.DC_CONTACT_DIRECT_CHAT)
        for eachContact in DcContactlist:
            Contact = eachContact.find_element(*Locators.DirectChatPage.DC_CONTACT_NAME_DIRECT_CHAT)
            getContact = Contact.text
            print(getContact)
            if getContact == dc_contact:
                print("contact exists")
                Contact.click()
                break
            else:
                print("contact name not matched")

    def check_scroll_to_bottom_icon(self):
        try:
            if self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON).is_displayed():
                if not self.get_element(Locators.DirectChatPage.NEW_MESSAGE_STRIP).is_displayed():
                    self.click(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
                    print("Count button and new message strip not appears")
                    time.sleep(1)
                elif (self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON).is_displayed()
                      and self.get_element(Locators.DirectChatPage.NEW_MESSAGE_STRIP).is_displayed()):
                    print("Both new message strip and Scroll to Bottom button appears")
                    self.click(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
                    time.sleep(0.5)
            else:
                print("Else")
        except NoSuchElementException:
            print("Scroll to bottom icon not appears")

    def last_dc_messages(self, expected_message):
        DcTabLayout = self.get_element(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA)
        lMessage_area = DcTabLayout.find_element(*Locators.DirectChatPage.MESSAGES_AREA)
        MessageList = lMessage_area.find_elements(*Locators.DirectChatPage.MESSAGE_LISTS)
        found_message = None
        for eachMessage in reversed(MessageList):
            if eachMessage.text == expected_message:
                found_message = eachMessage
                found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                print("Last sent message " + eachMessage.text + " exists")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "DC_Message",
                                                  "Last sent message " + eachMessage.text + " exists")
                break

            elif expected_message in eachMessage.text:
                found_message = eachMessage
                found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                print("Last sent message " + eachMessage.text + " exists")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "DC_Message",
                                                  "Last sent message " + eachMessage.text + " exists")
                break
            else:
                print("Last sent message " + eachMessage.text + " not exists")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT, "DC_Message",
                                                  "Last sent message " + eachMessage.text + " not exists")
                # pytest.fail("Last Sent message not exists!!!")
        if found_message is not None:
            return found_message

    def verify_last_dc_message(self, dc_message):
        try:
            found_message = self.last_dc_messages(dc_message)
            print("After Found Message")
            try:
                self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
                print("Check scroll to bottom in try")
            except NoSuchElementException:
                print("Check scroll to bottom in except")
                pass
            if found_message is None and self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON).is_displayed():
                self.click(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
                time.sleep(1)
                print("Check scroll to bottom in if block")
                found_message = self.last_dc_messages(dc_message)
                print("After Found Message in if cond")
                if found_message:
                    print("DC message Available")
                    return True
            elif found_message:
                print("After Found Message in elif cond")
                try:
                    if self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON).is_displayed():
                        print("Multiple New Messages with Scroll to bottom icon appears")
                        return True
                except NoSuchElementException:
                    print("DC message Available")
                    return True
        except NoSuchElementException:
            print("DC message not Available")
            return False

    def verify_forward_strip(self, expected_message):
        found_message = self.last_dc_messages(expected_message)
        if found_message:
            # print("Inside If found message")
            Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
            forwardStrip = Message_item.find_element(*Locators.DirectChatPage.FORWARDED_STRIP_MESSAGE)
            # print("Forward strip")
            if forwardStrip.is_displayed():
                print("Forward Strip Exists")
                return True
            else:
                print("Forward strip Not exists")
                return False
        else:
            print("message Not exists")
            return False

    def last_dc_file(self, expected_message):
        DctabMessageArea = self.get_element(Locators.DirectChatPage.DC_TAB_LAYOUT)
        lmessage_area = DctabMessageArea.find_element(*Locators.DirectChatPage.DC_MESSAGE_AREA)
        Messages = lmessage_area.find_elements(*Locators.DirectChatPage.DC_FILE)
        found_File = None
        for eachFileMessage in reversed(Messages):
            if eachFileMessage.text == expected_message:
                found_File = eachFileMessage
                print("Last sent File " + eachFileMessage.text + " exists")
                found_File.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "LastDCFile",
                                                  "Last sent message " + eachFileMessage.text + " exists")
                return found_File
        if found_File:
            print("Last sent File exists")
            return found_File
        elif found_File is None:
            print("Last sent File " + expected_message + " not exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT, "LastDCFile",
                                              "Last sent message " + expected_message + " not exists")
            pytest.fail("Last Sent DC File Not Found")

    def verify_last_file_message(self, dc_message):
        try:
            found_message = self.last_dc_file(dc_message)
            if found_message:
                print("DC file Available")
                return True
        except NoSuchElementException:
            print("DC file not Available")
            return False

    def click_dc_file(self, expected_message):
        found_file = self.last_dc_file(expected_message)
        if found_file:
            found_file.click()
        else:
            print("FileNotFound")

    def click_attachment_icon_dc_file(self):
        self.click(Locators.DirectChatPage.CHAT_EDITOR)
        ChatInputArea = self.get_element(Locators.DirectChatPage.INPUT_AREA)
        svg_icon = ChatInputArea.find_elements(By.TAG_NAME, "svg")
        first_icon = svg_icon[0]
        first_icon.click()
        wait_for_file_explorer_open()

    def send_dc_file(self, file_upload_count, file_name):
        self.click(Locators.DirectChatPage.CHAT_EDITOR)
        ChatInputArea = self.get_element(Locators.DirectChatPage.INPUT_AREA)
        svg_icon = ChatInputArea.find_elements(By.TAG_NAME, "svg")
        first_icon = svg_icon[0]
        first_icon.click()
        time.sleep(4)
        current_file_path = os.path.abspath(__file__)  # Get the path of the current script
        project_path = os.path.dirname(os.path.dirname(current_file_path))
        # print(project_path)
        if file_upload_count == 1:
            file_path = project_path + "\\testfiles\\" + file_name
            mouse = MouseController()
            mouse.position = (300, 100)  # Set the coordinates of the file in the dialog
            mouse.click(Button.left)
            keyboard = Controller()
            keyboard.type(str(file_path))
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
        elif file_upload_count == 2:
            file_path = project_path + "\\testfiles"
            keyboard = Controller()
            mouse = MouseController()
            keyboard.type(file_path)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            mouse.position = (300, 200)  # Set the coordinates of the file in the dialog
            mouse.click(Button.left)
            keyboard.press(Key.ctrl)
            keyboard.press('a')
            keyboard.release('a')
            keyboard.release(Key.ctrl)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1)

    def get_contact_under_contacts_tab(self, contact):
        DC_Contacts = self.get_elements(Locators.DirectChatPage.DC_CONTACTS_AREA)
        DC_Contacts_list = self.get_element(Locators.DirectChatPage.DC_CONTACTS_UNDER_DIRECT_CHAT)
        Participant_Name = DC_Contacts_list.find_elements(*Locators.DirectChatPage.DC_CONTACT_NAME_AREA)
        found_contact = None
        for eachContact in reversed(Participant_Name):
            if len(DC_Contacts) == 1:
                if contact == Participant_Name[0].text:
                    print("contact " + eachContact.text + " Found")
                    found_contact = eachContact
                    found_contact.find_element(By.XPATH, "./ancestor::im-ct-contacts")
                    # self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DC_Contact", "contact " + eachContact.text + " exists")
                    break
            elif len(DC_Contacts) > 1:
                if contact == eachContact.text:
                    print("contact " + eachContact.text + " Found")
                    found_contact = eachContact
                    found_contact.find_element(By.XPATH, "./ancestor::im-ct-contacts")
                    # self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DC_Contact", "contact " + eachContact.text + " exists")
                    break
            else:
                print("No items found.")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DC_Contact", "contact not exists")
        return found_contact

    def verify_green_indicator_dc(self, contact_name):
        try:
            found_contact = self.get_contact_under_contacts_tab(contact_name)
            if found_contact:
                green_indicator = self.get_element(Locators.DirectChatPage.GREEN_INDICATOR_STATUS_ICON)
                if green_indicator.is_enabled():
                    print("Green indicator appears")
                    self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DCContactGreenIndicator",
                                                      "verify contact green indicator")
                    # found_contact.click()
                    return True
        except NoSuchElementException:
            print("Green indicator not appears or contact not found")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DCContactGreenIndicator",
                                              "verify contact green indicator")
            return False

    def hover_on_dc_contact(self, contact_name):
        found_contacts = self.get_contact_under_contacts_tab(contact_name)
        if found_contacts:
            self.hover_on_element(found_contacts)
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "HoverDCContact", "DC Contact Hovered")
        else:
            print("contact Not Found")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "HoverDCContact", "Verify DC Contact Hovered")

    def click_on_dc_contact(self, contact_name):
        found_contacts = self.get_contact_under_contacts_tab(contact_name)
        if found_contacts:
            found_contacts.click()
        else:
            print("contact Not Found")

    def verify_dc_contact_under_contacts(self, contact_name):
        found_contacts = self.get_contact_under_contacts_tab(contact_name)
        if found_contacts:
            print("contact Exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DCContactUnderContacts",
                                              "Verify DC Contact Exists under Contacts")
        else:
            print("contact Not Found under Direct Chat Area")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DCContactUnderContacts",
                                              "Verify DC Contact Exists under Contacts")
            pytest.fail("contact not exists under Direct Chat area!!!")

    def verify_dc_contact_not_exists(self, contact_name):
        found_contacts = self.get_contact_under_contacts_tab(contact_name)
        if not found_contacts:
            print("contact Not Exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DC_Contact_Area", "Verify contact not exists")
        else:
            print("contact Found under Direct Chat Area")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DIRECT_CHAT_AREA, "DC_Contact_Area", "Verify contact not exists")
            pytest.fail("contact exists under Direct Chat area!!!")

    def send_dc_message(self, message):
        self.wait_for_element(Locators.DirectChatPage.DC_HEADER)
        self.send_keys(Locators.DirectChatPage.CHAT_EDITOR, message + Keys.ENTER)

    def wait_for_dc_tab_load(self):
        self.wait_for_element(Locators.DirectChatPage.DC_HEADER)

    def verify_block_ui_dc_tab(self):
        try:
            blockUi = self.get_element(Locators.DirectChatPage.BLOCK_UI_DC)
            if blockUi.is_displayed:
                print("Block UI visible")
                self.screenshot_and_attach_report(Locators.DirectChatPage.BLOCK_UI_DC, "Block_UI_DC_Contact",
                                                  "Verify Block UI in DC contact")
                return True
        except NoSuchElementException:
            print("Block UI not visible")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "Block_UI_DC_Contact",
                                              "Verify Block UI in DC contact")
            return False
            # pytest.fail("contact exists under Direct Chat area!!!")

    def verify_file_viewer_overlay(self):
        File_viewer_overlay = self.get_element(Locators.DirectChatPage.FILE_OVERLAY)
        if File_viewer_overlay.is_displayed():
            # print("File opened")
            iframe_element = File_viewer_overlay.find_element(*Locators.DirectChatPage.IFRAME_ELEMENT_CLASS)
            self.driver.switch_to.frame(iframe_element)
            # print("iframeFile")
            try:
                if self.get_element(Locators.DirectChatPage.IFRAME_ELEMENT_PREPARING_CLARITI_VIEWER).is_displayed():
                    self.wait_for_element_disappears(Locators.DirectChatPage.IFRAME_ELEMENT_PREPARING_CLARITI_VIEWER)
                    iframe_element_file = self.get_element(Locators.DirectChatPage.IFRAME_ELEMENT_FILE_CONTAINER)
                    if iframe_element_file.is_displayed():
                        # print("File Loaded")
                        self.driver.switch_to.default_content()
                        self.screenshot_and_attach_report(Locators.DirectChatPage.FILE_OVERLAY, "FileViewer", "File_Overlay_Viewer")
                        return True
                    else:
                        print("File not loaded")
                    self.driver.switch_to.default_content()
                    return False
                else:
                    time.sleep(2)
                    iframe_element_file = self.get_element(Locators.DirectChatPage.IFRAME_ELEMENT_FILE_CONTAINER)
                    if iframe_element_file.is_displayed():
                        # print("File Loaded from else")
                        self.driver.switch_to.default_content()
                        self.screenshot_and_attach_report(Locators.DirectChatPage.FILE_OVERLAY, "FileViewer", "File_Overlay_Viewer")
                        return True
                    else:
                        print("File not loaded")
                    self.driver.switch_to.default_content()
                return False

            except TimeoutException:
                print("Time out - File not loaded in desired time.")
                self.driver.switch_to.default_content()
                self.screenshot_and_attach_report(Locators.DirectChatPage.FILE_OVERLAY, "FileViewer", "File_Overlay_Viewer")
                return False
        else:
            print("File overlay not opened")
            self.screenshot_and_attach_report(Locators.DirectChatPage.FILE_OVERLAY, "FileViewer", "File_Overlay_Viewer")
            return False

    def close_file_overlay(self):
        MainOverlay = self.get_element(Locators.DirectChatPage.FILE_MAIN_OVERLAY)
        CloseIcon = MainOverlay.find_element(*Locators.DirectChatPage.CLOSE_ICON_OVERLAY)
        CloseIcon.click()

    def verify_non_viewable_file(self):
        try:
            self.get_element(Locators.DirectChatPage.FILE_OVERLAY)
            self.get_element(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA)
            unsupportedFile = self.get_element(Locators.DirectChatPage.UNSUPPORTED_FILE_AREA)
            DownloadButton = unsupportedFile.find_element(*Locators.DirectChatPage.DOWNLOAD_BUTTON_FILE_OVERLAY)
            if DownloadButton.is_displayed():
                print("Download Button displayed")
                self.screenshot_and_attach_report(Locators.DirectChatPage.FILE_OVERLAY, "FileViewer_non_viewable_File",
                                                  "File_Overlay_Viewer_Non_Viewable_File")
                return True
            else:
                print("Download Button not displayed")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "FileViewer_non_viewable_File",
                                                  "File_Overlay_Viewer_Non_Viewable_File")
                return False
        except NoSuchElementException:
            self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "FileViewer_non_viewable_File",
                                              "File_Overlay_Viewer_Non_Viewable_File")
            return False

    def verify_reply_strip_chat_editor(self, dc_file_message, expected_message):
        DcTabLayout = self.get_element(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA)
        if dc_file_message == "message":
            try:
                ChatInputArea = self.get_element(Locators.DirectChatPage.INPUT_AREA)
                RefArea = ChatInputArea.find_element(*Locators.DirectChatPage.REFERENCE_STRIP_AREA)
                if RefArea.is_displayed():
                    print("Reference strip Displayed")
                    RefMessage = ChatInputArea.find_element(*Locators.DirectChatPage.REFERENCE_STRIP_MESSAGE_TEXT)
                    if RefMessage.text == expected_message:
                        print("message Appears in Reply Strip")
                        self.screenshot_and_attach_report(Locators.DirectChatPage.INPUT_AREA, "ReferenceStrip_ChatEditor",
                                                          "ReferenceStrip_ChatEditor")

                    else:
                        print("message not appears in Reply Strip")
                        self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "ReferenceStrip_ChatEditor",
                                                          "ReferenceStrip_ChatEditor")

            except NoSuchElementException:
                print("Reference strip not added")
                self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "ReferenceStrip_ChatEditor",
                                                  "ReferenceStrip_ChatEditor")
        elif dc_file_message == "file":
            try:
                ChatInputArea = self.get_element(Locators.DirectChatPage.INPUT_AREA)
                RefArea = ChatInputArea.find_element(*Locators.DirectChatPage.REFERENCE_STRIP_AREA)
                if RefArea.is_displayed():
                    print("Reference strip Displayed")
                    RefMessage = ChatInputArea.find_element(*Locators.DirectChatPage.REFERENCE_STRIP_FILE_TEXT)
                    if RefMessage.text == expected_message:
                        print("message Appears in Reply Strip")
                        self.screenshot_and_attach_report(ChatInputArea, "ReferenceStrip_ChatEditor",
                                                          "ReferenceStrip_ChatEditor")

                    else:
                        print("message not appears in Reply Strip")
                        self.screenshot_and_attach_report(ChatInputArea, "ReferenceStrip_ChatEditor",
                                                          "ReferenceStrip_ChatEditor")
            except NoSuchElementException:
                print("Reference strip not added")
                self.screenshot_and_attach_report(DcTabLayout, "ReferenceStrip_ChatEditor",
                                                  "ReferenceStrip_ChatEditor")

    def reply_strip_message(self, expected_message):
        DcTabLayout = self.get_element(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA)
        lMessage_area = DcTabLayout.find_element(*Locators.DirectChatPage.MESSAGES_AREA)
        MessageList = lMessage_area.find_elements(*Locators.DirectChatPage.MESSAGE_LISTS)
        found_message = None
        for eachMessage in reversed(MessageList):
            if eachMessage.text == expected_message:
                # logger.info("Last sent message "+ele.text+ " exists")
                found_message = eachMessage
                Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                Reply_Strip_item = Message_item.find_element(*Locators.DirectChatPage.REFERENCE_STRIP_CONTAINER)
                if Reply_Strip_item.is_displayed():
                    print("Last sent message " + eachMessage.text + " exists")
                    self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "DC_Message", "Last sent message exists")
                else:
                    print("Reply Strip not added")
                    self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA, "DC_Message",
                                                      "Last sent message not exists")
                break
            else:
                # logger.info("Last sent message " + ele.text + " not exists")
                print("Last sent message " + eachMessage.text + " not exists")
                self.screenshot_and_attach_report(*Locators.DirectChatPage.MESSAGES_AREA, "DC_Message",
                                                  "Last sent message " + eachMessage.text + " not exists")
        if found_message is not None:
            print("message available with Reply Strip")
            return found_message

    def verify_reply_strip_message(self, dc_message_reply):
        try:
            found_message = self.reply_strip_message(dc_message_reply)
            if found_message:
                print("DC message with Reply Strip")
                return True
        except NoSuchElementException:
            print("DC message not Received")
            return False

    def click_reply_from_message(self, expected_message):
        found_message = self.last_dc_messages(expected_message)
        if found_message:
            self.hover_on_element(found_message)
            Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
            time.sleep(0.2)
            Message_item.find_element(*Locators.DirectChatPage.SHOW_ACTIONS_ICON).click()
            time.sleep(0.5)
            overlay = self.get_element(Locators.DirectChatPage.OVERLAY_SHOW_ACTIONS)
            overlay.find_element(*Locators.DirectChatPage.REPLY_BUTTON_SHOW_ACTION).click()
        else:
            print("message Not Found")

    def click_forward_from_message(self, expected_message):
        found_message = self.last_dc_messages(expected_message)
        if found_message:
            self.hover_on_element(found_message)
            Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
            time.sleep(0.2)
            Message_item.find_element(*Locators.DirectChatPage.SHOW_ACTIONS_ICON).click()
            time.sleep(0.5)
            overlay = self.get_element(Locators.DirectChatPage.OVERLAY_SHOW_ACTIONS)
            overlay.find_element(*Locators.DirectChatPage.FORWARD_BUTTON_SHOW_ACTION).click()
        else:
            print("message Not Found")

    def click_forward_option(self):
        forward_icon = self.get_element(Locators.DirectChatPage.MAT_ICONS)
        if forward_icon.text == "arrow_forward":
            forward_icon.find_element(By.XPATH, "./ancestor::button").click()
            time.sleep(1)

    def click_forward_button_dialog(self):
        self.get_element(Locators.DirectChatPage.FORWARD_BUTTON_DIALOG).click()

    def dc_area_screenshot(self):
        DcTabLayout = self.get_element(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA)
        self.screenshot_and_attach_report(DcTabLayout, "DC_Area", "DC_Area")

    # def CopySendMessage_Verify(self, expected_message):
    #     found_message = self.last_dc_messages(expected_message)
    #     if found_message:
    #         self.hover_on_element(found_message)
    #         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
    #         time.sleep(0.2)
    #         Message_item.find_element(*Locators.DirectChatPage.SHOW_ACTIONS_ICON).click()
    #         time.sleep(0.5)
    #         overlay = self.get_element(self.overlay_show_actions)
    #         overlay.find_element(*Locators.DirectChatPage.COPY_BUTTON_SHOW_ACTION).click()
    #         getName = Message_item.find_element(*self.get_name_message).text
    #         print(getName)
    #         getTime = Message_item.find_element(*Locators.DirectChatPage.GET_TIME_MESSAGE).text
    #         print(getTime)
    #         # Get the current date and time
    #         # Get the current date
    #         current_date = datetime.now()
    #         month_name = current_date.strftime("%b")
    #
    #         # Format the date with the first letter of the month in uppercase
    #         formatted_datetime = f"[{current_date.day} {month_name} {current_date.year}, {getTime}]"
    #
    #         print(formatted_datetime)
    #         CopiedMessage = Keys.CONTROL, "v" + Keys.ENTER
    #         self.send_keys(Locators.DirectChatPage.CHAT_EDITOR,CopiedMessage)
    #
    #         time.sleep(1)
    #         message = formatted_datetime + " " + getName + ": " + expected_message
    #         print(message)
    #         date_time, rest_of_text = message.split("]", 1)
    #
    #         # Split the date and time
    #         date, times = date_time.strip("[").split(",")
    #
    #         # Remove the leading zero from the time
    #         time_parts = times.strip().split(":")
    #         hour = str(int(time_parts[0]))  # Convert to integer and back to string to remove leading zero
    #         minute = time_parts[1]
    #
    #         # Reconstruct the modified date and time
    #         new_date_time = f"[{date}, {hour}:{minute}]"
    #
    #         # Combine the modified date and time with the rest of the text
    #         result_text = new_date_time + rest_of_text
    #
    #         print(result_text)
    #         return result_text
    #
    # def verify_dc_message_copy_withTime(self, expected_message):
    #     result_text = self.CopySendMessage_Verify(expected_message)
    #     print(result_text)
    #     found_message = self.last_dc_messages(result_text)
    #     if found_message:
    #         print("Copied message Found")
    #
    #     else:
    #         print("Copied message not found")
    #         pytest.fail("Copied and Pasted DC message not available")

    def copy_sent_message(self, expected_message):
        found_message = self.last_dc_messages(expected_message)
        if found_message:
            action = ActionChains(self.driver)
            action.move_to_element(found_message).perform()
            Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
            time.sleep(0.2)
            Message_item.find_element(*Locators.DirectChatPage.SHOW_ACTIONS_ICON).click()
            time.sleep(0.5)
            overlay = self.get_element(Locators.DirectChatPage.OVERLAY_SHOW_ACTIONS)
            overlay.find_element(*Locators.DirectChatPage.COPY_BUTTON_SHOW_ACTION).click()

    def copy_message_format_message(self, expected_message, user_name, user):
        if user == "sender":
            found_message = self.last_dc_messages(expected_message)
            if found_message:
                action = ActionChains(self.driver)
                action.move_to_element(found_message).perform()
                Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                try:
                    getTime = Message_item.find_element(*Locators.DirectChatPage.GET_TIME_MESSAGE).text
                    print(getTime)
                except NoSuchElementException:
                    getTime = Message_item.find_element(*Locators.DirectChatPage.GET_TIME_HOVER_MESSAGE).text
                    print(getTime)

                current_date = datetime.now()
                month_name = current_date.strftime("%b")

                # Format the date with the first letter of the month in uppercase
                formatted_datetime = f"[{current_date.strftime('%d')} {month_name} {current_date.year}, {getTime}]"

                print(formatted_datetime)
                CopiedMessage = Keys.CONTROL, "v" + Keys.ENTER
                self.send_keys(Locators.DirectChatPage.CHAT_EDITOR, CopiedMessage)
                time.sleep(1)
                message = formatted_datetime + " " + user_name + ": " + expected_message
                print(message)
                date_time, rest_of_text = message.split("]", 1)

                # Split the date and time
                date, times = date_time.strip("[").split(",")

                # Remove the leading zero from the time
                time_parts = times.strip().split(":")
                hour = str(int(time_parts[0]))  # Convert to integer and back to string to remove leading zero
                minute = time_parts[1]

                # Reconstruct the modified date and time
                new_date_time = f"[{date}, {hour}:{minute}]"

                # Combine the modified date and time with the rest of the text
                result_text = new_date_time + rest_of_text
                print("From Func A" + result_text)
                return result_text
        if user == "receiver":
            found_message = self.last_dc_messages(expected_message)
            if found_message is None and self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON).is_displayed():
                self.click(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
                time.sleep(1)
                print("Check scroll to bottom in if block")
                time.sleep(1)
            found_message = self.last_dc_messages(expected_message)
            if found_message:
                action = ActionChains(self.driver)
                action.move_to_element(found_message).perform()
                Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
                try:
                    getTime = Message_item.find_element(*Locators.DirectChatPage.GET_TIME_MESSAGE).text
                    print(getTime)
                except NoSuchElementException:
                    getTime = Message_item.find_element(*Locators.DirectChatPage.GET_TIME_HOVER_MESSAGE).text
                    print(getTime)

                current_date = datetime.now()
                month_name = current_date.strftime("%b")

                # Format the date with the first letter of the month in uppercase
                formatted_datetime = f"[{current_date.strftime('%d')} {month_name} {current_date.year}, {getTime}]"

                print(formatted_datetime)
                message = formatted_datetime + " " + user_name + ": " + expected_message
                print(message)
                date_time, rest_of_text = message.split("]", 1)

                # Split the date and time
                date, times = date_time.strip("[").split(",")

                # Remove the leading zero from the time
                time_parts = times.strip().split(":")
                hour = str(int(time_parts[0]))  # Convert to integer and back to string to remove leading zero
                minute = time_parts[1]

                # Reconstruct the modified date and time
                new_date_time = f"[{date}, {hour}:{minute}]"

                # Combine the modified date and time with the rest of the text
                result_text = new_date_time + rest_of_text
                print("From Func A" + result_text)
                return result_text

    def verify_copied_dc_message(self, expected_message, user_name, user_type):
        if user_type == "sender":
            self.copy_sent_message(expected_message)
            result_text = self.copy_message_format_message(expected_message, user_name, user_type)
            print(result_text)
            found_message = self.last_dc_messages(result_text)
            if found_message:
                print("Copied message Found")
                return True
            else:
                print("Copied message not found")
                return False
        elif user_type == "receiver":
            result_text = self.copy_message_format_message(expected_message, user_name, user_type)
            print(result_text)
            found_message = self.last_dc_messages(result_text)
            if found_message:
                print("Copied message Found")
                return True
            else:
                print("Copied message not found")
                return False

    def verify_new_messages_strip(self):
        NewMessageStripClass = self.get_element(Locators.DirectChatPage.NEW_MESSAGE_STRIP)
        self.get_element(Locators.DirectChatPage.MESSAGES_AREA)
        GetNewMessageStripText = NewMessageStripClass.text
        if GetNewMessageStripText == "NEW MESSAGES":
            print("New Messages Strip exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.NEW_MESSAGE_STRIP,
                                              "New_Messages_Strip", "New_Messages_Strip")
        else:
            print("New Messages Strip not exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.MESSAGES_AREA, "New_Messages_Strip_not_exists",
                                              "New_Messages_Strip_not_exists")

    def verify_received_messages_with_new_messages_strip(self, message_count, dc_message):
        try:
            found_message = self.last_dc_messages(dc_message)
            if found_message:
                print("DC message Received")
                if message_count == "one":
                    self.verify_new_message_strip()
                elif message_count == "morethanone":
                    self.verify_new_messages_strip()
                return True
        except NoSuchElementException:
            print("DC message not Received")
            # pytest.fail(dc_message + " , This DC message is not available")
            return False

    def new_messages_strip_return(self):
        NewMessageStripClass = self.get_element(Locators.DirectChatPage.NEW_MESSAGE_STRIP)
        return NewMessageStripClass

    def scroll_to_bottom_return(self):
        ScrollToBottomClass = self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
        return ScrollToBottomClass

    def verify_new_message_strip(self):
        NewMessageStripClass = self.get_element(Locators.DirectChatPage.NEW_MESSAGE_STRIP)
        self.get_element(Locators.DirectChatPage.MESSAGES_AREA)
        GetNewMessageStripText = NewMessageStripClass.text
        if GetNewMessageStripText == "NEW MESSAGE":
            print("New message Strip exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.NEW_MESSAGE_STRIP, "New_Messages_Strip", "New_Messages_Strip")
        else:
            print("New message Strip not exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.MESSAGES_AREA, "New_Messages_Strip_not_exists",
                                              "New_Messages_Strip_not_exists")

    def verify_scroll_to_bottom_icon(self):
        ScrollToBottom = self.get_element(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON)
        self.get_element(Locators.DirectChatPage.MESSAGES_AREA)
        if ScrollToBottom.is_displayed():
            print("Scroll to Bottom icon exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.SCROLL_TO_BOTTOM_ICON, "ScrollToBottom_Icon", "ScrollToBottom_Icon")
            return True
        else:
            print("Scroll to Bottom icon not exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.MESSAGES_AREA, "ScrollToBottom_Icon", "ScrollToBottom_Icon")
            return False

    def verify_search_text_box_exists(self):
        try:
            search_text_box_container = self.get_element(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER)
            if search_text_box_container.is_displayed():
                print("Search Text Box Exists")
                self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER, "Search_Text_Box_Exists",
                                                  "SearchTextBoxExists")
                return True
        except NoSuchElementException:
            print("Search Text Box Not Exists")
            self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER,"Search_Text_Box_Not_Exists",
                                              "SearchTextBoxNotExists")
            return False

    def verify_search_text_box_not_exists(self):
        try:
            search_text_box_container = self.get_element(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER)
            if search_text_box_container.is_displayed():
                print("Search Text Box Exists for Fresh DC")
                self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER, "Search_Text_Box_Exists",
                                                  "SearchTextBoxExists")
                return False
        except NoSuchElementException:
            print("Search Text Box Not Exists for Fresh DC")
            self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER,"Search_Text_Box_Not_Exists",
                                              "SearchTextBoxNotExists")
            return True

    # Date: 26.1.24
    # Author : Surya
    def click_search_text_box(self):
        try:
            search_text_box_container = self.get_element(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER)
            search_text_box_input = search_text_box_container.find_element(*Locators.DirectChatPage.SEARCH_INPUT_TEXTBOX)
            search_text_box_input.click()
        except NoSuchElementException:
            print("Search Text Box Not Found")

    def verify_search_text_box_focused(self):
        search_text_box_container = self.get_element(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER)
        search_text_box_input = search_text_box_container.find_element(*Locators.DirectChatPage.SEARCH_INPUT_TEXTBOX)
        # search_text_box_input.click()
        is_active_element = search_text_box_input == self.driver.switch_to.active_element
        if is_active_element:
            print("The text box is the currently active element")
            self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER, "SearchCursorTextBox",
                                              "Cursor is focused in Search Text Box")
            return True
        else:
            print("The text box is not the currently active element")
            self.screenshot_and_attach_report(Locators.DirectChatPage.DC_TAB_LAYOUT_AREA,
                                              "SearchCursorTextBoxNotFocused",
                                              "Cursor is not focused in Search Text Box")
            return False

    def search_messages(self, message):
        try:
            search_text_box_container = self.get_element(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER)
            search_text_box_container.find_element(*Locators.DirectChatPage.SEARCH_INPUT_TEXTBOX).send_keys(message)
            self.click(Locators.DirectChatPage.SEARCH_ICON)
            time.sleep(0.2)
            self.wait_for_element_disappears(Locators.DirectChatPage.SEARCH_LOADING_ICON)
            Search_messages_hint = self.get_text(Locators.DirectChatPage.SEARCH_MESSAGES_FOUND_HINT)
            if "message(s) found" in Search_messages_hint:
                print("Search progress completed and results appears")
                self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER,
                                                  "Search_Text_Box_Exists",
                                                  "SearchTextBoxExists")
            return True

        except NoSuchElementException:
            print("Search Text Box Not Exists or search results not found")
            self.screenshot_and_attach_report(Locators.DirectChatPage.SEARCH_TEXT_BOX_CONTAINER,"Search_Text_Box_Not_Exists",
                                              "SearchTextBoxNotExists")
            return False

