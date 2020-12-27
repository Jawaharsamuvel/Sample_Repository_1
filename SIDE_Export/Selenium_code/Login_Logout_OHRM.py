from selenium import webdriver
import time
'''
driver = webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')
driver.implicitly_wait(10)
# driver = webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')
# driver.implicitly_wait(10)

# driver.get("https://www.google.com")
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
# driver.find_element_by_id('txtUsername').send_keys("Admin")
# driver.find_element_by_name('txtUsername').send_keys("Admin")
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
# driver.find_element_by_id('txtPassword').send_keys("admin123")
driver.find_element_by_name('txtPassword').send_keys("admin123")
# driver.find_element_by_name("Submit").click()
driver.find_element_by_id("btnLogin").click()

checkwelcome = driver.find_element_by_id("welcome").is_displayed()
if checkwelcome:
    print("Login Successful")
else:
    print("Login failed")

driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()
driver.quit()
'''



class OHRM_Cases:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def login(self,username,password):  #constructor

        self.driver.get(self.url)
        txtUsername = self.driver.find_element_by_xpath("//input[@id='txtUsername']")
        txtPassword = self.driver.find_element_by_name('txtPassword')
        btnLogin = self.driver.find_element_by_id("btnLogin")

        print(self.driver.title)
        txtUsername.send_keys(username)
        txtPassword.send_keys(password)
        btnLogin.click()
        iblWelcome = self.driver.find_element_by_id("welcome")

        checkwelcome = iblWelcome.is_displayed()
        if checkwelcome:
            print("Login Successful")
        else:
            print("Login failed")

    def logout(self):
        iblWelcome = self.driver.find_element_by_id("welcome")
        # time.sleep(3)
        iblWelcome.click()
        lnkLogout = self.driver.find_element_by_link_text("Logout")
        lnkLogout.click()
        self.driver.quit()

ohrm = OHRM_Cases()
ohrm.login("Admin","admin123")
ohrm.logout()
