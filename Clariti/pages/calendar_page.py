import datetime
import time
from selenium.webdriver.common.by import By
from Clariti.pages.base_page import BasePage, random_string
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.locators import Locators


def take_element_screenshot(element, file_name):
    element.screenshot(file_name)


class CalendarPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.Keys = None
        self.driver = driver

    # calendar_tab = Locators.CalendarPage.CALENDAR_TAB
    # header_icon_area = Locators.CalendarPage.HEADER_ICON_AREA
    # todo_header_icon = Locators.CalendarPage.TODO_HEADER_ICON
    # event_header_icon = (By.XPATH, ".//*[contains(text(), 'Event')]")
    # call_header_icon = (By.XPATH, ".//*[contains(text(), 'Call')]")
    #
    # overlay_pane = (By.CSS_SELECTOR, f"[class*='{'cdk-overlay-pane'}']")
    # overlay_container = (By.CSS_SELECTOR, f"[class*='{'cdk-overlay-container'}']")
    #
    # calendar_overlay = (By.CSS_SELECTOR, f"[class*='{'im-td-cdrive-detailsOverlay'}']")
    # close_icon_overlay = (By.CSS_SELECTOR, "[class*='im-td-overlayClose-icon']")
    # discard_yes_button = (By.XPATH, "//button[contains(., 'Yes')]")
    # discard_no_button = (By.XPATH, "//button[contains(., 'No')]")
    #
    # reason_to_do = (By.CSS_SELECTOR, "[class*='im-td-todo-reason']")
    # reason_remind_me = (By.XPATH, "//div[contains(@class, 'mat-select-panel-wrap')]//div//div//mat-option[contains(@class, 'material-select-option')]//span[text()=' Remind me about ']")
    # reason_schedule_chat = (By.XPATH, "//div[contains(@class, 'mat-select-panel-wrap')]//div//div//mat-option[contains(@class, 'material-select-option')]//span[text()=' Schedule a chat ']")
    # reason_compose_mail = (By.XPATH, "//div[contains(@class, 'mat-select-panel-wrap')]//div//div//mat-option[contains(@class, 'material-select-option')]//span[text()=' Compose new mail ']")
    # reason_schedule_call = (By.XPATH, "//div[contains(@class, 'mat-select-panel-wrap')]//div//div//mat-option[contains(@class, 'material-select-option')]//span[text()=' Schedule a call ']")
    # subject_text_box = (By.XPATH, "//mat-form-field[contains(@class, 'im-td-todo-subject')]//div//div//div//input[contains(@class, 'mat-input-element')]")
    # date_picker_icon = (By.CSS_SELECTOR, f"[class*='{'im-sh-date-area'}']")
    # time_picker_icon = (By.CSS_SELECTOR, f"[class*='{'im-uc-dateComponent-timecontrol'}']")
    # show_optional_fields_text = (By.CSS_SELECTOR, f"[class*='{'im-td-todo-advanced'}']")
    # description_text_box = (By.CSS_SELECTOR, f"[class*='{'im-td-description-textarea'}']")
    # remind_me_drop_down = (By.XPATH, "//mat-form-field[contains(@class, 'im-td-todo-reminder')]//mat-select")
    # remind_me_option_lists = (By.CSS_SELECTOR, f"[class*='{'ps--active-y'}']")
    # remind_me_option_item = (By.CSS_SELECTOR, f"[class*='{'material-select-option'}']")
    # remind_me_option_item_text = (By.CSS_SELECTOR, f"[class*='{'mat-option-text'}']")
    # schedule_todo_button = (By.CSS_SELECTOR, f"[class*='{'im-cm-footersenddiscard-SendBtn'}']")
    #
    # scheduled_filter_button = (By.XPATH, "//div[contains(@class, 'im-td-definedfilter-container')]//button[contains(@class, 'im-td-filterbtn')]//span[text()=' Scheduled ']")
    # completed_filter_button = (By.XPATH, "//div[contains(@class, 'im-td-definedfilter-container')]//button[contains(@class, 'im-td-filterbtn')]//span[text()=' Completed ']")
    # monthly_filter_button = (By.XPATH, "//div[contains(@class, 'im-td-definedfilter-container')]//button[contains(@class, 'im-td-filterbtn')]//span[text()=' Monthly ']")
    # weekly_filter_button = (By.XPATH, "//div[contains(@class, 'im-td-definedfilter-container')]//button[contains(@class, 'im-td-filterbtn')]//span[text()=' Weekly ']")
    # daily_filter_button = (By.XPATH, "//div[contains(@class, 'im-td-definedfilter-container')]//button[contains(@class, 'im-td-filterbtn')]//span[text()=' Daily ']")

    def click_calendar_tab(self):
        self.click(Locators.CalendarPage.CALENDAR_TAB)

    def click_schedule_todo(self):
        self.click(Locators.CalendarPage.TODO_HEADER_ICON)

    def click_schedule_event(self):
        self.click(Locators.CalendarPage.EVENT_HEADER_ICON)

    def click_schedule_call(self):
        self.click(Locators.CalendarPage.CALL_HEADER_ICON)

    def enter_subject(self):
        self.send_keys(Locators.CalendarPage.SUBJECT_TEXT_BOX, "Test-" + random_string(5))

    def click_schedule_todo_button(self):
        self.click(Locators.CalendarPage.SCHEDULE_TODO_BUTTON)

    def select_at_time_next_slot_to_current_time_with_reminder(self):
        self.click(Locators.CalendarPage.TIME_PICKER_ICON)
        time.sleep(0.5)
        current_time = datetime.datetime.now()

        # Extract the current hour and minutes
        current_hour = current_time.hour
        current_minutes = current_time.minute

        # Define your predefined minute intervals
        minute_intervals = [0, 15, 30, 45]

        # Find the next predefined minute interval greater than the current minutes
        # next_interval = min([x for x in minute_intervals if x >= current_minutes])
        next_interval = min([x for x in minute_intervals if x >= current_minutes], default=None)
        # If there is no next interval in the current hour, move to the next hour
        if next_interval is None:
            current_hour += 1
            next_interval = min(minute_intervals)  # Use the first interval of the next hour

        # Ensure the hour stays within the valid range (0-23)
        current_hour %= 24

        # Determine AM or PM
        am_pm = 'AM' if current_hour < 12 else 'PM'

        # Convert the hour to 12-hour format
        if current_hour == 0:
            current_hour = 12
        elif current_hour > 12:
            current_hour -= 12

        hour = current_hour
        minutes = next_interval
        am = am_pm

        # Calculate the time difference in minutes
        time_difference_minutes = (hour * 60 + minutes) - (current_time.hour * 60 + current_time.minute)

        print("Current Time:", current_time.strftime("%I:%M %p"))
        print("Hour:", hour)
        print("Minutes:", minutes)
        print("AM/PM:", am_pm)

        elements = self.driver.find_elements(By.CSS_SELECTOR, f"[class*='{'im-uc-dateComponen-txtBox'}']")
        # Check if there are any matching elements
        if elements:
            # Click the first matching element
            elements[0].send_keys(hour)
            elements[1].send_keys(minutes)
            elements[2].send_keys(am)
            time.sleep(1)
        self.click(Locators.CalendarPage.OVERLAY_CONTAINER)
        time.sleep(1)
        # Check if the time difference is greater than 15 minutes
        if time_difference_minutes > 15:
            print("Time difference is greater than 15 minutes.")
        elif 15 > time_difference_minutes > 1:
            print("Time difference is greater than 5 minutes amd less than 15 minutes.")
            self.click(Locators.CalendarPage.SHOW_OPTIONAL_FIELDS_TEXT)
            time.sleep(0.5)
            self.select_and_set_remind_me_option("5 Mins")
        else:
            print("Time difference is less than or equal to 15 minutes.")
            self.click(Locators.CalendarPage.SHOW_OPTIONAL_FIELDS_TEXT)
            time.sleep(0.5)
            self.select_and_set_remind_me_option("5 Mins")

    def select_and_set_remind_me_option(self, reminder_option):
        self.click(Locators.CalendarPage.REMIND_ME_DROP_DOWN)
        time.sleep(1)
        Overlay = self.get_element(Locators.CalendarPage.OVERLAY_PANE)
        OptionClass = Overlay.find_element(*Locators.CalendarPage.REMIND_ME_OPTION_LISTS)
        Options = OptionClass.find_elements(*Locators.CalendarPage.REMIND_ME_OPTION_ITEM)
        for option in Options:
            text = option.find_element(*Locators.CalendarPage.REMIND_ME_OPTION_ITEM_TEXT).text
            if text == reminder_option:
                option.click()
                break
            else:
                print("Enter a proper mentioned Reminder time,.")

