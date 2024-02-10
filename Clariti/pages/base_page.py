import os
import random
import string
import time

import pyautogui
import pygetwindow as gw
import allure
import pytest
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController, Button
from allure_commons.types import AttachmentType
from pywinauto import Application
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def random_string(str_len):
    letters = string.ascii_letters + string.digits
    result = ''
    for _ in range(str_len):
        result += random.choice(letters)
    return result


def take_element_screenshot(element, file_name):
    element.screenshot(file_name)


def is_file_explorer_open():
    windows = gw.getWindowsWithTitle("Open")
    return len(windows) > 0


def focus_window_by_title(window_title):
    try:
        app = Application().connect(title_re=window_title)
        window = app.window(title_re=window_title)
        if not window.is_active():
            window.set_focus()
            print(f"Activated window: {window_title}")
        else:
            print(f"Window is already active: {window_title}")
    except Exception as e:
        print(f"Error activating window: {window_title}\n{e}")


def close_file_explorer():
    # Replace 'Your Window Title' with the title of the window you want to focus
    window_title_to_focus = "Open"
    # Focus the window with the specified title
    focus_window_by_title(window_title_to_focus)
    pyautogui.press('esc')


def wait_for_file_explorer_open(timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        windows = gw.getWindowsWithTitle("Open")
        if windows:
            return windows[0]  # Return the first found File Explorer window
        time.sleep(1)  # Wait for 1 second before checking again
    return None  # Return None if the timeout is reached


def upload_files(file_upload_count, file_name,
                 dc_or_mail):  # file_upload_count to mention as "one" or "many" or multiple
    global file_path
    current_file_path = os.path.abspath(__file__)  # Get the path of the current script
    project_path = os.path.dirname(os.path.dirname(current_file_path))
    # print(project_path)
    if file_upload_count == "one":
        file_path = project_path + "\\testfiles\\" + file_name
        focus_window_by_title("Open")
        keyboard = Controller()
        keyboard.type(str(file_path))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
    elif file_upload_count == "many":
        if dc_or_mail == "dc":
            file_path = project_path + "\\testfiles"
        elif dc_or_mail == "mail":
            file_path = project_path + "\\manytestfiles"
        focus_window_by_title("Open")
        keyboard = Controller()
        mouse = MouseController()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        mouse.position = (300, 200)  # Set the coordinates of the file in the dialog
        mouse.click(Button.left)
        keyboard.press(Key.ctrl)
        keyboard.press('a')
        keyboard.release('a')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)


def screenshot_and_attach_report_pyautogui(fileName, ReportName):
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    path = os.path.join(project_path, "Screenshots")
    screen_shot = pyautogui.screenshot()
    filename = random_string(5) + fileName + ".png"
    screen_shot.save(os.path.join(path, filename))
    with open(os.path.join(path, filename), "rb") as file:
        allure.attach(file.read(), name=ReportName, attachment_type=allure.attachment_type.PNG)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver1 = driver1
        self.wait = WebDriverWait(self.driver, 25)

    def click(self, by_locator):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
            # presence_of_element_located(by_locator)).click()
        except TimeoutException:
            print("Page Not loaded")
            allure.attach(self.driver.get_screenshot_as_png(), name="Clickable_Element_Not_Loaded",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("Element not found due to Exceeded the Time out - more than 15 seconds")

    def send_keys(self, by_locator, value):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).send_keys(value)
            # self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(value)
        except TimeoutException:
            print("Time_out")
            allure.attach(self.driver.get_screenshot_as_png(), name="Element_Not_Loaded",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("Element not found due to Exceeded the Time out - more than 15 seconds")

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("innerText")

    def wait_for_element(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            print("Time_out")
            allure.attach(self.driver.get_screenshot_as_png(), name="Element_Not_Loaded",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("Element not found due to Exceeded the Time out - more than 15 seconds")

    def wait_for_all_element(self, by_locator):
        try:
            self.wait.until(EC.presence_of_all_elements_located(by_locator))
        except TimeoutException:
            print("Time_out")
            allure.attach(self.driver.get_screenshot_as_png(), name="All_Elements_Not_Loaded",
                          attachment_type=AttachmentType.PNG)
            pytest.fail("Elements not found due to Exceeded the Time out - more than 15 seconds")

    def wait_for_element_disappears(self, by_locator):
        self.wait.until(EC.invisibility_of_element_located(by_locator))

    def element_present(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def get_window_handle(self):
        return self.driver.current_window_handle

    def hover_on_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def screenshot_and_attach_report(self, location, fileName, ReportName):
        screenshot_path = ".//Screenshots/" + random_string(5) + fileName + ".png"
        take_element_screenshot(self.get_element(location), screenshot_path)
        allure.attach.file(screenshot_path, name=ReportName, attachment_type=allure.attachment_type.PNG)
