import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class unittest_example(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setUpClass method - creating the driver instance")
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.url = "https://opensource-demo.orangehrmlive.com/"
    def setUp(self):
        print("setUp method - logging into the application")
        self.driver.get(self.url)
        self.driver.find_element(By.NAME, "txtUsername").send_keys("admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
    def tearDown(self):
        print("tearDown method - logging out")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        lblWelcome = self.driver.find_element_by_id("welcome")
        lblWelcome.click()
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()
    @classmethod
    def tearDownClass(self):
        print("setDownClass method - quiting driver instance")
        self.driver.quit()
    # def ttest_TC1_verifyWelcomePageAvailable(self):
    #     print("test medhod: verifying if the welcome page is available after successful login")
    #     checkWelcome = self.driver.find_element_by_id("welcome").is_displayed()
    #     print("check welcome page is available", checkWelcome)
    #
    # def ttest_TC2_verifyWelcomePage(self):
    #     print("TC2 method - unit test method")
    #
    # def ttest_TC3_verifyLogout(self):
    #     print("TC3 method - unit test method")
    #
    # def ttest_TC4_verifyDownload(self):
    #     print("TC5 method - unit test method")
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
    #     self.driver.find_element(By.LINK_TEXT, "Download").click()
    #
    # def ttest_TC5_verifyUpload(self):
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
    #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/USER/PycharmProjects/TCOct2020/backup/resources/importData.csv")
    #     self.driver.find_element(By.ID, "btnSave").click()
    # def test_TC6_handleSimpleAlert(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #     self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
    #     # self.driver.switch_to_alert()
    #     alertBox = self.driver.switch_to.alert
    #     print(alertBox.text)
    #     alertBox.accept()
    # def test_TC5_handleConfirmationAlert(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #     self.driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
    #     alert = self.driver.switch_to.alert
    #     print(alert.text)
    #     alert.dismiss()
    #     msgElement = self.driver.find_element(By.ID, "confirm-demo")
    #     print(msgElement.is_displayed())
    #     print("what happened?", msgElement.text)
    #     self.driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
    #     alert = self.driver.switch_to.alert
    #     print(alert.text)
    #     alert.accept()
    #     print("what happened?", msgElement.text)
    def test_TC6_handleInputPromptAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
        msgElement = self.driver.find_element(By.ID, "prompt-demo")
        print(msgElement.is_displayed())
        print("what happened?", msgElement.text)
        self.driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        alert = self.driver.switch_to.alert
        alert.send_keys("ABCDEFGH")
        print(alert.text)
        alert.accept()
        print("what happened?", msgElement.text)

if __name__ == '__main__':
    unittest.main()