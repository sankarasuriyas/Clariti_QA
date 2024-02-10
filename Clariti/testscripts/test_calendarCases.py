import time
import allure
from Clariti.testscripts.base_test import BaseTest1
from Clariti.utilities.customlogger import LogGen
from Clariti.utilities.utils import verify_status


class TestCalendar(BaseTest1):
    logger = LogGen.loggen()

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("TC_01 - User A add User B contact and User B contact should focused. "
                        "User B side, User A contact should not Add.")
    def test_dc_01(self):
        UserA_email = "triadqa1@aol.com"
        UserA_password = "Welcome123$#@!"
        test_case_number = "TC_01"
        sheet_name = "Direct Chat"
        status_tc_01 = None
        try:
            with allure.step("Login to clariti User A and User B"):
                self.loginPage.clariti_sign_in(UserA_email, UserA_password)
                time.sleep(1)
            with allure.step("Select Calendar tab"):
                self.calendarPage.click_calendar_tab()
                time.sleep(1)

            with allure.step("Select Schedule Todo"):
                self.calendarPage.click_schedule_todo()
                time.sleep(1)

            with allure.step("Schedule Todo"):
                self.calendarPage.enter_subject()
                self.calendarPage.select_at_time_next_slot_to_current_time_with_reminder()
                time.sleep(1)
                self.calendarPage.click_schedule_todo_button()

            with allure.step("Doing logout"):
                self.homePage.click_logout()

        finally:
            verify_status(test_case_number, status_tc_01)
            #status_report_update_to_xls(sheet_name, status_tc_01, test_case_number)