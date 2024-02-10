import os

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Clariti import settings
# from Clariti.pages.calendar_page import CalendarPage
from Clariti.pages.contacts_page import ContactsPage
from Clariti.pages.directChat_page import DirectChatPage
from Clariti.pages.home_page import HomePage
from Clariti.pages.login_page import LoginPage
from Clariti.pages.mail_draft_page import MailDraftPage
from Clariti.pages.mail_page import MailPage
from Clariti.pages.signup_page import SignUpPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture()
def getDriver(request, getBrowser):
    global driver
    if getBrowser == "chrome":
        # chromedriver_autoinstaller.install()
        # driver = webdriver.Chrome()
        # driver_path = "./chromedriver/chromedriver.exe"
        # options = webdriver.ChromeOptions()
        # service = ChromeService(executable_path=driver_path)
        # driver = webdriver.Chrome(service=service, options=options)
        #chrome_options = Options()
        # chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--disable-logging')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')    // Used for Automation ignore case google oauth
        os.environ['WDM_LOCAL'] = '1'
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif getBrowser == "firefox":
        driver = webdriver.Firefox()

    driver.get(settings.url)
    driver.maximize_window()

    # driver.implicitly_wait(10)
    # request.cls.basePage = BasePage(driver)
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)
    request.cls.mailDraftPage = MailDraftPage(driver)
    request.cls.contactsPage = ContactsPage(driver)
    request.cls.directChatPage = DirectChatPage(driver)
    request.cls.mailPage = MailPage(driver, request.cls.homePage)
    request.cls.signupPage = SignUpPage(driver)
    #request.cls.calendarPage = CalendarPage(driver)
    request.cls.driver = driver
    yield driver
    time.sleep(0.1)
    driver.quit()


@pytest.fixture()
def getDriver1(request, getBrowser):
    global driver1
    if getBrowser == "chrome":
        # chromedriver_autoinstaller.install()
        # driver = webdriver.Chrome()
        # driver_path = "./chromedriver/chromedriver.exe"
        # options = webdriver.ChromeOptions()
        # service = ChromeService(executable_path=driver_path)
        # driver = webdriver.Chrome(service=service, options=options)
        # chrome_options = Options()
        # chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--disable-logging')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif getBrowser == "firefox":
        driver1 = webdriver.Firefox()

    driver1.get(settings.url)
    driver1.maximize_window()

    # driver1.implicitly_wait(10)
    # request.cls.basePage = BasePage(driver)
    request.cls.loginPage1 = LoginPage(driver1)
    request.cls.homePage1 = HomePage(driver1)
    request.cls.mailDraftPage1 = MailDraftPage(driver1)
    request.cls.contactsPage1 = ContactsPage(driver1)
    request.cls.directChatPage1 = DirectChatPage(driver1)
    request.cls.mailPage1 = MailPage(driver1, request.cls.homePage)
    #request.cls.calendarPage1 = CalendarPage(driver1)
    request.cls.driver1 = driver1
    # request.cls.driver = driver
    yield driver1
    time.sleep(0.1)
    driver1.quit()


@pytest.fixture()
def getDriver2(request, getBrowser):
    global driver2
    if getBrowser == "chrome":
        # chromedriver_autoinstaller.install()
        # driver = webdriver.Chrome()
        # driver_path = "./chromedriver/chromedriver.exe"
        # options = webdriver.ChromeOptions()
        # service = ChromeService(executable_path=driver_path)
        # driver = webdriver.Chrome(service=service, options=options)
        # chrome_options = Options()
        # chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--disable-logging')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # driver2 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver2 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif getBrowser == "firefox":
        driver2 = webdriver.Firefox()

    driver2.get(settings.url)
    driver2.maximize_window()

    # driver.implicitly_wait(10)
    # request.cls.basePage = BasePage(driver)
    request.cls.loginPage2 = LoginPage(driver2)
    request.cls.homePage2 = HomePage(driver2)
    request.cls.mailDraftPage2 = MailDraftPage(driver2)
    request.cls.contactsPage2 = ContactsPage(driver2)
    request.cls.directChatPage2 = DirectChatPage(driver2)
    request.cls.mailPage2 = MailPage(driver2, request.cls.homePage)
    #request.cls.calendarPage2 = CalendarPage(driver2)
    request.cls.driver2 = driver2
    yield driver2
    time.sleep(0.1)
    driver2.quit()
