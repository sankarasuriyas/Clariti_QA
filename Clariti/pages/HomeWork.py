import datetime
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Clariti.pages.base_page import BasePage, random_string
from Clariti.utilities.customlogger import LogGen


class MailPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self, driver, homePageInstance):
        super().__init__(driver)
        self.driver = driver

    table_body = (By.XPATH, '//*[contains(@id, "cdk-drop-list-")]')
    rows = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-row'}']")
    rowsLoading = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-row row-loading'}']")
    subject_class = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrivetablecell-textname'}']")
    participant_class = (By.CSS_SELECTOR, f"[class*='{'im-sc-ll-participant-host'}']")
    dateSeperatorRow = (By.CSS_SELECTOR, f"[class*='{'im-td-Dateseparator'}']")
    Overlay_Container = (By.CSS_SELECTOR, f"[class*='im-td-detailsoverlay-container']")
    CheckBoxClass = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrivetablecell-checkbox'}']")
    BringSelectedMailsButton = (By.CSS_SELECTOR, f"[class*='{'ok_button'}']")

    AddMailToSendMailsTextClass = (By.CSS_SELECTOR, f"[class*='im-da-dr-warningText']")
    AddMailToSendMailsText = "Add mail account to send mails"

    # Enter Body content in 1st Line.
    DraftBodyText = (By.CSS_SELECTOR, f"[class*='claritioriginalcontent'] br")
    DraftBody = (By.CSS_SELECTOR, f"[class*='claritioriginalcontent']")

    # Updated code with Date seperator row skip check
    # Dated on 22.10.2023
    def get_mail_tab_items(self, subject):
        # Get the table body element
        time.sleep(1)
        table = self.get_element(self.table_body)
        rows = table.find_elements(*self.rows)
        print(len(rows))
        found_row = None
        for row in rows:
            dateSeparator = row.find_elements(*self.dateSeperatorRow)
            if dateSeparator:
                # Skip rows with dateSeperator
                continue
            subject_cell = row.find_element(*self.subject_class)
            if subject_cell:
                if subject == subject_cell.text:
                    print(subject_cell.text)
                    break

    # Select Bring Mails by Verify with SUbject name, say given subject,...
    # Dated on 22.10.2023
    def get_bring_mails_items(self, subject):
        BringMailOverlay = self.get_element(self.Overlay_Container)
        table = self.get_element(self.table_body)
        rows = table.find_elements(*self.rows)
        print(len(rows))
        selected_subjects = []
        for row in rows:
            subject_cell = row.find_element(*self.subject_class)
            if subject == subject_cell.text:
                print(subject_cell.text)
                CheckBox = row.find_element(*self.CheckBoxClass)
                CheckBox.click()
                subject_cell = row.find_element(*self.subject_class)
                subject = subject_cell.text
                selected_subjects.append(subject)
                print(subject)
                break

        BringSelectedMails = BringMailOverlay.find_element(*self.BringSelectedMailsButton)
        BringSelectedMails.click()
        self.wait_for_element_disappears(BringMailOverlay)
        print(1)
        time.sleep(5)

    # Select Bring Mails by given count to select 1 by 1,,...
    # Dated on 22.10.2023
    def get_bring_mails_items_random(self, SelectCount):
        BringMailOverlay = self.get_element(self.Overlay_Container)
        table = self.get_element(self.table_body)
        rows = table.find_elements(*self.rows)
        print(len(rows))
        selected_subjects = []
        for row in rows:
            if SelectCount > 0:
                CheckBox = row.find_element(*self.CheckBoxClass)
                CheckBox.click()
                subject_cell = row.find_element(*self.subject_class)
                subject = subject_cell.text
                selected_subjects.append(subject)
                print(subject)
                SelectCount -= 1
        BringSelectedMails = BringMailOverlay.find_element(*self.BringSelectedMailsButton)
        BringSelectedMails.click()

        self.wait_for_element_disappears(BringMailOverlay)
        print(1)
        time.sleep(5)

    # Verify Add Mail account to send Mails,.
    # Dated on 23.10.2023
    def verifyAddMailToSendMails(self):
        AddText = self.get_element(self.AddMailToSendMailsTextClass)
        inner_html = AddText.get_attribute("innerHTML")
        # Parse the inner HTML with BeautifulSoup
        soup = BeautifulSoup(inner_html, "html.parser")
        # Extract and merge the text from the <a> and <span> elements
        JoinMultiLineText = ' '.join(soup.stripped_strings)
        print(JoinMultiLineText)

        if self.AddMailToSendMailsText in JoinMultiLineText:
            print("Alert info appears")
        else:
            print("Alert not appears")

    # Verify Bold text available in Draft Body,.
    # Dated on 23.10.2023
    def verifyBoldContent(self):
        BodyContent = self.get_element(self.DraftBody)
        if BodyContent:
            try:
                bold_tag = BodyContent.find_element(By.TAG_NAME, 'b')
                if bold_tag:
                    print("Bold Exists")
            except:
                print("Bold Not Exists")

