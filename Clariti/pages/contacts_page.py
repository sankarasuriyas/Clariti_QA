import time
import allure
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Clariti.pages.base_page import BasePage, random_string
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.locators import Locators


def take_element_screenshot(element, file_name):
    element.screenshot(file_name)


class ContactsPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.Keys = None
        self.driver = driver

    # CLARITI_FULL_VIEW = (By.CSS_SELECTOR, f"[class*='im-app-left-splitter']")
    # DIRECT_CHAT_TAB = (By.XPATH, "//div[@class='im-ct-menu-title im-ct-contacts-header' and text()='Contacts']")
    # SEARCH_TEXTBOX = (By.XPATH, "//input[contains(@class, 'im-pa-mc-contactsearch-searchTextBox')]")
    # NO_CONTACTS_FOUND_ALERT = (By.XPATH, '//*[contains(@class, "im-pa-mc-no-contacts")]')
    #
    # TABLE_BODY = (By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
    # ROWS = (By.CSS_SELECTOR, f"[class*='{'im-table-row ng-star-inserted'}']")
    # SUBJECT_CLASS = (By.CSS_SELECTOR, f"[class*='{'im-pa-mc-contact-textname'}']")
    # CONTEXT_AREA = (By.CSS_SELECTOR, f"[class*='{'im-ct-items ps'}']")
    # CONTACT_TABLE = (By.CSS_SELECTOR, f"[class*='{'im-pa-mc-mycontainer'}']")
    # SCROLL_CLASS = (By.CSS_SELECTOR, f"[class*='{'ps--active-y'}']")
    # SCROLLBAR = (By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
    # ROW_ACTIONS = (By.CLASS_NAME, "im-pa-mc-hoveroverlayer-hoverButtonContainer")
    #
    # DC_HEADER = (By.XPATH, "//*[contains(@class, 'im-dctab-headerroot')]")
    # CHAT_EDITOR = (By.CSS_SELECTOR, f"[class*='{'im-da-ch-textarea editable-element'}']")
    # DC_TAB_AREA_LAYOUT = (By.XPATH, "//*[contains(@class, 'im-td-directchattablayout-root')]")
    # DC_TAB_LAYOUT = (By.XPATH, "//*[contains(@class, 'im-td-directchattablayout-body')]")
    # DC_MESSAGE_AREA = (By.XPATH, "//*[contains(@class, 'im-da-ch-marginTop')]")
    # DC_MESSAGE = (By.CSS_SELECTOR, "[class*='im-da-ch-msg-text ng-star-inserted']")
    # DC_FILE = (By.CSS_SELECTOR, "[class*='attachImgIcon-fileName']")
    # INPUT_AREA = (By.CLASS_NAME, "im-da-ch-inputcontainer")
    # SVG_ICONS = (By.TAG_NAME, "svg")
    # SVG_ICON_CONTACT_ROW_ACTION = (By.TAG_NAME, "im-sc-svgicon")
    #
    # OVERLAY_CONTAINER = (By.CSS_SELECTOR, f"[class*='im-td-detailsoverlay-container']")
    # BLOCK_BUTTON = (By.CSS_SELECTOR, "[class*='im-pa-mc-contactedit-deleteBtn']")
    #
    # DIALOG_CONTAINER = (By.CSS_SELECTOR, f"[class*='{'im-pa-mc-blockchatcontactalert-confirmationDialog'}']")
    # # YES_BUTTON = (By.XPATH, "//button/span[(text(),'Yes')]")
    # YES_BUTTON = (By.XPATH, "//button[contains(., 'Yes')]")
    #
    # DC_CONTACTS_UNDER_DIRECT_CHAT = (By.CLASS_NAME, "im-ct-contacts-pinned")
    # DC_CONTACTS_AREA = (By.CSS_SELECTOR, f"[class*='{'im-ct-pinnedcontacts-contactcontainer'}']")
    # DC_CONTACT_NAME_AREA = (By.CSS_SELECTOR, f"[class*='{'im-sc-participant-myChatContact'}']")
    #
    # MINI_CONTACT_LIST_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-list'}']")  # Updated from im-pa-mc-minicontactlist-itemlist
    # CONTACT_LIST_OVERLAY = (By.CSS_SELECTOR, "[class*='im-sc-participant-myChatContact']")
    # MINI_CONTACT_CONTAINER_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-container'}']")  # Updated from im-pa-mc-minicontactlist-container
    # MINI_CONTACT_CONTAINER_MAIN_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'im-pa-sh-mpw-body'}']")
    # ADD_CONTACT_LIST_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'im-shareitems-contacttable'}']")
    # SCROLL_AREA_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'ps__rail-y'}']")  # Updated from ps--active-y
    # SCROLL_BAR_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
    # CONTACT_CLICK_OVERLAY = (By.CSS_SELECTOR, 'button[type="button"]')
    #
    # ADD_INVITE_BUTTON_DIRECT_CHAT = (By.CSS_SELECTOR, f"[class*='{'im-ct-contacts-invitationstatus'}']")
    # SEARCH_CHAT_BUTTON = (By.CSS_SELECTOR, f"[class*='{'im-pa-iv-clariti-contacts-section'}']")
    # SEARCH_TEXT_BOX = (By.XPATH, "//input[contains(@class, 'im-uc-searchinput')]")
    # CHAT_BUTTON = (By.CSS_SELECTOR, f"[class*='{'invite-buttons'}']")
    # CHECKBOX_SELECTION_OVERLAY = (By.CSS_SELECTOR, f"[class*='{'im-td-item-checkbox'}']")
    # ADD_CONTACT_BUTTON = (By.CSS_SELECTOR, f"[class*='{'im-shareitems-sharebtn'}']")
    # PAYMENT_UPGRADE_CONTAINER = (By.CSS_SELECTOR, f"[class*='{'im-sh-paymentupgrade-container'}']")
    # SVG_ICON = (By.TAG_NAME, "im-sc-svgicon")
    # DC_TAB_HEADER = (By.CSS_SELECTOR, f"[class*='im-dctab-headerroot']")

    def add_contact(self, contact):
        self.click(Locators.ContactsPage.ADD_INVITE_BUTTON_DIRECT_CHAT)
        self.click(Locators.ContactsPage.SEARCH_CHAT_BUTTON)
        time.sleep(0.5)
        self.send_keys(Locators.ContactsPage.SEARCH_TEXT_BOX, contact)
        self.click(Locators.ContactsPage.CHAT_BUTTON)
        self.wait_for_element(Locators.ContactsPage.CHAT_EDITOR)

    # Date: 8.12.2023
    # Author: Suriya
    def verify_contact_added_and_dc_focused(self, contact):
        try:
            self.add_contact(contact)
            contactName = self.get_text(Locators.ContactsPage.DC_TAB_HEADER)
            if contactName == contact:
                print("Contact Added and DC tab Focused")
                self.screenshot_and_attach_report(Locators.ContactsPage.CLARITI_FULL_VIEW, "DCTabFocused",
                                                  "Verify contact added and DC Focused")
                return True
        except NoSuchElementException:
            print("Contact Not Added or DC tab Focused")
            self.screenshot_and_attach_report(Locators.ContactsPage.CLARITI_FULL_VIEW, "DCTabNotFocused",
                                              "Verify contact added and DC Focused or Not")
            return False

    def click_contacts_tab(self):
        self.click(Locators.ContactsPage.DIRECT_CHAT_TAB)

    def contact_search_textbox(self, contact_name):
        self.send_keys(Locators.ContactsPage.SEARCH_TEXTBOX, contact_name)

    def get_contact_direct_chat_tab_using_scroll(self, contact_name):
        generated_string = random_string(5)
        # Get the table body element
        self.wait_for_element(Locators.ContactsPage.TABLE_BODY)
        table = self.get_element(Locators.ContactsPage.TABLE_BODY)

        # Initialize a variable to store the found row
        found_row = None
        max_scrolls = 20  # Maximum number of scrolls
        scroll_count = 0
        while found_row is None and scroll_count < max_scrolls:
            rows = table.find_elements(*Locators.ContactsPage.ROWS)

            # Iterate over the ROWS and check the conditions
            for row in rows:
                # print(len(ROWS))
                # Get the subject cell
                subject_cell = row.find_elements(*Locators.ContactsPage.SUBJECT_CLASS)
                for cell in subject_cell:
                    if cell.text == contact_name:
                        found_row = row
                        screenshot_path = ".//Screenshots/"+generated_string+" contact.png"
                        take_element_screenshot(row, screenshot_path)
                        allure.attach.file(screenshot_path, name="Contact_Exists", attachment_type=allure.attachment_type.PNG)
                        break
                if found_row is not None:
                    return found_row

            if found_row is None and len(rows) > 18:
                action_chains = ActionChains(self.driver)
                action_chains.move_to_element(self.get_element(Locators.ContactsPage.TABLE_BODY)).perform()
                action_chains.send_keys(Keys.PAGE_DOWN).perform()
                time.sleep(1)
                CONTACT_TABLE = self.get_element(Locators.ContactsPage.CONTACT_TABLE)
                Scroll_area = CONTACT_TABLE.find_element(*Locators.ContactsPage.SCROLL_CLASS)
                SCROLLBAR_icon = Scroll_area.find_element(*Locators.ContactsPage.SCROLLBAR)
                action_chains.move_to_element(SCROLLBAR_icon).click_and_hold().move_by_offset(0, -3).release().perform()
                scroll_count += 1
                return found_row
            elif found_row is None:
                print("Less contacts without SCROLLBAR and Proceed")
                # return found_row
                break
        if found_row is None:
            print("contact not found")
            screenshot_path = ".//Screenshots/" + generated_string + " contact.png"
            take_element_screenshot(table, screenshot_path)
            allure.attach.file(screenshot_path, name="Contact_Not_Exists", attachment_type=allure.attachment_type.PNG)
            return None

    def click_contact_using_scroll(self, UserB_name):
        foundContact = self.get_contact_direct_chat_tab_using_scroll(UserB_name)
        if foundContact:
            print("contact Exists")
            foundContact.click()
        else:
            print("contact not exists")
            pytest.fail("Contact not exists")
        time.sleep(1)

    def verify_dc_contact_in_contacts_tab(self, contact_name):
        found_row = self.get_contact_direct_chat_tab_using_scroll(contact_name)
        if found_row:
            print("contact Present in Direct Chat tab")
        else:
            print("contact not Present in Direct chat tab")
            pytest.fail("contact not Present in Direct Chat tab!!!")

    def verify_dc_contact_not_exists_in_contacts_tab(self, contact_name):
        found_row = self.get_contact_direct_chat_tab_using_scroll(contact_name)
        if not found_row:
            print("contact not Present in Direct Chat tab")
        else:
            print("contact Found in Direct Chat tab")
            pytest.fail("contact exists in Direct Chat tab!!!")

    def click_visiting_card(self, contact_name):
        found_row = self.get_contact_direct_chat_tab_using_scroll(contact_name)
        if found_row:
            found = found_row.find_element(*Locators.ContactsPage.ROW_ACTIONS)
            SVG_ICON = found.find_elements(*Locators.ContactsPage.SVG_ICON)
            first_icon = SVG_ICON[1]
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(first_icon).perform()
            first_icon.click()
            return found_row
        elif found_row is None:
            print("contact Not Found to Block")
            return found_row

    def block_contact(self, contact_name):
        # self.click_contacts_tab()
        time.sleep(1)
        found_row = self.click_visiting_card(contact_name)
        if found_row:
            self.click(Locators.ContactsPage.BLOCK_BUTTON)
            self.click(Locators.ContactsPage.YES_BUTTON)
            self.wait_for_element_disappears(Locators.ContactsPage.OVERLAY_CONTAINER)

    def select_contact_direct_chat_tab_search(self, contact_name):
        self.contact_search_textbox(contact_name)
        time.sleep(1)

        # Get the table body element
        try:
            table = self.get_element(Locators.ContactsPage.TABLE_BODY)
            if table.is_displayed():

                # Initialize a variable to store the found row
                found_row = None
                while found_row is None:
                    ROWS = table.find_elements(*Locators.ContactsPage.ROWS)

                    # Iterate over the ROWS and check the conditions
                    for row in ROWS:
                        # Get the subject cell
                        subject_cell = row.find_elements(*Locators.ContactsPage.SUBJECT_CLASS)
                        for cell in subject_cell:
                            if cell.text == contact_name:
                                found_row = row
                                row.click()
                                break
                        if found_row is not None:
                            return found_row

                if found_row is None:
                    print("contact not found")
                    return None
        except NoSuchElementException:
            NoContacts = self.get_element(Locators.ContactsPage.NO_CONTACTS_FOUND_ALERT)
            if NoContacts.is_displayed():
                print("No Contacts found Alert appears")

    def contact_selection_from_overlay(self, contact_name):
        # Get the table body element
        try:
            table = self.get_element(Locators.ContactsPage.TABLE_BODY)
            if table.is_displayed():

                # Initialize a variable to store the found row
                found_row = None
                while found_row is None:
                    ROWS = table.find_elements(*Locators.ContactsPage.ROWS)

                    # Iterate over the ROWS and check the conditions
                    for row in ROWS:
                        # Get the subject cell
                        subject_cell = row.find_elements(*Locators.ContactsPage.SUBJECT_CLASS)
                        for cell in subject_cell:
                            if cell.text == contact_name:
                                found_row = row
                                break
                        if found_row is not None:
                            return found_row

                if found_row is None:
                    print("contact not found")
                    return None
        except NoSuchElementException:
            NoContacts = self.get_element(Locators.ContactsPage.NO_CONTACTS_FOUND_ALERT)
            if NoContacts.is_displayed():
                print("No Contacts found Alert appears")

    def select_contact_from_overlay(self, contact_name):
        found_row = self.contact_selection_from_overlay(contact_name)
        base_tr = found_row.find_element(By.XPATH, ".//ancestor::tr")
        base_tr.find_element(*Locators.ContactsPage.CHECKBOX_SELECTION_OVERLAY).click()
        time.sleep(1)
        self.click(Locators.ContactsPage.ADD_CONTACT_BUTTON)
        time.sleep(1)

    def contact_visible_in_overlay(self, contact_name):
        try:
            table = self.get_element(Locators.ContactsPage.TABLE_BODY)
            if table.is_displayed():
                # Initialize a variable to store the found row
                found_row = None
                while found_row is None:
                    ROWS = table.find_elements(*Locators.ContactsPage.ROWS)
                    # Iterate over the ROWS and check the conditions
                    for row in ROWS:
                        # Get the subject cell
                        subject_cell = row.find_elements(*Locators.ContactsPage.SUBJECT_CLASS)
                        for cell in subject_cell:
                            if cell.text.lower() == contact_name.lower():
                                found_row = row
                                return found_row
                        if found_row is not None:
                            return found_row
                    return False
                if found_row is None:
                    print("contact not found")
                    return None
        except NoSuchElementException:
            NoContacts = self.get_element(Locators.ContactsPage.NO_CONTACTS_FOUND_ALERT)
            if NoContacts.is_displayed():
                print("No Contacts found Alert appears")
                return None

    def contact_scroll_in_overlay(self, contact_list):
        ContactListContainer = self.get_element(Locators.ContactsPage.ADD_CONTACT_LIST_OVERLAY)
        ScrollClass = ContactListContainer.find_element(*Locators.ContactsPage.SCROLL_CLASS)
        SCROLLBAR = ScrollClass.find_element(*Locators.ContactsPage.SCROLLBAR)
        # Create an ActionChains instance
        actions = ActionChains(self.driver)
        tableBody = self.get_element(Locators.ContactsPage.TABLE_BODY)
        actions.move_to_element(self.driver.find_element(tableBody)).perform()
        # Hover over the SCROLLBAR element and perform the scroll action
        actions.move_to_element(SCROLLBAR).click_and_hold().move_by_offset(0, 25).release().perform()
        # Wait for a new element to be present
        WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(tableBody))
        actions.move_to_element(SCROLLBAR).click_and_hold().move_by_offset(0, 3).release().perform()
        # Find the updated contact list element
        contact_list = self.get_element(Locators.ContactsPage.TABLE_BODY)
        print("contact list updated")
        # Return the updated contact list element
        return contact_list

    def check_contact_visibility_in_overlay(self, contact_name):
        visible = self.contact_visible_in_overlay(contact_name)
        contact_list = self.get_element(Locators.ContactsPage.TABLE_BODY)
        previous_contact_list_text = contact_list.text
        # Find the parent element containing the contacts
        contact_list = self.get_element(Locators.ContactsPage.TABLE_BODY)
        while not visible:
            self.contact_scroll_in_overlay(contact_list)
            contact_list1 = self.get_element(Locators.ContactsPage.TABLE_BODY)
            current_contact_list_text = contact_list1.text

            if current_contact_list_text == previous_contact_list_text:
                print("No contact exists")
                break
            visible = self.contact_visible_in_overlay(contact_name)
            visible1 = self.contact_visible_in_overlay(contact_name)
            if visible:
                base_tr = visible1.find_element(By.XPATH, ".//ancestor::tr")
                base_tr.find_element(*Locators.ContactsPage.CHECKBOX_SELECTION_OVERLAY).click()
                time.sleep(1)
                self.click(Locators.ContactsPage.ADD_CONTACT_BUTTON)
                time.sleep(1)
                return True
            previous_contact_list_text = current_contact_list_text

    def select_add_contact_from_overlay(self, contact_name):
        visible = self.contact_visible_in_overlay(contact_name)
        visible1 = self.contact_visible_in_overlay(contact_name)
        if visible:
            print("Visible")
            base_tr = visible1.find_element(By.XPATH, ".//ancestor::tr")
            base_tr.find_element(*Locators.ContactsPage.CHECKBOX_SELECTION_OVERLAY).click()
            try:
                if self.get_element(Locators.ContactsPage.PAYMENT_UPGRADE_CONTAINER).is_displayed():
                    time.sleep(1)
                    self.screenshot_and_attach_report(Locators.ContactsPage.PAYMENT_UPGRADE_CONTAINER, "PaymentUpgradeAlertAppears",
                                                      "Verify Payment Upgrade Alert Appears After Adding Support Contact")
                    return True
            except NoSuchElementException:
                print("Proceeds")
            self.click(Locators.ContactsPage.ADD_CONTACT_BUTTON)
            time.sleep(1)
            return True
        # If not visible, scroll down and check again
        if not visible:
            visible = self.check_contact_visibility_in_overlay(contact_name)
            if visible:
                print("Scroll and Visible")
                return True
            if not visible:
                print("FAIL")
                return False
        time.sleep(1)

    def is_contact_visible(self, contact_name):
        contact_list = self.get_element(Locators.ContactsPage.MINI_CONTACT_LIST_OVERLAY)
        contact_elements = contact_list.find_elements(*Locators.ContactsPage.CONTACT_LIST_OVERLAY)
        for element in contact_elements:
            # co=element.text
            # print(co)
            # if contact_name.lower() in co.lower():
            if element.text.lower() == contact_name.lower():
                # print(element)
                element.click()
                return True
        return False

    # This function used in contact_selection_ip_chat
    def hover_and_scroll(self, contact_list):
        # Find the SCROLLBAR element
        ContactMiniContainer = self.get_element(Locators.ContactsPage.MINI_CONTACT_CONTAINER_MAIN_OVERLAY)
        ScrollClass = ContactMiniContainer.find_element(*Locators.ContactsPage.SCROLL_AREA_OVERLAY)
        SCROLLBAR = ScrollClass.find_element(*Locators.ContactsPage.SCROLL_BAR_OVERLAY)

        # Create an ActionChains instance
        actions = ActionChains(self.driver)

        # Hover over the SCROLLBAR element and perform the scroll action
        actions.move_to_element(SCROLLBAR).click_and_hold().move_by_offset(0, 30).release().perform()
        # time.sleep(3)

        # Wait for a new element to be present
        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located(Locators.ContactsPage.MINI_CONTACT_LIST_OVERLAY))

        actions.move_to_element(SCROLLBAR).click_and_hold().move_by_offset(0, 3).release().perform()

        # Find the updated contact list element
        contact_list = self.get_element(Locators.ContactsPage.MINI_CONTACT_LIST_OVERLAY)
        print("contact list updated")
        con = contact_list.text
        # print(con)
        # Return the updated contact list element
        return contact_list

    # This function used in contact_selection_ip_chat
    def check_contact_visibility(self, contact_name):
        visible = self.is_contact_visible(contact_name)
        contact_list = self.get_element(Locators.ContactsPage.MINI_CONTACT_LIST_OVERLAY)
        previous_contact_list_text = contact_list.text
        # Find the parent element containing the contacts
        contact_list = self.get_element(Locators.ContactsPage.MINI_CONTACT_LIST_OVERLAY)

        while not visible:
            self.hover_and_scroll(contact_list)
            contact_list1 = self.get_element(Locators.ContactsPage.MINI_CONTACT_LIST_OVERLAY)
            current_contact_list_text = contact_list1.text

            if current_contact_list_text == previous_contact_list_text:
                print("No contact exists")
                break

            c = contact_list1.text
            # print(c)
            visible = self.is_contact_visible(contact_name)
            previous_contact_list_text = current_contact_list_text

    def contact_selection_dialog(self, contact_name):
        visible = self.is_contact_visible(contact_name)

        # If not visible, scroll down and check again
        if not visible:
            self.check_contact_visibility(contact_name)

        time.sleep(1)
        # self.click(Locators.ContactsPage.CONTACT_CLICK_OVERLAY)

    def proceed_button_overlay(self):
        self.click(Locators.ContactsPage.CONTACT_CLICK_OVERLAY)
