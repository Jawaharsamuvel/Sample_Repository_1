from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Sam Spartan\\PycharmProjects\\Selenium_proj_2\\SIDE_Export\\drivers\\chromedriver.exe')

driver.get("https://www.google.com")
# driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)

element = driver.find_element_by_name("q")
element.send_keys("Hello world")
element.submit()

print(driver.title)