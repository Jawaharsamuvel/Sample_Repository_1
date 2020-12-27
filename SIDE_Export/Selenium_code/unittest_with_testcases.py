import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from SIDE_Export.commonUtils.comUtils import commonUtilities


#
# class unittest_exemple(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(self):
#         print("setUpClass method - creating the driver instance")
#         self.driver = webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')
#         self.driver.implicitly_wait(10)
#         self.url = "https://opensource-demo.orangehrmlive.com/"
#
#     def setUp(self):
#         print("setup method - runs before every test method")
#         self.driver.get(self.url)
#         print("TC1 method - Unit teat method")
#         txtUsername = self.driver.find_element_by_name('txtUsername')
#         txtPassword = self.driver.find_element_by_name('txtPassword')
#         btnLogin = self.driver.find_element_by_id("btnLogin")
#         print(self.driver.title)
#         txtUsername.send_keys("Admin")
#         txtPassword.send_keys("admin123")
#         btnLogin.click()
#         checkLogin = self.driver.find_element_by_id("welcome").is_displayed()
#         print("Check Login :", checkLogin )
#
#     def tearDown(self):
#         self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
#         print("tearDown method - runs after every test method")
#         iblWelcome = self.driver.find_element_by_id("welcome")
#         iblWelcome.click()
#         check = self.driver.find_element_by_link_text("Logout").is_displayed()
#         print("logout displayed", check)
#         lnkLogout = self.driver.find_element_by_link_text("Logout")
#         lnkLogout.click()
#
#     @classmethod
#     def tearDownClass(self):
#         print("tearDownClass method - quiting driver instance")
#         self.driver.quit()
#
#     def test_TC1_verifywelcomePageAvailable(self):
#         print("verifyong if the welcome page availabe after successfull logiin")
#         checkwelcome  = self.driver.find_element_by_id("welcome").is_displayed()
#         print("welcome page is avaliable", checkwelcome)
#
#     # def test_TC2_verifywelcomePage(self):
#     #     print("TC2 method - Unit teat method")
#     #
#     # def test_TC3_verifyLogout(self):
#     #     print("TC3 method - Unit teat method")
#     #
#     # def test_TC4_verifyUpload(self):
#     #     print("TC4 method - Unit teat method")
#     #     self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
#     #     self.driver.find_element(By.LINK_TEXT, "Download").click()
#     #
#     # def test_TC5_verifyLogout(self):
#     #     print("TC5 method - Unit teat method")
#     #     self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
#     #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/resources/importData.csv")
#     #     self.driver.find_element(By.ID, "btnSave").click()
#
#     # def test_TC6_verifyUpload(self):
#     #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
#     #     self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
#     #     alertBox = self.driver.switch_to.alert
#     #     print(alertBox.text)
#     #     alertBox.accept()
#     #
#     # def test_TC7_verifyLogout(self):
#     #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
#     #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/resources/importData.csv")
#     #     self.driver.find_element(By.ID, "btnSave").click()
#     #
#     # def test_TC8_verifyLogout(self):
#     #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
#     #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/resources/importData.csv")
#     #     self.driver.find_element(By.ID, "btnSave").click()
#
# if __name__ == '__main__':
#     unittest.main()



''' Common utilities'''


class unittest_exemple(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setUpClass method - creating the driver instance")
        self.cu = commonUtilities()
        # self.driver = webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')
        self.driver = self.cu.getDriver('chrome')
        self.driver.implicitly_wait(10)
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def setUp(self):
        print("setup method - runs before every test method")
        self.driver.get(self.url)
        print("Verify Login page is available", self.cu.checkElementPresent(self.driver, By.NAME, 'txtUsername'))
        self.cu.sendKeysToElement(self.driver, By.NAME, "txtUsername", "admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        self.cu.clickElement(self.driver, By.ID, "btnLogin")

    def tearDown(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        print("tearDown method - runs after every test method")
        iblWelcome = self.driver.find_element_by_id("welcome")
        iblWelcome.click()
        check = self.driver.find_element_by_link_text("Logout").is_displayed()
        print("logout displayed", check)
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()

    @classmethod
    def tearDownClass(self):
        print("tearDownClass method - quiting driver instance")
        self.driver.quit()

    def test_TC1_verifywelcomePageAvailable(self):
        print("verifyong if the welcome page availabe after successfull logiin")
        checkwelcome  = self.driver.find_element_by_id("welcome").is_displayed()
        print("welcome page is avaliable", checkwelcome)

    # def test_TC2_verifywelcomePage(self):
    #     print("TC2 method - Unit teat method")
    #
    # def test_TC3_verifyLogout(self):
    #     print("TC3 method - Unit teat method")
    #
    # def test_TC4_verifyUpload(self):
    #     print("TC4 method - Unit teat method")
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
    #     self.driver.find_element(By.LINK_TEXT, "Download").click()
    #
    # def test_TC5_verifyLogout(self):
    #     print("TC5 method - Unit teat method")
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
    #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/resources/importData.csv")
    #     self.driver.find_element(By.ID, "btnSave").click()

    # def test_TC6_verifyUpload(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #     self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
    #     alertBox = self.driver.switch_to.alert
    #     print(alertBox.text)
    #     alertBox.accept()
    #
    # def test_TC7_verifyLogout(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/resources/importData.csv")
    #     self.driver.find_element(By.ID, "btnSave").click()
    #
    # def test_TC8_verifyLogout(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #     self.driver.find_element(By.ID, "pimCsvImport_csvFile").send_keys("C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/resources/importData.csv")
    #     self.driver.find_element(By.ID, "btnSave").click()

if __name__ == '__main__':
    unittest.main()
