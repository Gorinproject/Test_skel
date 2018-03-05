from selenium import webdriver
import unittest

class UnitTestExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() # note that this creates a class instance variable
        self.driver.implicitly_wait(30) # when testing AJAX this would not be used
        self.base_url = "http://ukr.net" # sets up another class instance variable
        self.verificationErrors = []

    def testWebSite1(self): # a first test case there can be others
        driver = self.driver  # class instance variable used here
        driver.get("http://ukr.net")

        # put your test code here


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__": # allows unittest to start by running this class file
    unittest.main()  # start the main method of unittest