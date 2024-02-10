import random
import re
from datetime import datetime
import datetime
from datetime import datetime

import os
import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui as pyautogui
import pytest
from allure_commons.types import AttachmentType
from bs4 import BeautifulSoup
from pynput import mouse
from selenium.webdriver.common import keys
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController, Button
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    NoSuchWindowException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from Clariti.pages.base_page import take_element_screenshot, random_string, upload_files, focus_window_by_title
from Clariti.pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8866")
# chrome_options.add_experimental_option("--auto-open-devtools-for-tabs", "localhost:6500")
driver = webdriver.Chrome(options=chrome_options)

# NewComposeMailicon_Home(driver)

# driver.get("https://qa.clariti.app/")
print("Loaded")

# searchTextBox = driver.find_element(By.CSS_SELECTOR,f"[class='{'im-da-ch-dc-search'}']")
# searchTextBox.find_element(By.TAG_NAME,"input").send_keys("SAM")
# driver.find_element(By.CSS_SELECTOR,f"[class='{'im-da-ch-dc-searchActions'}']").click()
# time.sleep(0.5)
# Loading = driver.find_element(By.CSS_SELECTOR,f"[class='{'im-se-search-inProgress'}']")
# WebDriverWait(driver,10).until(EC.invisibility_of_element_located(Loading))
# get_text = driver.find_element(By.CSS_SELECTOR, f"[class*='{'bottom-align hint'}']").text
# print(get_text)
# if "message(s) found" in get_text:
#     print("Pass")
# else:
#     print("Fail")
# HeaderOperation = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-em-spamText'}']")
# OperationHeader = HeaderOperation.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-th-trashOperationIcon'}']")
# OperationHeader.click()


# def verify_enter_valid_email_address_alert_reply_to():
#     # self.click_reply_to_option()
#     driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-replyto'] input").send_keys(random_string(6))
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-okBtn']").click()
#     try:
#         ReplyTo_dialog = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-parentContainer']")
#         Alert = ReplyTo_dialog.find_element(By.CSS_SELECTOR, f"[class*='mat-mdc-form-field-error']")
#         if Alert.text == "Enter valid mail address":
#             print("Enter valid mail address Alert Appears")
#             time.sleep(0.5)
#
#     except NoSuchElementException:
#         print("Enter valid mail address Alert not Appears")
#         time.sleep(0.5)
#
#
# verify_enter_valid_email_address_alert_reply_to()
# print("1")
# Tooltip = driver.find_element(By.CLASS_NAME, "claritioriginalcontent").text
# print(Tooltip)
# if "Sent using Clariti" == Tooltip:
#     print("Text appears")
# else:
#     print("Text not appears")
# DcTabLayout = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-dc-scrollContainer'}']")
# lMessage_area = DcTabLayout.find_element(By.XPATH, "//*[contains(@class, 'im-da-ch-marginTop')]")
# MessageList = lMessage_area.find_elements(By.CSS_SELECTOR, "[class*='im-da-ch-msg-text ng-star-inserted']")
# found_message = None
# for eachMessage in reversed(MessageList):
#     print("1")
#     if "[09 Jan 2024, 10:02] Triad qa9: SAd," in eachMessage.text:
#         found_message = eachMessage
#         found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         print("2")
#         action = ActionChains(driver)
#         action.move_to_element(found_message).perform()
#         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         try:
#             getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msg-time'}']").text
#             print(getTime)
#         except NoSuchElementException:
#             getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msgNameNotShown'}']").text
#             print(getTime)
#
#         current_date = datetime.now()
#         month_name = current_date.strftime("%b")
#
#         # Format the date with the first letter of the month in uppercase
#         formatted_datetime = f"[{current_date.strftime('%d')} {month_name} {current_date.year}, {getTime}]"
#
#         print(formatted_datetime)
#         message = formatted_datetime + " " + "Triad qa9" + ": " + "[09 Jan 2024, 10:02] Triad qa9: SAd,"
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
#         new_date_time = f"[{date}, {hour}:{minute}]"
#         print(date)
#
#         # Combine the modified date and time with the rest of the text
#         result_text = new_date_time + rest_of_text
#         print("From Func A" + result_text)
# actions = ActionChains(driver)
# DCScrollView = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-dc-scrollContainer'}']")
# scrollbar = DCScrollView.find_element(By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
# actions.move_to_element(DCScrollView).perform()
# time.sleep(1)
# actions.move_to_element(scrollbar).perform()
# # Hover over the scrollbar element and perform the scroll action
# actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 50).release().perform()
# # Wait for a new element to be present
# WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[class*='{'im-da-ch-dc-scrollContainer'}']")))
# driver.refresh()
#actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 3).release().perform()
# Find the updated contact list element


# def get_home_tab_items_includes_seperator(subject):
#     # Get the table body element
#     time.sleep(1)
#     table = driver.find_element(By.XPATH, '//*[contains(@id, "cdk-drop-list-")]')
#     rows = table.find_elements(By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-row isDiscussion'}']")
#     # print(len(rows))
#     found_row = None
#     for row in rows:
#         dateSeparator = row.find_elements(By.CSS_SELECTOR, f"[class*='{'im-td-Dateseparator'}']")
#         if dateSeparator:
#             # Skip rows with dateSeperator
#             continue
#         subject_cell = row.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-cdrivetablecell-textname'}']")
#         if subject_cell:
#             if subject == subject_cell.text:
#                 # print(subject_cell.text)
#                 # The row is found
#                 found_row = subject_cell
#                 # print(found_row.text)
#                 break
#     # Return the found row
#     return found_row
#
#
# found_row = get_home_tab_items_includes_seperator("Sample Mial to create conversation")
# if found_row:
#     print("Cfound")
#     found_row.click()
# else:
#     print("Not found")
# S = driver.find_element(By.CSS_SELECTOR, f"[class='{'im-da-ch-forwardedLabel'}']")
# action = ActionChains(driver)
# action.move_to_element(S).perform()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-tc-startnewcommstrip'}']").click()

# OverlayPane = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-emailtoPos']")
# OverlayPane.find_element(By.CSS_SELECTOR, f"[class*='im-pa-mc-minicontactlist-searchinput']").send_keys("Suriya S QA")
# time.sleep(3)

# MailDraftBody = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerBody']")
# action = ActionChains(driver)
# action.move_to_element(MailDraftBody).perform()
# time.sleep(1)
# ShowEditorToolbarIcon = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftEditorPullDownArrowContainer']")
# ShowEditorToolbarIcon.click()
#
# driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarBold']").click()
# driver.find_element(By.CLASS_NAME, "claritioriginalcontent").send_keys("SAMPLE")

# Parent = driver.find_element(By.CLASS_NAME, "claritioriginalcontent")
# try:
#     if Parent.find_element(By.TAG_NAME, "b"):
#         child_b_element = Parent.find_element(By.TAG_NAME, "b").text
#         print(child_b_element)
# except:
#     print("Element Not Found")

# driver.find_element(By.CSS_SELECTOR, f"[class*='im-ct-email-subtitle']").click()

# try:
#     BringMailOverlay = driver.find_element(By.CSS_SELECTOR,f"[class*='im-td-detailsoverlay-container']")
#     if BringMailOverlay.is_displayed():
#         print("Overlay Opened")
# except:
#     print("Overlay Not opened")
# print(Header)
# if Header == "Mail":
#     print("Mail Tab clickable and opened")
# else:
#     print("Mail tab not opened")

# BringMailOverlay = driver.find_element(By.CSS_SELECTOR,f"[class*='im-td-detailsoverlay-container']")
# BringMailOverlay.find_element(By.XPATH, "//*[@class='card-name' and contains(text(),'Outlook')]").click()
# time.sleep(2)
# current_window = driver.current_window_handle
#
# time.sleep(2)
# try:
#     # wait until handle becomes more than 1
#     WebDriverWait(driver, 20).until(lambda driver: len(driver.window_handles) > 1)
# except TimeoutException or NoSuchWindowException or NoSuchElementException:
#     print("Oauth window not opened due to some Issues ")
#     pytest.fail("Oauth window not opened due to some Issues")
#
# # Get all the window handle
# window_handles = driver.window_handles
#
# # Switch to the new window
# for handle in window_handles:
#     if handle != current_window:
#         driver.switch_to.window(handle)
#         break
# new_handle = driver.current_window_handle
# # Enter Outlook address
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("triadqa1@outlook.com")
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
# time.sleep(2)
#
#
# # Enter Gmail Password
# driver.find_element(By.XPATH, "//input[@name='passwd']").send_keys("Welcome123$")
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
# # focusing to old window handle
# WebDriverWait(driver, 30).until(lambda driver: len(driver.window_handles) == len(window_handles) - 1)
#
# driver.switch_to.window(current_window)
# WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR , f"[class*='im-td-cdrive-tablebody']")))
# Loaidng = driver.find_element(By.CSS_SELECTOR,f"[class*='im-da-cm-progress-statusIconContainer ng-star-inserted']")
#
# WebDriverWait(driver, 30).until(EC.invisibility_of_element(Loaidng))
# time.sleep(2)
# WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR , f"[class*='im-td-cdrive-row']")))
# while True:
#     TableBody = BringMailOverlay.find_element(By.CSS_SELECTOR, f"[class*='im-td-cdrive-tablebody']")
#     Elem = TableBody.find_elements(By.CSS_SELECTOR, f"[class*='im-td-cdrive-row']")
#     if len(Elem) > 3:
#         print("Item Row is greater than 6.")
#         break
#     else:
#         print("Item Row is not yet greater than 6. Waiting...")
#         WebDriverWait(BringMailOverlay, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"[class*='im-td-cdrive-row']")))

# Loaidng = driver.find_element(By.CSS_SELECTOR,f"[class*='im-da-cm-progress-statusIconContainer ng-star-inserted']")
# Loaidng1 = (By.CLASS_NAME, "im-td-cdrive-RowSpinner")
#
# WebDriverWait(driver, 30).until(EC.invisibility_of_element(Loaidng))
# print("1")
# WebDriverWait(driver, 30).until(EC.visibility_of_element_located(Loaidng1))
# print("2")
# WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(Loaidng1))
# print("3")


# (By.CSS_SELECTOR, f"[class*='im-pa-mc-minicontactlist-search']").click()

# DraftHeader = driver.find_element(By.CSS_SELECTOR, "[class*='im-da-dr-draftcontainerDraftHeader']")
# RecipientList = driver.find_element(By.CSS_SELECTOR, "[class*='im-da-dr-recipientlistColl']")
#
# # Find all the ToColumn items using XPath
# ToColumn = RecipientList.find_elements(By.XPATH, "//im-da-cm-chipitemlist")
#
#
# # Print the number of ToColumn items
# # print(len(ToColumn))
#
#
# # Define a function to click the link based on the label prefix
# def click_link_by_label_prefix(prefix):
#     label_prefix = DraftHeader.find_elements(By.CSS_SELECTOR, f"[class*='im-da-cm-labelPrefix']")
#     print(len(label_prefix))
#     for prefixs in label_prefix:
#         print(prefixs.text)
#         if prefixs.text == prefix:
#             found_row_full = prefixs.find_element(By.XPATH, "./ancestor::mat-chip-list")
#             found_row_full.find_element(By.CSS_SELECTOR,
#                                         f"[class*='{'im-da-dr-contactsIconContainer'}']").click()  # You may need to adjust the element and action here
#
#
# click_link_by_label_prefix("Bcc")

# Example usage:
# for _ in ToColumn:
#     click_link_by_label_prefix("To")  # Click the link for "To"
#     click_link_by_label_prefix("CC")

# def click_AddPartiipanticon(ToCCBCC):
#     DraftHeader = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-dr-draftcontainerDraftHeader'}']")
#     RecipientList = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-dr-recipientlistColl'}']")
#     ToColumn = RecipientList.find_elements(By.XPATH, "//im-da-cm-chipitemlist")
#     print(len(ToColumn))
#
#     if len(ToColumn)>1:
#         Tolink = DraftHeader.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-cm-labelPrefix'}']").text
#
#
#     if ToCCBCC == "to":
#         Tolink = DraftHeader.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-cm-labelPrefix'}']").text
#         #print(Tolink)
#
#         if Tolink == "To":
#             driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-dr-contactsIconContainer'}']").click()
#     elif ToCCBCC == "cc":
#         Tolink = DraftHeader.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-cm-labelPrefix'}']").text
#         print(Tolink)
#         if Tolink == "Cc":
#             driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-dr-contactsIconContainer'}']").click()
#
# click_AddPartiipanticon("cc")

# driver.find_element(By.XPATH, "//input[@id='passp-field-login']").send_keys("triadqa1@yandex.com")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.XPATH, "//input[@id='passp-field-passwd']").send_keys("Triad@#123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# def get_mail_items(subject):
#     # Get the table body element
#     table = driver.find_element(By.CSS_SELECTOR, ".ns-view-container-desc.mail-MessagesList.js-messages-list")
#
#     # Find all the rows in the table
#     rows = table.find_elements(By.XPATH, "//*[@class='mail-MessageSnippet-Content']")
#
#     for row in rows:
#
#         From_cell = row.find_element(By.CSS_SELECTOR, ".mail-MessageSnippet-Item.mail-MessageSnippet-Item_sender.js-message-snippet-sender")
#         From_address_name = From_cell.find_elements(By.CLASS_NAME, "mail-MessageSnippet-FromText")
#         for item in From_address_name:
#             if subject == item.text:
#                 item.click()
#                 return
# get_mail_items("Clariti Support")
# NewConversationIcon = (By.XPATH, ".//*[contains(text(), 'To-Do')]")
# a= driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-tc-startnewcommstrip'}']")
# a.find_element(By.XPATH, ".//*[contains(text(), 'Call')]").click()
# CalendarOverlay = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-detailsOverlay'}']")
# CalendarOverlay.find_element(By.XPATH, "//button[contains(., 'No')]").click()
# driver.find_element(By.XPATH, "//mat-form-field[contains(@class, 'im-sh-dateComponent-date')]//div//div//div//div[contains(@class, 'im-sh-date-area')]").click()
# driver.find_element(By.XPATH, ".//*[contains(text(), 'To-Do')]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//mat-form-field[contains(@class, 'im-td-todo-subject')]//div//div//div//input[contains(@class, 'mat-input-element')]").send_keys("sadbjgfjsdbghsdbgb")
# date = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-uc-dateComponent-timecontrol'}']")
# date.click()
# # date = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-description-textarea'}']")
# # SubjectTextBox = driver.find_element(By.XPATH, "//mat-form-field[contains(@class, 'im-td-todo-reminder')]//mat-select")
# # SubjectTextBox.click()
# # time.sleep(1)
# # Overlay = driver.find_element(By.CSS_SELECTOR, f"[class*='{'cdk-overlay-pane'}']")
# # OptionClass = Overlay.find_element(By.CSS_SELECTOR, f"[class*='{'ps--active-y'}']")
# # Options = OptionClass.find_elements(By.CSS_SELECTOR, f"[class*='{'material-select-option'}']")
# # for option in Options:
# #     text = option.find_element(By.CSS_SELECTOR, f"[class*='{'mat-option-text'}']").text
# #     if text == "30 Mins":
# #         option.click()
# #         break
#
#
#                 # current_time = datetime.datetime.now()
#                 # # Format the current time as a string (optional)
#                 # current_time_str = current_time.strftime("%H:%M")
#                 # print("Current Time:", current_time_str)
#                 # current_minutes = current_time.minute
#                 # # Define your predefined minute intervals
#                 # minute_intervals = [0, 15, 30, 45]
#                 # # Find the next rounded minute interval
#                 # next_interval = min([x for x in minute_intervals if x > current_minutes])
#                 # # Update your selection based on the rounded minute interval while keeping the same hour
#                 # selected_time = current_time.replace(minute=next_interval, second=0).strftime("%M")
#                 # print("Current Time:", current_time.strftime("%H:%M"))
#                 # print("Selected Time:", selected_time)
#
# current_time = datetime.datetime.now()
#
# # Extract the current hour and minutes
# current_hour = current_time.hour
# current_minutes = current_time.minute
#
# # Define your predefined minute intervals
# minute_intervals = [0, 15, 30, 45]
#
# # Find the next predefined minute interval greater than the current minutes
# next_interval = min([x for x in minute_intervals if x >= current_minutes], default=None)
#
# # If there is no next interval in the current hour, move to the next hour
# if next_interval is None:
#     current_hour += 1
#     next_interval = min(minute_intervals)  # Use the first interval of the next hour
#
# # Ensure the hour stays within the valid range (0-23)
# current_hour %= 24
#
# # Determine AM or PM
# am_pm = 'AM' if current_hour < 12 else 'PM'
#
# # Convert the hour to 12-hour format
# if current_hour == 0:
#     current_hour = 12
# elif current_hour > 12:
#     current_hour -= 12
#
# hour = current_hour
# minutes = next_interval
# am = am_pm
#
# # Calculate the time difference in minutes
# time_difference_minutes = (hour * 60 + minutes) - (current_time.hour * 60 + current_time.minute)
# print(time_difference_minutes)
#
# # Check if the time difference is greater than 15 minutes
# if time_difference_minutes > 15:
#     print("Time difference is greater than 15 minutes.")
# elif 15 > time_difference_minutes > 1:
#     print("Time difference is greater than 5 minutes amd less than 15 minutes.")
# else:
#     print("Time difference is less than or equal to 15 minutes.")
#
# print("Current Time:", current_time.strftime("%I:%M %p"))
# print("Hour:", hour)
# print("Minutes:", minutes)
# print("AM/PM:", am_pm)
#
# elements = driver.find_elements(By.CSS_SELECTOR, f"[class*='{'im-uc-dateComponen-txtBox'}']")
# # Check if there are any matching elements
# if elements:
#     # Click the first matching element
#     elements[0].send_keys(hour)
#     elements[1].send_keys(minutes)
#     elements[2].send_keys(am)
#     time.sleep(1)
#
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'cdk-overlay-container'}']").click()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-cm-footersenddiscard-SendBtn'}']").click()


# driver.find_element(By.CSS_SELECTOR,"[class*='im-td-overlayClose-icon']").click()
# driver.find_element(By.XPATH, "//im-td-calendarfilters//button[contains(@class, 'im-td-filterbtn')]//span[contains(@class, 'mat-button-wrapper') and text()='Scheduled']").click()


# driver.find_element(By.XPATH, "//div[@class='im-ct-menu-title im-ct-contacts-header' and text()='Direct Chat']").click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# delete = driver.find_element(By.CSS_SELECTOR, f"[class*='{'view-toolbar-button-delete'}']")
# delete.click()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-letsgobutton'}']").click()
# actions = ActionChains(driver)
# actions.send_keys(Keys.DELETE).perform()
# a_ele = driver.find_elements(By.CSS_SELECTOR, "a[href]")
# for e in a_ele:
#     if "qa.clariti.app" in e.text:
#         print(e.text)
#         actions = ActionChains(driver)
#         actions.context_click(e).perform()
#         time.sleep(1)
#         href_value = e.get_attribute("href")
#         new_tab_script = "window.open('{}');".format(href_value)
#         driver.execute_script(new_tab_script)
#         # Switch to the new tab
#         driver.switch_to.window(driver.window_handles[-1])
#         break

# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter name']").send_keys("Triadqa1 yandex")
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter password']").send_keys("Welcome123$#@!")
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Re-enter password']").send_keys("Welcome123$#@!")
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@class='im-au-custom-proceed-button' and text()=' Sign up ']").click()


# a_ele = driver.find_elements(By.CSS_SELECTOR, "a[href='https://qa.clariti']")
# print(len(a_ele))
# actions = ActionChains(driver)
# actions.context_click(element).perform()
# def conte(option):
#     if option == 'later':
#         a= driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-onboardingoption-dialog dialog2'}']")
#         b= a.find_element(By.CLASS_NAME,"im-td-onboardingoption-text1")
#         action_chains = ActionChains(driver)
#         action_chains.move_to_element(a).perform()
#         b.click()
#     if option == 'now':
#         a= driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-onboardingoption-dialog dialog1'}']")
#         b= a.find_element(By.CLASS_NAME,"im-td-onboardingoption-text1")
#         action_chains = ActionChains(driver)
#         action_chains.move_to_element(a).perform()
#         b.click()
#
# conte("now")

# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-letsgobutton'}']").click()
# driver.find_element(By.CSS_SELECTOR, "button.im-au-custom-login-btn").click()
# contact1s = driver.find_element(By.CLASS_NAME, "im-ct-contacts-pinned")
# contact1=contact1s.find_elements(By.CSS_SELECTOR, f"[class*='{'im-ct-pinnedcontacts-contactcontainer'}']")
# for contact in contact1:
#     Contact= contact.find_element(By.CSS_SELECTOR, f"[class*='{'im-sc-participantName im-sc-participant-myChatContact'}']")
#     c=Contact.text
#     print(c)
#     if c == "Triadqa1 AOL":
#         try:
#            green = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-ct-pinnedcontacts-status ng-star'}']")
#            if green.is_enabled():
#                print("Green indicator appeas")
#                Contact.click()
#                break
#         except:
#             print("Green indicator not appears")
#
#     else:
#         print("contact name not matched")

# def last_dc_messages(expected_message):
#     generated_string = random_string(5)
#     global chat_message_text
#     Dctablayout = driver.find_element(By.XPATH, "//*[contains(@class, 'im-td-directchattablayout-body')]")
#     lmessage_area = Dctablayout.find_element(By.XPATH, "//*[contains(@class, 'im-da-ch-marginTop')]")
#     MessageList = lmessage_area.find_elements(By.CSS_SELECTOR, "[class*='im-da-ch-msg-text ng-star-inserted']")
#     # ContinuousView = driver.find_element(By.CSS_SELECTOR, "[class*='im-da-th-continuousTimelineviewRoot']")
#     # # ItemList =ContinuousView.find_elements(*ItemListContinuousView)
#     # Messages = ContinuousView.find_elements(By.CSS_SELECTOR, "[class*='im-da-ch-msg-text ng-star-inserted']")
#     found_message = None
#     for eachMessage in reversed(MessageList):
#         if eachMessage.text == expected_message:
#             #logger.info("Last sent Message "+ele.text+ " exists")
#             found_message=eachMessage
#             print("Last sent Message "+eachMessage.text+ " exists")
#             Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#             action_chains = ActionChains(driver)
#             action_chains.move_to_element(found_message).perform()
#             screenshot_path = ".//Screenshots/Contact.png"
#             #take_element_screenshot(Message_item, screenshot_path)
#             found_message.screenshot(screenshot_path)
#             break
#         else:
#             #logger.info("Last sent Message " + ele.text + " not exists")
#             print("Last sent Message "+eachMessage.text+ " not exists")
#     if found_message is not None:
#         return found_message
# last_dc_messages("sad")

# def wait_until_homepage():
#     start_time = time.time()
#     timeout = 20
#     while time.time() - start_time < timeout:
#         try:
#             # main_element = get_element(Home_tab_focus) or get_element(Go_Back_home_icon)
#             m = driver.find_element(By.CSS_SELECTOR, "[class*='im-tc-startnewcommstrip']")
#             main_element = m.find_element(By.XPATH, ".//*[contains(text(), 'New Conversation')]")
#
#             if main_element.is_displayed:
#                 print("Home Page Navigated")
#                 return True
#             else:
#                 print("Home Page not Navigated")
#                 time.sleep(1)  # Wait for the page to update after clicking
#         except:
#             wait = WebDriverWait(driver, 1)
#         time.sleep(0.5)  # Wait before checking again
#     print("Home page not loaded due some issues")
#     return False
#
#
# def mail_send_validation():
#     home = None
#     try:
#         home = wait_until_homepage()
#         time.sleep(0.5)
#         # assert True, " " + testcasenumber + " Failed _ Mail sending failed"
#     except AssertionError as e:
#         print("Do logout")
#         allure.attach(str(e), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
#         pytest.fail("Assertion failed: Mail sending Failed {}".format(e))
#
#
# mail_send_validation()
# showaction = driver.find_element(By.CSS_SELECTOR, "[class*='im-da-threadOperations']")
# #print(len(showaction))
# shwo = driver.find_element(By.CSS_SELECTOR, "[class*='im-da-th-settingsBtn']")
# time.sleep(1)
# shwo.click()
# OverlayDropdown = driver.find_element(By.CSS_SELECTOR, "[class*='cdk-overlay-pane']")
# buttons = OverlayDropdown.find_elements(By.CSS_SELECTOR, "[class*='im-da-th-oper']")
# print(len(buttons))
# driver.find_element(By.XPATH, ".//*[contains(text(), 'New Conversation')]").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-th-subject-input'}']").send_keys("DUNFJBNSJKFJSF")
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-th-startConversationButton'}']").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'BgChatCall'}']").click()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'BgScheduleCall'}']").click()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'BgChatCall'}']").click()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'BgChatCall'}']").click()
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'BgChatCall'}']").click()
# def is_contact_visible(contact_list, contact_name):
#     contact_elements = contact_list.find_elements(By.CSS_SELECTOR, "[class*='im-sc-participant-myChatContact']")
#     for element in contact_elements:
#         # co=element.text
#         # print(co)
#         # if contact_name.lower() in co.lower():
#         if element.text.lower() == contact_name.lower():
#             # print(element)
#             element.click()
#             return True
#     return False

# Active = driver.find_element(By.CLASS_NAME,"im-ct-contacts-activechats")
# ActiveItem = Active.find_elements(By.CSS_SELECTOR, f"[class*='{'im-ct-contacts-activechat ng'}']")
# print(len(ActiveItem))
# for item in reversed(ActiveItem):
#     s= item.find_element(By.CLASS_NAME, "im-ct-chatSubject")
#     print(s.text)
#     if s.text == "GC CALL LIB FOLDER":
#         action_chains = ActionChains(driver)
#         action_chains.move_to_element(item).perform()
#         item.click()
#         m=item.find_element(By.CSS_SELECTOR, f"[class*='{'im-ct-close ng'}']")
#         m.click()
#         break


#
# # This function used in contact_selection_ip_chat
# def is_contact_visible(contact_name):
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-list'}']")
#     contact_elements = contact_list.find_elements(By.CSS_SELECTOR, "[class*='im-sc-participant-myChatContact']")
#     for element in contact_elements:
#         # co=element.text
#         # print(co)
#         # if contact_name.lower() in co.lower():
#         if element.text.lower() == contact_name.lower():
#             # print(element)
#             element.click()
#             return True
#     return False
#
#
# def hover_and_scroll(contact_list):
#     # Find the scrollbar element
#     ContactlistAreaMain = "im-pa-sh-mpw-body"
#     ContactMiniContainer = driver.find_element(By.CSS_SELECTOR, f"[class*='{ContactlistAreaMain}']")
#     FindScroll = "ps__rail-y"
#     ScrollClass = ContactMiniContainer.find_element(By.CSS_SELECTOR, f"[class*='{FindScroll}']")
#     Scroll = "ps__thumb-y"
#     scrollbar = ScrollClass.find_element(By.CSS_SELECTOR, f"[class*='{Scroll}']")
#     partial_Minicontact_class_name = "im-cm-sh-sharelist-list"
#
#     # Create an ActionChains instance
#     actions = ActionChains(driver)
#
#     # Hover over the scrollbar element and perform the scroll action
#     actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 30).release().perform()
#     # time.sleep(3)
#
#     # Wait for a new element to be present
#     WebDriverWait(driver, 1).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, f"[class*='{partial_Minicontact_class_name}']")))
#
#     actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 3).release().perform()
#
#     # Find the updated contact list element
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{partial_Minicontact_class_name}']")
#     print("contact list updated")
#     con = contact_list.text
#     # print(con)
#     # Return the updated contact list element
#     return contact_list
#
#
# # This function used in contact_selection_ip_chat
#
# def check_contact_visibility(contact_name):
#     visible = is_contact_visible(contact_name)
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-list'}']")
#     previous_contact_list_text = contact_list.text
#     # partial_Minicontact_class_name = "im-pa-mc-minicontactlist-itemlist"
#     # Find the parent element containing the contacts
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-list'}']")
#
#     while not visible:
#         hover_and_scroll(contact_list)
#         contact_list1 = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-cm-sh-sharelist-list'}']")
#         current_contact_list_text = contact_list1.text
#
#         if current_contact_list_text == previous_contact_list_text:
#             print("No contact exists")
#             break
#
#         c = contact_list1.text
#         # print(c)
#         visible = is_contact_visible(contact_name)
#         previous_contact_list_text = current_contact_list_text
#
#
# def contact_selection_ip_chat(contact_name):
#     visible = is_contact_visible(contact_name)
#
#     # If not visible, scroll down and check again
#     if not visible:
#         check_contact_visibility(contact_name)
#
#     time.sleep(1)
#     # driver.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()
#     time.sleep(10)
#
#
# # selecting contact to IP chat
# contact_selection_ip_chat("Suriya S QA")

# # def wait_until_Go_back_home_tab():
# #     wait = WebDriverWait(driver, 15)
# #     main_element = wait.until(
# #         EC.visibility_of_element_located((By.XPATH, "//*[contains(@class,'im-td-cdrive-previousbreadcrumb')]")))
# #     if main_element.is_displayed:
# #         print("Home Page Navigated")
# #         return True
# #     else:
# #         print("Home Page not Navigated")
# #         time.sleep(0.5)  # Wait for the page to update after clicking
# #
# #
# #
# # wait_until_Go_back_home_tab()
# # def get_mail_tab_items(subject):
# #     #subject = "Suriya S QA C"
# #     # table_body = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
# #     # Contact_table = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-mycontainer'}']")
# #     # ScrollClass = Contact_table.find_element(By.CSS_SELECTOR, f"[class*='{'ps--active-y'}']")
# #     # scrollbar = ScrollClass.find_element(By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
# #
# #     # Get the table body element
# #     global table, NoContacts
# #
# #     try:
# #         table = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
# #         if table.is_displayed():
# #
# #             # Find all the rows in the table
# #             rows = table.find_elements(By.CSS_SELECTOR, f"[class*='{'im-table-row ng-star-inserted'}']")
# #
# #             # Initialize a variable to store the found row
# #             found_row = None
# #             max_scrolls = 20  # Maximum number of scrolls
# #             scroll_count = 0
# #             while found_row is None and scroll_count < max_scrolls:
# #                 rows = table.find_elements(By.CSS_SELECTOR, f"[class*='{'im-table-row ng-star-inserted'}']")
# #
# #                 # Iterate over the rows and check the conditions
# #                 for row in rows:
# #                     # Get the subject cell
# #                     subject_cell = row.find_elements(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-contact-textname'}']")
# #                     for cell in subject_cell:
# #                         if cell.text == subject:
# #                             found_row = row
# #                             row.click()
# #                             break
# #                     if found_row is not None:
# #                         return found_row
# #             if found_row is None:
# #                 print("Contact not found")
# #                 return None
# #     except:
# #         NoContacts = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-no-contacts")]')
# #         if NoContacts.is_displayed():
# #             print("No sontacts")
#
#
# #
# #Direct_chat_tab = driver.find_element(By.XPATH, "//div[@class='im-ct-menu-title im-ct-contacts-header' and text()='Direct Chat']")
# searchTextbox = driver.find_element(By.XPATH, "//input[contains(@class, 'im-pa-mc-contactsearch-searchTextBox')]")
# #Direct_chat_tab.click()
# searchTextbox.send_keys("Suriya S QA C")
# time.sleep(2)
# get_mail_tab_items("Suriya S QA C")
# def check_scroll_to_bottom_icon():
#     try:
#         if driver.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-dc-arrowWithNewMsgCnt']").is_displayed():
#             if not driver.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-unreadStrip']").is_displayed():
#                 driver.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-dc-arrowWithNewMsgCnt']").click()
#                 print("Count button and new message strip not appears")
#             elif driver.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-unreadStrip']").is_displayed() and driver.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-dc-arrowWithNewMsgCnt']").is_displayed():
#                 print("Both new message strip and Scroll to Bottom button appears")
#
#         else:
#             print("Else")
#
#     except:
#         print("Scroll to bottom icon not appears")
#
# def last_dc_messages(expected_message):
#     global chat_message_text
#     check_scroll_to_bottom_icon()
#     Dctablayout = driver.find_element(By.XPATH, "//*[contains(@class, 'im-td-directchattablayout-body')]")
#     lmessage_area = Dctablayout.find_element(By.XPATH, "//*[contains(@class, 'im-da-ch-marginTop')]")
#     # Messageitem = "im-da-ch-dc-bookmarkItem"
#     # lmessages = lmessage_area.find_elements(By.CSS_SELECTOR, f"[class*='{Messageitem}']")
#     # lmessages = lmessage_area.find_elements(By.CLASS_NAME,"im-da-ch-dc-messageitem")
#     # print(len(lmessages))
#     # Get the msgrank value of the latest element
#     # Find the parent element
#     # parent_element = lmessage_area.find_elements(By.XPATH, "//im-da-ch-bookmarkitem")
#     # parent_element = lmessage_area.find_elements(By.CSS_SELECTOR, "[class*='attachImgIcon-fileName']")
#     MessageList = lmessage_area.find_elements(By.CSS_SELECTOR, "[class*='im-da-ch-msg-text ng-star-inserted']")
#     found_message = None
#     for eachMessage in reversed(MessageList):
#         if eachMessage.text == expected_message:
#             # logger.info("Last sent Message "+ele.text+ " exists")
#             found_message = eachMessage
#             Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#             print("Last sent Message " + eachMessage.text + " exists")
#             # screenshot_path = ".//Screenshots/" + generated_string + " DC_Message.png"
#             # take_element_screenshot(Message_item, screenshot_path)
#             # allure.attach.file(screenshot_path, name="Last sent Message " + eachMessage.text + " exists",
#             #                    attachment_type=allure.attachment_type.PNG)
#             break
#         elif expected_message in eachMessage.text:
#             found_message = eachMessage
#             Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#             print("Last sent Message " + eachMessage.text + " exists")
#             break
#         else:
#             # logger.info("Last sent Message " + ele.text + " not exists")
#             print("Last sent Message " + eachMessage.text + " not exists")
#             # screenshot_path = ".//Screenshots/" + generated_string + " DC_Message.png"
#             # take_element_screenshot(lmessage_area, screenshot_path)
#             # allure.attach.file(screenshot_path, name="Last sent Message " + eachMessage.text + " not exists",
#             #                    attachment_type=allure.attachment_type.PNG)
#     if found_message is not None:
#         print("Message Found")
#         return found_message
#
# last_dc_messages("STNU")
# a=driver.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-unreadStrip']").text
# print(a)
# def copy_sent_message(expected_message):
#     found_message = last_dc_messages(expected_message)
#     if found_message:
#         action = ActionChains(driver)
#         action.move_to_element(found_message).perform()
#         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         time.sleep(0.2)
#         Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-messageActionIcon'}']").click()
#         time.sleep(0.5)
#         overlay = driver.find_element(By.CLASS_NAME, "cdk-overlay-pane")
#         overlay.find_element(By.XPATH, "//button/span[contains(text(), 'Copy')]").click()
#
# def getNameTimeMessage(expected_message, UserName , user):
#     global getTime
#     if user == "sender":
#         found_message = last_dc_messages(expected_message)
#         if found_message:
#             action = ActionChains(driver)
#             action.move_to_element(found_message).perform()
#             Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#             try:
#                 getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msg-time'}']").text
#                 print(getTime)
#             except:
#                 getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msgNameNotShown'}']").text
#                 print(getTime)
#
#             current_date = datetime.now()
#             month_name = current_date.strftime("%b")
#
#             # Format the date with the first letter of the month in uppercase
#             formatted_datetime = f"[{current_date.day} {month_name} {current_date.year}, {getTime}]"
#
#             print(formatted_datetime)
#             driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-textarea editable-element'}']").send_keys(
#                 Keys.CONTROL, "v" + Keys.ENTER)
#             time.sleep(1)
#             message = formatted_datetime + " " + UserName + ": " + expected_message
#             print(message)
#             date_time, rest_of_text = message.split("]", 1)
#
#             # Split the date and time
#             date, times = date_time.strip("[").split(",")
#
#             # Remove the leading zero from the time
#             time_parts = times.strip().split(":")
#             hour = str(int(time_parts[0]))  # Convert to integer and back to string to remove leading zero
#             minute = time_parts[1]
#
#             # Reconstruct the modified date and time
#             new_date_time = f"[{date}, {hour}:{minute}]"
#
#             # Combine the modified date and time with the rest of the text
#             result_text = new_date_time + rest_of_text
#             print("From Func A" + result_text)
#             return result_text
#     if user == "receiver":
#         found_message = last_dc_messages(expected_message)
#         if found_message:
#             action = ActionChains(driver)
#             action.move_to_element(found_message).perform()
#             Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#             try:
#                 getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msg-time'}']").text
#                 print(getTime)
#             except:
#                 getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msgNameNotShown'}']").text
#                 print(getTime)
#
#             current_date = datetime.now()
#             month_name = current_date.strftime("%b")
#
#             # Format the date with the first letter of the month in uppercase
#             formatted_datetime = f"[{current_date.day} {month_name} {current_date.year}, {getTime}]"
#
#             print(formatted_datetime)
#             message = formatted_datetime + " " + UserName + ": " + expected_message
#             print(message)
#             date_time, rest_of_text = message.split("]", 1)
#
#             # Split the date and time
#             date, times = date_time.strip("[").split(",")
#
#             # Remove the leading zero from the time
#             time_parts = times.strip().split(":")
#             hour = str(int(time_parts[0]))  # Convert to integer and back to string to remove leading zero
#             minute = time_parts[1]
#
#             # Reconstruct the modified date and time
#             new_date_time = f"[{date}, {hour}:{minute}]"
#
#             # Combine the modified date and time with the rest of the text
#             result_text = new_date_time + rest_of_text
#             print("From Func A" + result_text)
#             return result_text
#
# def format_to_copypastemessage(expected_message):
#     getName, getTime = getNameTimeMessage(expected_message)
#     current_date = datetime.now()
#     month_name = current_date.strftime("%b")
#
#     # Format the date with the first letter of the month in uppercase
#     formatted_datetime = f"[{current_date.day} {month_name} {current_date.year}, {getTime}]"
#
#     print(formatted_datetime)
#     driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-textarea editable-element'}']").send_keys(
#         Keys.CONTROL, "v" + Keys.ENTER)
#     time.sleep(1)
#     message = formatted_datetime + " " + getName + ": " + expected_message
#     print(message)
#     date_time, rest_of_text = message.split("]", 1)
#
#     # Split the date and time
#     date, times = date_time.strip("[").split(",")
#
#     # Remove the leading zero from the time
#     time_parts = times.strip().split(":")
#     hour = str(int(time_parts[0]))  # Convert to integer and back to string to remove leading zero
#     minute = time_parts[1]
#
#     # Reconstruct the modified date and time
#     new_date_time = f"[{date}, {hour}:{minute}]"
#
#     # Combine the modified date and time with the rest of the text
#     result_text = new_date_time + rest_of_text
#     print("From Func A" + result_text)
#     return result_text

# def verify_copied_message(expected_message):
#     found_message = last_dc_messages(expected_message)
#     if found_message:
#         action = ActionChains(driver)
#         action.move_to_element(found_message).perform()
#         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         time.sleep(0.2)
#         Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-messageActionIcon'}']").click()
#         time.sleep(0.5)
#         overlay = driver.find_element(By.CLASS_NAME, "cdk-overlay-pane")
#         overlay.find_element(By.XPATH, "//button/span[contains(text(), 'Copy')]").click()
#         getName = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msg-name'}']").text
#         print(getName)
#         getTime = Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-msg-time'}']").text
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
#         driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-textarea editable-element'}']").send_keys(
#             Keys.CONTROL, "v" + Keys.ENTER)
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
#         print("From Func A" + result_text)
#         return result_text
#
#
# def verify_dc_message_copy_withTime(expected_message, user):
#     if user == "sender":
#         copy_sent_message(expected_message)
#         result_text = getNameTimeMessage(expected_message,"triad gmail1 QA","receiver")
#         print(result_text)
#         found_message = last_dc_messages(result_text)
#         if found_message:
#             print("Copied Message Found")
#
#         else:
#             print("Copied Message not found")
#             pytest.fail("Copied and Pasted DC Message not available")
#     elif user == "receiver":
#         result_text = getNameTimeMessage(expected_message, "triad gmail1 QA", "receiver")
#         print(result_text)
#         found_message = last_dc_messages(result_text)
#         if found_message:
#             print("Copied Message Found")
#
#         else:
#             print("Copied Message not found")
#             pytest.fail("Copied and Pasted DC Message not available")
#
#
# verify_dc_message_copy_withTime("SLAVE","receiver")
# def verify_forward_strip(expected_message):
#     found_message = last_dc_messages(expected_message)
#     if found_message:
#         forwardStrip = driver.find_element(By.CSS_SELECTOR, f"[class='{'im-da-ch-forwardedLabel'}']")
#         if forwardStrip.is_displayed():
#             print("Forward Strip Exists")
#         else:
#             print("Forward strip Not exists")
#             pytest.fail("Forward strip Not exists")
#     else:
#         pytest.fail("Message Not exists")
#
# verify_forward_strip("SUYN")
#
#
# def click_dc_file(expected_message):
#     found_message = last_dc_messages(expected_message)
#     if found_message:
#         action = ActionChains(driver)
#         action.move_to_element(found_message).perform()
#         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         time.sleep(1)
#         Message_item.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-messageActionIcon'}']").click()
#         time.sleep(1)
#         overlay = driver.find_element(By.CLASS_NAME, "cdk-overlay-pane")
#         overlay.find_element(By.XPATH, "//button/span[contains(text(), 'Reply')]").click()
#         #overlay.find_element(By.CSS_SELECTOR, "[class*='im-da-ch-messageActionIcon'][text()='Reply']").click()
#     else:
#         print("FileNotFound")
#
# click_dc_file("GOA")
# def is_contact_visible(contact_name):
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-itemlist'}']")
#     contact_elements = contact_list.find_elements(By.CSS_SELECTOR, "[class*='im-sc-participant-myChatContact']")
#     for element in contact_elements:
#         # co=element.text
#         # print(co)
#         # if contact_name.lower() in co.lower():
#         if element.text.lower() == contact_name.lower():
#             # print(element)
#             element.click()
#             return True
#     return False
#
#
# # This function used in contact_selection_ip_chat
# def hover_and_scroll(contact_list):
#     # Find the scrollbar element
#     ContactMiniContainer = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-container'}']")
#     ScrollClass = ContactMiniContainer.find_element(By.CSS_SELECTOR, f"[class*='{'ps--active-y'}']")
#     scrollbar = ScrollClass.find_element(By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
#
#     # Create an ActionChains instance
#     actions = ActionChains(driver)
#
#     # Hover over the scrollbar element and perform the scroll action
#     actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 30).release().perform()
#     # time.sleep(3)
#
#     # Wait for a new element to be present
#     WebDriverWait(driver, 1).until(
#         EC.presence_of_element_located(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-itemlist'}']"))
#
#     actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 3).release().perform()
#
#     # Find the updated contact list element
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-itemlist'}']")
#     print("contact list updated")
#     con = contact_list.text
#     # print(con)
#     # Return the updated contact list element
#     return contact_list
#
#
# # This function used in contact_selection_ip_chat
#
# def check_contact_visibility(contact_name):
#     visible = is_contact_visible(contact_name)
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-itemlist'}']")
#     previous_contact_list_text = contact_list.text
#     # Find the parent element containing the contacts
#     contact_list = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-itemlist'}']")
#
#     while not visible:
#         hover_and_scroll(contact_list)
#         contact_list1 = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-minicontactlist-itemlist'}']")
#         current_contact_list_text = contact_list1.text
#
#         if current_contact_list_text == previous_contact_list_text:
#             print("No contact exists")
#             break
#
#         c = contact_list1.text
#         # print(c)
#         visible = is_contact_visible(contact_name)
#         previous_contact_list_text = current_contact_list_text
#
#
# def contact_selection_ip_chat(contact_name):
#     visible = is_contact_visible(contact_name)
#
#     # If not visible, scroll down and check again
#     if not visible:
#         check_contact_visibility(contact_name)
#     time.sleep(1)
#
#
# #contact_selection_ip_chat("Manohar E")
# driver.find_element(By.XPATH, "//button/span[contains(text(), 'Forward')]").click()
# def check_file_viewer():
#     File_viewer_overlay = driver.find_element(By.CLASS_NAME, "im-td-overlayDynamicContent")
#     if File_viewer_overlay.is_displayed():
#         print("File opened")
#         iframe_element = File_viewer_overlay.find_element(By.CSS_SELECTOR,
#                                                           f"[class*='{'im-da-th-singletonfile-iframe'}']")
#         driver.switch_to.frame(iframe_element)
#         print("iframeFile")
#         try:
#             if driver.find_element(By.CSS_SELECTOR, "[class*='fv-downloadingAnimationDiv']").is_displayed():
#                 WebDriverWait(driver, 18).until(EC.invisibility_of_element(driver.find_element(By.CSS_SELECTOR, "[class*='fv-downloadingAnimationDiv']")))
#                 iframe_element_file = driver.find_element(By.CSS_SELECTOR, "[class*='fv-fileContainer']")
#                 if iframe_element_file.is_displayed():
#                     print("File Loaded")
#
#                 else:
#                     print("File not loaded")
#                 driver.switch_to.default_content()
#             else:
#                 time.sleep(2)
#                 iframe_element_file = driver.find_element(By.CSS_SELECTOR, "[class*='fv-fileContainer']")
#                 if iframe_element_file.is_displayed():
#                     print("File Loaded from else")
#
#                 else:
#                     print("File not loaded from else")
#                 driver.switch_to.default_content()
#         except TimeoutException as e:
#             print("Time out - File not loaded in desired time.")
#             driver.switch_to.default_content()
#
#     else:
#         print("File overlay not opened")
#
#
# #
# #
# # click_dc_file("LoginData.xlsx")
# check_file_viewer()
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, "im-td-detailsoverlsssay-container").find_element(By.CSS_SELECTOR,"[class*='im-td-overlayClose-icon']").click()

# cookies = driver.find_element(By.XPATH, "xome xpath")
#
# location = cookies.location
# size = cookies.size
# w, h = size['width'], size['height']
#
# print(location)
# print(size)
# print(w, h)
# driver.find_element(By.CLASS_NAME, "im-td-overlayDynamicContent")
# def file_send(File_upload):
#     ChatInputArea = driver.find_element(By.CLASS_NAME, "im-da-ch-inputcontainer")
#     svg_icon = ChatInputArea.find_elements(By.TAG_NAME, "svg")
#     first_icon = svg_icon[0]
#     first_icon.click()
#     time.sleep(3)
#     current_file_path = os.path.abspath(__file__)  # Get the path of the current script
#     project_path = os.path.dirname(os.path.dirname(current_file_path))
#     print(project_path)
#     if File_upload == 1:
#         file_path = project_path + "\\testfiles\\LoginData.xlsx"
#         mouse = MouseController()
#         mouse.position = (300, 100)  # Set the coordinates of the file in the dialog
#         mouse.click(Button.left)
#         keyboard = Controller()
#         keyboard.type(str(file_path))
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         time.sleep(3)
#     elif File_upload == 2:
#         file_path = project_path + "\\testfiles"
#         keyboard = Controller()
#         mouse = MouseController()
#         keyboard.type(file_path)
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         mouse.position = (300, 200)  # Set the coordinates of the file in the dialog
#         mouse.click(Button.left)
#         keyboard.press(Key.ctrl)
#         keyboard.press('a')
#         keyboard.release('a')
#         keyboard.release(Key.ctrl)
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         time.sleep(3)
#
#
# file_send(1)
# try:
#     inputArea = driver.find_element(By.CSS_SELECTOR,f"[class*='{'im-da-ch-inputcontainer'}']")
#     RefArea = inputArea.find_element(By.CSS_SELECTOR,f"[class*='{'im-da-ch-refmsg'}']")
#     if RefArea.is_displayed():
#         print("Reference strip Added")
#         RefMessage = inputArea.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-refmsg-textcontainer'}']")
#         if RefMessage.text == "GUNfb":
#             print("Message Appears")
#         else:
#             print("Message not appears")
# except:
#     print("Reference strip not added")


# def contacts(contact):
#     DC_Contacts = driver.find_elements(By.CSS_SELECTOR, f"[class*='{'im-ct-pinnedcontacts-contactcontainer'}']")
#     Participant_Name = driver.find_elements(By.CSS_SELECTOR, f"[class*='{'im-sc-participant-myChatContact'}']")
#     found_contact = None
#     for eachContact in reversed(Participant_Name):
#         if len(DC_Contacts) == 1:
#             if contact == Participant_Name[0].text:
#                 print("items found.")
#                 found_contact = eachContact
#                 break
#         elif len(DC_Contacts) > 1:
#             if contact == eachContact.text:
#                 print("Contact " + eachContact.text + " Found")
#                 found_contact = eachContact
#                 break
#         else:
#             print("No items found.")
#     return found_contact
#
# def hover_on_element(element):
#     action = ActionChains(driver)
#     action.move_to_element(element).perform()
#
# found_contacts = contacts("Triad QA8")
# if found_contacts:
#     hover_on_element(found_contacts)
# else:
#     print("Contact Not Found")

# WebDriverWait(driver,10).until(EC.presence_of_element_located(By.CSS_SELECTOR, f"[class*='{'im-da-th-unsupportedFile'}']")
# unsupportedFile = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-th-unsupportedFile'}']")
# DownloadButton = unsupportedFile.find_element(By.CSS_SELECTOR,f"[class*='{'im-da-th-singletonDownloadFileBtn'}']")
# if DownloadButton.is_displayed():
#     print("Download Button displayed")
# else:
#     print("Download Button not displayed")


# driver.find_element(By.XPATH, "//button/span[contains(text(), 'Copy')]").click()

# OverlayHeaderText = driver.find_element(By.CSS_SELECTOR, f"[class*='breadcrumb-title']").text
# print(OverlayHeaderText)
# email = "triadqa1@outlook.com"
# if "Bring mails from " + email == OverlayHeaderText:
#     print(email+" - Mail Configured and Mails are listed ")
# else:
#     print("Mail not Configured or Mails are not listed related to Configured Email")

# driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-overlayClose-icon']").click()

# composemailicon = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-tc-startnewcommstrip'}']").text
# print(composemailicon)
#
# if "Compose Mail" not in composemailicon:
#     print("Compose Mail icon not present")
# else:
#     print("Compose Mail icon appears")

# driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-ct-close'}']").click()
#
# s = driver.find_element(By.CSS_SELECTOR, f"[class*='im-sc-confirmationdialog-Btn'] span").text
# print(s)
# if " Yes " == s:
#     driver.find_element(By.CSS_SELECTOR, f"[class*='im-sc-confirmationdialog-Btn mat']").click()
#


# main_element = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-replyto'] input")
# main_element.send_keys("asgdjknsdjkogh")
# driver.find_element(By.CLASS_NAME, "im-np-hm-userNameSpan").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, f"[class*='{'imEmailPreference'}']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//button/span[contains(text(),"Add ")]').click()
#
# m= driver.find_elements(By.CSS_SELECTOR, f"[class*='{'im-np-cm-integrationslist-optionheader'}']")
# for eachitem in m:
#     print(eachitem.text)
#     if eachitem.text == "Outlook":
#         base_tr = eachitem.find_element(By.XPATH, ".//ancestor::im-np-cm-integrationscard")
#         base_tr.find_element(By.CSS_SELECTOR, f"[class*='{'im-np-cm-integrationslist-connectbtn'}']").click()
#         break
# CloseIcon = (By.CSS_SELECTOR, f"[class*='{'im-np-ep-configured-container'}']")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(CloseIcon))
# print("Email Added")
# Drafts = driver.find_elements(By.CSS_SELECTOR, f"[class*='im-ct-emaildraft-layout']")
# print(len(Drafts))
# for eachdraft in Drafts:
#     eachdraft.click()
#     break

# try:
# Drafts = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-selectedMailId']")
# print(Drafts.text)
# Drafts.click()
# time.sleep(1)
# overlayPane = driver.find_element(By.CSS_SELECTOR, f"[class*='cdk-overlay-pane']")
# EmailId = overlayPane.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-selectFromEmailIDs']")
# print(EmailId.text)
# EmailId.click()
# time.sleep(1)
# Drafts = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-selectedMailId']")
# print(Drafts.text)

# Drafts = driver.find_element(By.XPATH, ".//*[contains(text(), 'New Conversation')]")
# Drafts.click()
# time.sleep(1)
# s = driver.find_element(By.CSS_SELECTOR, f"[class*='im-dctab-headerroot']").text
# time.sleep(1)
# print(s)
# if s == "Suriya S QA":
#     print("SA")
# self.check_scroll_to_bottom_icon()

# def activate_window_by_partial_title(window_title, max_attempts=3, activation_delay=1):
#     all_windows = gw.getAllTitles()
#     print(all_windows)
#     for each_window_title in all_windows:
#         if window_title.lower() in each_window_title.lower():
#             try:
#                 window = gw.getWindowsWithTitle(each_window_title)[0]
#                 print(f"Attempting to activate window: {each_window_title}")
#                 attempts = 0
#                 while not window.isActive and attempts < max_attempts:
#                     window.activate()
#                     time.sleep(activation_delay)
#                     attempts += 1
#
#                 if window.isActive:
#                     print(f"Activated window: {each_window_title}")
#                 else:
#                     print(f"Window activation failed: {each_window_title}")
#             except IndexError:
#                 print(f"Window not found: {each_window_title}")
# def activate_window_by_partial_title(window_title):
#     try:
#         app = Application().connect(title_re=window_title)
#         window = app.window(title_re=window_title)
#         if not window.is_active():
#             window.set_focus()
#             print(f"Activated window: {window_title}")
#         else:
#             print(f"Window is already active: {window_title}")
#     except Exception as e:
#         print(f"Error activating window: {window_title}\n{e}")
# def close_file_explorer():
#     time.sleep(1)
#     # Replace 'Your Window Title' with the title of the window you want to focus
#     window_title_to_focus = "Open"
#
#     # Focus the window with the specified title
#     activate_window_by_partial_title(window_title_to_focus)
#     pyautogui.press('esc')
#
# close_file_explorer()

# ChatInputArea = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-ch-inputcontainer'}']")
# svg_icon = ChatInputArea.find_elements(By.TAG_NAME, "svg")
# first_icon = svg_icon[0]
# first_icon.click()
# time.sleep(3)
# focus_window_by_title("Open")
# time.sleep(1)
# upload_files("one", "S_image.jpg", "")
# # Example usage:


# DcTabLayout = driver.find_element(By.XPATH, "//*[contains(@class, 'im-td-directchattablayout-body')]")
# lMessage_area = DcTabLayout.find_element(By.XPATH, "//*[contains(@class, 'im-da-ch-marginTop')]")
# MessageList = lMessage_area.find_elements(By.CSS_SELECTOR, "[class*='im-da-ch-msg-text']")
# found_message = None
# for eachMessage in reversed(MessageList):
#     print(eachMessage.text)
#     if eachMessage.text == "GOLD":
#         found_message = eachMessage
#         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         print("Last sent message " + eachMessage.text + " exists")
#         break
#
#     elif "GOLD" in eachMessage.text:
#         found_message = eachMessage
#         Message_item = found_message.find_element(By.XPATH, "./ancestor::im-da-ch-messageitem")
#         print("Last sent message " + eachMessage.text + " exists")
#         break
#     else:
#         print("Last sent message " + eachMessage.text + " not exists")


# driver.find_element(By.CSS_SELECTOR, f"[class*='BcCompose']").click()

# for eachemail in Drafts:
#     print(eachemail.text)
#     if "triadqa8@gmail.com" in eachemail.text:
#         eachemail.find_element(By.CSS_SELECTOR, f"[class*='im-np-cm-integrationslist-connectbtn']").click()
#         break


#  if Drafts.is_displayed():
#      print("Mail will be sent using Strip appears")
#
# except NoSuchElementException:
#     print("Only 1 Mail configured, so Mail will be sent using Strip not appears")


# try:
#     CloseIcon = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-np-ep-configured-container'}']")
#     if CloseIcon.is_displayed():
#         CloseIcon.click()
# except NoSuchElementException:
#     print("Close icon not avaialble")
# try:
#     ReplyTo_dialog = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-da-dr-fromidComp'}']")
#
#     # Check if the button is enabled or disabled
#     if ReplyTo_dialog.is_displayed():
#         print("Button is disabled.")
# except NoSuchElementException:
#     print("Fail")

# actions = ActionChains(driver)
# actions.move_to_element(ReplyTo_dialog).perform()
# ReplyTo_dialog = driver.find_element(By.CSS_SELECTOR, f"[class='im-da-dr-draftcontainerSendMsgInfoPopUp']")
# print(ReplyTo_dialog.text)
# inner_html = ReplyTo_dialog.get_attribute("innerHTML")
# soup = BeautifulSoup(inner_html, "html.parser")
# JoinMultiLineText = ' '.join(soup.stripped_strings)
# print(JoinMultiLineText)
# if "Information: Subject is empty" == JoinMultiLineText:
#     print("pass")
# else:
#     print("fail")
# A = ReplyTo_dialog.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-hyperlink']")
# A.click()
# print(ReplyTo_dialog.text)
# if "Reply for this email will be sent to" in ReplyTo_dialog.text:
#     if "triadqa1@outlook.com" in ReplyTo_dialog.text:
#         print("Pass")
#     else:
#         print("Email id mismatch")
# else:
#     print("Reply Label text not givem")
# sendMailText = driver.find_element(By.CSS_SELECTOR, f"[class*='im-np-up-profiledetail-breadcrumb-container']")
# print(sendMailText.text)
# inner_html = sendMailText.get_attribute("innerHTML")
# # Parse the inner HTML with BeautifulSoup
# soup = BeautifulSoup(inner_html, "html.parser")
# # Extract and merge the text from the <a> and <span> elements
# JoinMultiLineText = ' '.join(soup.stripped_strings)
# print(JoinMultiLineText)
#
# if "Send mail is enabled with Premium subscription" in JoinMultiLineText:
#     print("Alert info appears")
# else:
#     print("Alert not appears")
# time.sleep(1)
# Overlay = driver.find_element(By.CSS_SELECTOR, f"[class='cdk-overlay-container']")
# draft_body_text = Overlay.find_element(By.CSS_SELECTOR, f"[class*='mat-menu-content")
# actions = draft_body_text.find_elements(By.TAG_NAME, "button")
# print(len(actions))
# if len(actions) == 2:
#     print("2 Options are there")
# else:
#     print("Options are not showing")
# main_element.send_keys(" "+random_string(5))
# s= main_element.text
# print(s)
# main_element = driver.find_element(By.CLASS_NAME, "claritioriginalcontent")
# s= main_element.text
# print(s)
# WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(main_element))
# time.sleep(1)
# subject = driver.find_element(By.XPATH, "//input[contains(@class,'im-da-dr-subjectInput')]")
# if subject.is_enabled():
#     print("Signature Dialog Closed")
# text_box = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-okBtn']")
# text_box.click()

# checlbox = text_box.find_element(By.CSS_SELECTOR, f"[class*='mat-checkbox-input']")
# if not checlbox.is_selected():
#     text_box.click()
# else:
#     print("Checkbox not selected")
# print(text_box.text)
# actions = ActionChains(driver)
# actions.click(text_box)
# actions.click(text_box)
# actions.click(text_box)
#
# actions.perform()
# actions.send_keys(Keys.BACKSPACE).perform()

# time.sleep(1)
#
# # # get first child window
# All_Windows = driver.window_handles
# print(len(All_Windows))
# if len(All_Windows) > 1:
#     driver.switch_to.window(All_Windows[1])
#     driver.close()
# else:
#     print("Only 1 tab is opened or newly clicked link is not opened")
#
# time.sleep(1)
# driver.switch_to.window(All_Windows[0])
# driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-cm-mcclose']").click()
# except:
#     print("EN")
# text_box.send_keys("SASFDAF")
# print(text_box.text)
# if text_box:

# def dd():
#     Draft = driver.find_elements(By.CSS_SELECTOR, f"[class*='im-ct-emaildraft-layout']")
#     print(len(Draft))
#
#     for eachDraft in Draft:
#         GetMailIcon = eachDraft.find_element(By.CSS_SELECTOR, f"[class*='im-ct-ipitem-icon']")
#         GetDraftText = eachDraft.find_element(By.CSS_SELECTOR, f"[class*='im-ct-activechat-initiator']").text
#         print(GetDraftText)
#         GetSubjectText = eachDraft.find_element(By.CSS_SELECTOR, f"[class*='im-ct-activechat-subject']").text
#         print(GetSubjectText)
#         if GetDraftText == "Draft" and GetSubjectText == "no subject" and GetMailIcon:
#             print("New Draft Opened with Draft text and No subject text")
#             return True
#         else:
#             print("New Draft not opened with Draft text or No subject text")
#             return False
#
#
#
# C = dd()
# if C:
#     print("Pass")
# else:
#     print("Fail")

# Draft = driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-maildrafttablayout-header']").text
# print(Draft)
# if Draft == "New mail":
#     print("New mail text appears in Draft")
# else:
#     print("New Mail text not appears")


# driver.find_element(By.XPATH, "//input[contains(@class,'im-da-dr-subjectInput')]").send_keys("Sample")
# time.sleep(2)
# GetSubjectText = driver.find_element(By.CSS_SELECTOR, f"[class*='im-ct-activechat-subject']").get_attribute("innerText")
# print(GetSubjectText)
# if GetSubjectText == "no subject":
#     print("New Draft Opened with Draft text and No subject text")
# else:
#     print("New Draft not opened with Draft text or No subject text")

# def cc(Recipe):
#     if Recipe == "Cc":
#         CcButtonArea = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-CCRecipientsAttachFiles']")
#         CcButtonArea.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-showCcMail']").click()
#         time.sleep(1)
#     elif Recipe == "Bcc":
#         CcButtonArea = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-CCRecipientsAttachFiles']")
#         CcButtonArea.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-showBccMail']").click()
#         time.sleep(1)
#     Draft = driver.find_elements(By.CSS_SELECTOR, f"[class*='im-da-dr-recipientItem']")
#     for eachDraft in Draft:
#         GetField = eachDraft.find_element(By.CSS_SELECTOR, f"[class*='im-da-cm-labelPrefix']")
#         if GetField.text == Recipe:
#             eachDraft.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-contactsIconContainer']").click()
#             time.sleep(0.5)
#             return True
#
#
#             # Particiapnt = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-emailtoPos']")
#             # TitleText = Particiapnt.find_element(By.CSS_SELECTOR, f"[class*='im-da-cm-title']").text
#             # print(TitleText)
#             # recipient_type = TitleText[16:-1]  # Extract "To", "Cc", or "Bcc"
#             # if recipient_type == "Recipe":
#             #     print("Add contact to '"+Recipe + "' - Dialog Opened")
#             #     print(recipient_type)
#             #     return True
#             # else:
#             #     print(f"Invalid recipient type: {recipient_type}")
#             #     print(Recipe + "- Dialog not Opened")
#             #     return False
#
#         # else:
#         #     print("No")
#
#
# Check = cc("To")
# if Check:
#     print("pass")
# else:
#     print("Fail")
# GetDraftText = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-CCRecipientsAttachFiles']")
# GetDraftText.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-showCcMail']").click()
# print(GetDraftText)
# GetSubjectText = eachDraft.find_element(By.CSS_SELECTOR, f"[class*='im-ct-activechat-subject']").text
# print(GetSubjectText)
# if GetDraftText == "Draft" and GetSubjectText == "no subject" and GetMailIcon:
#     print("New Draft Opened with Draft text and No subject text")
# else:
#     print("New Draft not opened with Draft text or No subject text")

# GetDraftText = driver.find_element(By.CSS_SELECTOR, f"[class*='im-sh-paymentupgrade-container']")
# AddparticiapntDialog = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-recipientItem']")
# AddparticiapntDialog.find_element(By.CSS_SELECTOR, f"[class*='im-da-cm-remove']").click()


# def wait_until_homepage():
#     start_time = time.time()
#     timeout = 20
#     while time.time() - start_time < timeout:
#         try:
#             # main_element = get_element(home_tab_focus) or get_element(go_back_home_icon)
#             main_element = driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-cdrive-detailsOverlay']")
#             # main_element = parent_element.find_element(*home_tab_focus)
#
#             if not main_element.is_displayed:
#                 print("Home Page Navigated")
#                 return True
#             else:
#                 print("Home Page not Navigated")
#                 time.sleep(1)  # Wait for the page to update after clicking
#         except:
#             WebDriverWait(driver, 1)
#         time.sleep(0.5)  # Wait before checking again
#     print("Home page not loaded")
#
#
# wait_until_homepage()

# def wait_until_mail_send_overlay():
#     try:
#         main_element = driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-cdrive-detailsOverlay']")
#
#         WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(main_element))
#         print("Pass")
#
#     except:
#         print("Overlay Draft not opened")
#
# wait_until_mail_send_overlay()
# draft_body_text = (By.CSS_SELECTOR, f"[class*='claritioriginalcontent'] br")
# main_element = driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-cdrive-detailsOverlay']")

# driver.find_element(By.CSS_SELECTOR, f"[class*='claritioriginalcontent'] div").click()
# def body_content_message(tab_or_overlay, message):
#     # click(body_area)
#     # for _ in range(4):
#     #     send_keys(body_area, Keys.UP)
#     # # keyboard_usage(body_area, Keys.UP, 4)
#     time.sleep(5)
#     element = driver.find_element(By.CSS_SELECTOR, "[class*='claritioriginalcontent'] br[clear='all']")
#     driver.execute_script("arguments[0].click();", element)
#     if tab_or_overlay == "tab":
#         driver.find_element(By.CSS_SELECTOR, "[class*='claritioriginalcontent'] br[clear='all']").send_keys(message)
#     elif tab_or_overlay == "overlay":
#         OverlayDraft = driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-cdrive-detailsOverlay']")
#         OverlayDraftBody = OverlayDraft.find_element(By.CSS_SELECTOR, "[class*='claritioriginalcontent'] br[clear='all']")
#         OverlayDraftBody.send_keys(message)
#
#
# body_content_message("overlay", "HELLO")

# AttachIconArea = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-CCRecipientsAttachFiles']")
# AttachIconArea.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-AttachFilesIcon']").click()
#
#
# # time.sleep(2)
# #
# #
# # # screenshot = pyautogui.screenshot()
# # #
# # # # Save the screenshot to a file
# # # screenshot.save('full_screen_screenshot.png')
# # def is_file_explorer_open():
# #     windows = gw.getWindowsWithTitle("Open")
# #     return len(windows) > 0
# #
# #
# # # Check if the File Explorer is open
# # if is_file_explorer_open():
# #     print("File Explorer is open.")
# # else:
# #     print("File Explorer is not open.")
# def wait_for_file_explorer_open(timeout=30):
#     start_time = time.time()
#     while time.time() - start_time < timeout:
#         windows = gw.getWindowsWithTitle("Open")
#         if windows:
#             return windows[0]  # Return the first found File Explorer window
#         time.sleep(1)  # Wait for 1 second before checking again
#     return None  # Return None if the timeout is reached
#
#
# # Set the maximum time to wait (in seconds)
#
# # Wait for File Explorer to open
# file_explorer_window = wait_for_file_explorer_open(15)
#
# if file_explorer_window:
#     print("File Explorer is open.")
#     print("File Explorer Title:", file_explorer_window.title)
# else:
#     print("File Explorer did not open within the specified timeout.")
#
# # def wait_for_file_explorer_open(timeout=30):
# #     start_time = time.time()
# #     while time.time() - start_time < timeout:
# #         windows = gw.getWindowsWithTitle("Open")
# #         if windows:
# #             return windows[0]  # Return the first found File Explorer window
# #         time.sleep(1)  # Wait for 1 second before checking again
# #     return None  # Re
# # def close_file_explorer(window):
# #     # Get the window's coordinates
# #     left, top, right, bottom = window.left, window.top, window.right, window.bottom
# #
# #     # Calculate the position of the close button relative to the window's top-left corner
# #     close_button_x = right - left - 150  # Adjust this value if needed
# #     close_button_y = top - 5  # Adjust this value if needed
# #
# #     # Click the close button
# #     pyautogui.click(left + close_button_x, top + close_button_y)
#
#
# # file_explorer_window = wait_for_file_explorer_open(30)
# #
# # # Close File Explorer
# # close_file_explorer(file_explorer_window)
# # actions = ActionChains(driver)
# #
# # # Press the ESC key
# # actions.send_keys(Keys.ESCAPE).perform()
# def focus_window_by_title(window_title):
#     window = gw.getWindowsWithTitle(window_title)
#     if window:
#         window[0].activate()
#
#
# # Replace 'Your Window Title' with the title of the window you want to focus
# window_title_to_focus = "Open"
#
# # Focus the window with the specified title
# focus_window_by_title(window_title_to_focus)
#
# pyautogui.press('esc')

# def screenshot_and_attach_report_pyautogui(fileName, ReportName):
#     project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
#     path = os.path.join(project_path, "Screenshots")
#     screenshot = pyautogui.screenshot()
#     filename = random_string(5) + fileName + ".png"
#     screenshot.save(os.path.join(path, filename))
#     with open(os.path.join(path, filename), "rb") as file:
#         allure.attach(file.read(), name=ReportName, attachment_type=allure.attachment_type.PNG)
#
# screenshot_and_attach_report_pyautogui("SAC" , "SADf")
# upload_files("one", "LoginData.xlsx", "")
# try:
#     Alert = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerInvalidAttachMessageContainer']")
#     if Alert:
#         print("Pass")
#         action = ActionChains(driver)
#         S = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerAttachInfoIcon']")
#         action.move_to_element(S).perform()
#
# except NoSuchElementException:
#     print("Fail")
# current_file_path = os.path.abspath(__file__)  # Get the path of the current script
# project_path = os.path.dirname(os.path.dirname(current_file_path))
# # print(project_path)
# file_path = project_path + "\\testfiles\\"
# keyboard = Controller()
# keyboard.type(str(file_path))
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# time.sleep(3)
# mouse = MouseController()
# mouse.position = (300, 200)  # Set the coordinates of the file in the dialog
# mouse.click(Button.left)
# keyboard.press(Key.ctrl)
# keyboard.press('a')
# keyboard.release('a')
# keyboard.release(Key.ctrl)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)

# def remove_file_attachment(file_name):
#     FileAttachmentsArea = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerAttachmentList']")
#     File = FileAttachmentsArea.find_elements(By.CSS_SELECTOR, f"[class*='im-da-cm-fileContainer']")
#     if len(File) > 0:
#         for eachFile in File:
#             FileName = eachFile.find_element(By.CSS_SELECTOR, f"[class*='attachImgIcon-fileName']").text
#             print(FileName)
#             if FileName == file_name:
#                 eachFile.find_element(By.CSS_SELECTOR, f"[class*='im-da-cm-deleteIconClass']").click()
#                 return True
#     if len(File) == 0:
#         print("File Attachments not found")
#         return False


# def verify_file_attachment_added():
#     FileAttachmentsArea = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftcontainerAttachmentList']")
#     File = FileAttachmentsArea.find_elements(By.CSS_SELECTOR, f"[class*='im-da-cm-fileContainer']")
#     if len(File) > 0:
#         for eachFile in File:
#             eachFile.find_element(By.CSS_SELECTOR, f"[class*='im-da-cm-cancelUploadIcon']").click()
#             print("File Attachments found")
#         return True
#     if len(File) == 0:
#         print("File Attachments not found")
#         return False
# def verify_show_editor_toolbar_displayed():
#     FontName = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarJustCenter']")
#     # actions = ActionChains(driver)
#     # actions.move_to_element(FontName).perform()
#     # time.sleep(1)
#     FontName.click()
#     # time.sleep(1)
#     # Icon = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftEditorPullDownArrowContainer']")
#     # actions.move_to_element(Icon).perform()
#     # Overlay = driver.find_element(By.CSS_SELECTOR, f"[class*='cdk-overlay-container']")
#     # Tooltip = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-editorToolbar']")
#     # if Tooltip:
#     #     print("Pass")
#     #     take_element_screenshot(Tooltip,"SAVE.png")
#     # else:
#     #     print("Fail")
# verify_show_editor_toolbar_displayed()
# M = verify_show_editor_toolbar_displayed()
# if M:
#     print("Pass")
# else:
#     print("Fail")

# OverlayDialog = driver.find_element(By.CSS_SELECTOR, f"[class*='im-td-detailsoverlay-container']")
# T = OverlayDialog.find_element(By.CSS_SELECTOR, f"[class*='im-shareitems-title']").text
# print(T)
# recipient_type = T[16:-1]
# print(recipient_type)

# def select_contact_direct_chat_tab_search(contact_name):
#     time.sleep(1)
#
#     # Get the table body element
#     table = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#     if table.is_displayed():
#         # Initialize a variable to store the found row
#         found_row = None
#         while found_row is None:
#             rows = table.find_elements(By.CSS_SELECTOR, f"[class*='{'im-table-row ng-star-inserted'}']")
#
#             # Iterate over the rows and check the conditions
#             for row in rows:
#                 # Get the subject cell
#                 subject_cell = row.find_elements(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-contact-textname'}']")
#                 for cell in subject_cell:
#                     if cell.text == contact_name:
#                         print(cell.text)
#                         found_row = row
#
#                         break
#                 if found_row is not None:
#                     return found_row
#
#
#         if found_row is None:
#             print("contact not found")
#             return None
#
#
# found_row = select_contact_direct_chat_tab_search("Suriya S QA")
# base_tr = found_row.find_element(By.XPATH, ".//ancestor::tr")
# base_tr.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-item-checkbox'}']").click()
#
# Overlay = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-detailsoverlay-container'}']")
# Overlay.find_element(By.CSS_SELECTOR, f"[class*='{'im-cm-share-searchTextBox'}']").send_keys("Clariti")

# subject_class = (By.CSS_SELECTOR, f"[class*='{'im-pa-mc-contact-textname'}']")
# no_contacts_found_alert = (By.XPATH, '//*[contains(@class, "im-pa-mc-no-contacts")]')
# contact_table = (By.CSS_SELECTOR, f"[class*='{'im-shareitems-contacttable'}']")
# scroll_area_overlay = (By.CSS_SELECTOR, f"[class*='{'ps__rail-y'}']")  # Updated from ps--active-y
# scroll_bar_overlay = (By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
#
#
# def is_contact_visible(contact_name):
#     try:
#         table = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#         if table.is_displayed():
#             # Initialize a variable to store the found row
#             found_row = None
#             while found_row is None:
#                 rows = table.find_elements(By.CSS_SELECTOR, f"[class*='{'im-table-row ng-star-inserted'}']")
#                 # Iterate over the rows and check the conditions
#                 for row in rows:
#                     # Get the subject cell
#                     subject_cell = row.find_elements(By.CSS_SELECTOR, f"[class*='{'im-pa-mc-contact-textname'}']")
#                     for cell in subject_cell:
#                         if cell.text.lower() == contact_name.lower():
#                             found_row = row
#                             return found_row
#                     if found_row is not None:
#                         return found_row
#                 return False
#             if found_row is None:
#                 print("contact not found")
#                 return None
#     except:
#         NoContacts = driver.find_element(no_contacts_found_alert)
#         if NoContacts.is_displayed():
#             print("No Contacts found Alert appears")
#             return None
#
#
# # This function used in contact_selection_ip_chat
# def hover_and_scroll(contact_list):
#     # Find the scrollbar element
#     ContactMiniContainer = driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-shareitems-contacttable'}']")
#     ScrollClass = ContactMiniContainer.find_element(By.CSS_SELECTOR, f"[class*='{'ps__rail-y'}']")
#     scrollbar = ScrollClass.find_element(By.CSS_SELECTOR, f"[class*='{'ps__thumb-y'}']")
#
#     # Create an ActionChains instance
#     actions = ActionChains(driver)
#     table_body = (By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#     actions.move_to_element(
#         driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')).perform()
#
#     # Hover over the scrollbar element and perform the scroll action
#     actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 25).release().perform()
#     # time.sleep(3)
#     table_body = (By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#
#     # Wait for a new element to be present
#     WebDriverWait(driver, 1).until(
#         EC.presence_of_element_located(table_body))
#
#     actions.move_to_element(scrollbar).click_and_hold().move_by_offset(0, 3).release().perform()
#
#     # Find the updated contact list element
#     contact_list = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#     print("contact list updated")
#     con = contact_list.text
#     # print(con)
#     # Return the updated contact list element
#     return contact_list
#
#
# # This function used in contact_selection_ip_chat
# def check_contact_visibility(contact_name):
#     visible = is_contact_visible(contact_name)
#     contact_list = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#     previous_contact_list_text = contact_list.text
#     # Find the parent element containing the contacts
#     contact_list = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#     while not visible:
#         hover_and_scroll(contact_list)
#         contact_list1 = driver.find_element(By.XPATH, '//*[contains(@class, "im-pa-mc-contact-tablebody")]')
#         current_contact_list_text = contact_list1.text
#
#         if current_contact_list_text == previous_contact_list_text:
#             print("No contact exists")
#             break
#         c = contact_list1.text
#         # print(c)
#         visible = is_contact_visible(contact_name)
#         if visible:
#             base_tr = visible.find_element(By.XPATH, ".//ancestor::tr")
#             base_tr.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-item-checkbox'}']").click()
#             time.sleep(1)
#             driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-shareitems-sharebtn'}']").click()
#             time.sleep(1)
#             return True
#         previous_contact_list_text = current_contact_list_text
#
#
# def verify_contact_selection_dialog(contact_name):
#     visible = is_contact_visible(contact_name)
#     if visible:
#         print("Visible")
#         base_tr = visible.find_element(By.XPATH, ".//ancestor::tr")
#         base_tr.find_element(By.CSS_SELECTOR, f"[class*='{'im-td-item-checkbox'}']").click()
#         time.sleep(1)
#         try:
#             if driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-sh-paymentupgrade-container'}']").is_displayed():
#                 time.sleep(1)
#                 return True
#         except NoSuchElementException:
#             print("No payment Dialog")
#         driver.find_element(By.CSS_SELECTOR, f"[class*='{'im-shareitems-sharebtn'}']").click()
#         time.sleep(1)
#         return True
#     # If not visible, scroll down and check again
#     if not visible:
#         visible = check_contact_visibility(contact_name)
#         if visible:
#             print("Scroll and Visible")
#             return True
#         if not visible:
#             print("FAIL")
#     time.sleep(1)
#
#
# #verify_contact_selection_dialog("Manohar E")
# Check = verify_contact_selection_dialog("Clariti Suppordt")
# if Check:
#     print("pass")
# else:
#     print("Fail")
# Overlay = driver.find_element(By.CSS_SELECTOR, f"[class*='cdk-overlay-container")
# draft_body_text = Overlay.find_element(By.CSS_SELECTOR, f"[class*='mat-menu-content")
# actions = draft_body_text.find_elements(By.TAG_NAME, "button")
# print(len(actions))
# if len(actions) == 3:
#     print("3 Options are there")
# elif len(actions) == 3:
#     print("4 Options are there")
# def verify(key):
#     editor_tool_bold = driver.find_element(By.CSS_SELECTOR, f"[class*='claritioriginalcontent']")
#     try:
#         imagetag = editor_tool_bold.find_element(By.TAG_NAME, "img")
#         imagetag.click()
#         time.sleep(1)
#         if key == "delete_key":
#             actions = ActionChains(driver)
#             actions.send_keys(Keys.DELETE).perform()
#             time.sleep(1)
#             try:
#                 if editor_tool_bold.find_element(By.TAG_NAME, "img"):
#                     print("Image not Deleted when using DELETE Key")
#             except NoSuchElementException:
#                 print("Image Deleted when using DELETE Key")
#         elif key == "backspace_key":
#             actions = ActionChains(driver)
#             actions.send_keys(Keys.BACKSPACE).perform()
#             time.sleep(1)
#             try:
#                 if editor_tool_bold.find_element(By.TAG_NAME, "img"):
#                     print("Image not Deleted when using BACKSPACE Key")
#             except NoSuchElementException:
#                 print("Image Deleted when using BACKSPACE Key")
#         else:
#             print("Enter a Valid Key: "+ key)
#
#         # style_attribute = imagetag.get_attribute("style")
#         # driver.execute_script("arguments[0].style.width='120px'; arguments[0].style.height='120px';", imagetag)
#         # if "border: 2px solid red" in style_attribute:
#         #     print("Pass")
#         #     print(style_attribute)
#         # else:
#         #     print("Fail")
#         #     print("Border not appears and Image not selected")
#     except NoSuchElementException:
#         print("Fail")
#
# verify("backspace_key")
# A = (By.CSS_SELECTOR, f"[class*='im-da-dr-parentContainer']")
# WebDriverWait(driver, 15).until(EC.visibility_of_element_located(A))
# print("1")
# def verify_hyperlink_dialog_Text_to_be_displayed_textbox_focused():
#     text_box = driver.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-urltext'] input")
#     is_active_element = text_box == driver.switch_to.active_element
#     if is_active_element:
#         print("The text box is the currently active element")
#         return True
#     else:
#         print("The text box is not the currently active element")
#         return False
#
# verify_hyperlink_dialog_Text_to_be_displayed_textbox_focused()
# # actions = ActionChains(driver)
# actions.click(draft_body_text)
# actions.click(draft_body_text)
# actions.click(draft_body_text)
# actions.perform()
# editor_tool_bold.click()
# time.sleep(1)
# Colour_tool = editor_tool_bold.find_element(By.CSS_SELECTOR, f"[class*='im-da-dr-draftToolBarFontColorList']")
# AllColours = Colour_tool.find_elements(By.TAG_NAME, "li")
# random_color = random.choice(AllColours)
# color_element = random_color.find_element(By.TAG_NAME, "a")
#
# color_class = color_element.get_attribute("class")
# text = color_class.split("im-da-dr-draftToolBarFont")[-1]
#
# print(text)

#
# color_element.click()
#
# style_attribute = editor_tool_font_icon.get_attribute("style")
# background_color = style_attribute.split("background-color:")[1].strip().strip(";")
# rgb_values = re.findall(r'\d+', background_color)
#
# # Convert the RGB values to hexadecimal
# hex_color = "#{:02X}{:02X}{:02X}".format(int(rgb_values[0]), int(rgb_values[1]), int(rgb_values[2]))
#
# font_element = draft_body_text.find_element(By.XPATH, ".//font")
#
# # Get the value of the color attribute
# color_attribute = font_element.get_attribute("color")
#
# draft_body_text.click()
# if hex_color.lower() == color_attribute.lower():
#     print("Passs")
# else:
#     print("Fail")


# print(len(AllColours))
# for eachColour in AllColours:
#     Color = eachColour.find_element(By.TAG_NAME, "a")
#     if Color:
#         print(Color.get_attribute("class"))
#
#
#     else:
#         print("Fail")
# computed_style = draft_body_text.value_of_css_property('text-align')
#
# # Verify if the text alignment is set to "left"
# if computed_style == 'center':
#     print("Text alignment is center")
# else:
#     print(f"Text alignment is {computed_style}")
# time.sleep(1)
# try:
#     if draft_body_text.find_element(By.TAG_NAME, "strike"):
#         print("text Changed to Bold")
# except NoSuchElementException:
#     print("Bold Tag not appears")
