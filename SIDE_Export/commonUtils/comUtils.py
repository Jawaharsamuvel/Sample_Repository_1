from selenium import webdriver


class commonUtilities():

    def clickElement(self,driver,byType,byValue):
        driver.find_element(byType,byValue).click()

    def sendKeysToElement(self,driver,byType,byValue,textToPass):
        driver.find_element(byType,byValue).send_keys(textToPass)

    def checkElementPresent(self,driver,byType,byValue):
        return driver.find_element(byType,byValue).is_displayed()

    def getDriver(self, browserName):
        if browserName in ('chrome','Chrome','CHROME'):
            return webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')
        else:
            raise Exception ("Invalied browser value passed")