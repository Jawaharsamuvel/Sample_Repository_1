import unittest

class unittest_exemple(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setUpClass method - runs before setup method of first test method")
        '''
        in setUpClass as it runs only once per class first in order we can be have below tasks associated with it
        instantiating the driver,browser, anu constant values(browser location)
        we can check if the browser/driver instance is not null. if null we can relaunch it
        '''

    def setUp(self):
        print("setup method - runs before every test method")
        '''
        we can setup prerequistion for unit test or scenario like :
        lanch applicable page
        we can do login
        '''

    def tearDown(self):
        print("tearDown method - runs after every test method")
        '''
        we can have below activities like:
        closing the window
        loging out
        check if logout is done correctly
        '''

    @classmethod
    def tearDownClass(self):
        print("tearDownClass method - runs after teardown method of last test method")
        '''
        since it's running in last  position we can add  the cleanup activities here like:
        close browser
        close selenium session
        quite session
        '''

    def test_TC1(self):
        print("TC1 method - Unit teat method")

    def test_TC2(self):
        print("TC2 method - Unit teat method")

    def test_TC3(self):
        print("TC3 method - Unit teat method")

if __name__ == '__main__':
    unittest.main()