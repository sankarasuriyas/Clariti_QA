rmdir /s /q reports
call .\venv\Scripts\activate.bat
pytest -s -v -k "TestPushMail2Users or TestPushMail3Users or TestPollingMail3Users or TestPollingMail2users"  --alluredir="./reports" Clariti/testscripts/test_mail_cases.py
REM pytest -s -v --alluredir="./reports" Clariti/testscripts/test_directChatCases.py
start "" explorer ".\Clariti\ReportDocument\AutomationCases.xlsx"
allure serve "./reports"