from selenium import webdriver
from selenium.webdriver.common.by import By

# Ganna app testing
class GANA_test:


    def Sign_in():
        driver = webdriver.Chrome(executable_path='C:/Users/Sam Spartan/PycharmProjects/Selenium_proj_2/SIDE_Export/drivers/chromedriver.exe')
        driver.implicitly_wait(20)
        driver.get("https://gaana.com/browse")
        driver.find_element(By.XPATH, '//li[@id = "searchTop"]').click()
        element = driver.find_element(By.ID, 'sb')
        element.send_keys("Shape of you")
        driver.find_element(By.CLASS_NAME, 'search_btn').click()
        driver.find_element(By.XPATH, "//img[@title= 'Shape Of You']").click()


    Sign_in()
# driver.find_element(By.NAME, 'search_btn').click()
# driver.quit()



