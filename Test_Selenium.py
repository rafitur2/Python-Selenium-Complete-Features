from selenium import webdriver
import time
import unittest

wd = webdriver.Chrome()

class TestSelenium(unittest.TestCase):

    def test_elements(self):
        wd.get(("http://www.teachmeselenium.com/automation-practice/"))
        #Find element by locator ID and populate the first name
        _first_name_element= wd.find_element_by_id("firstname")
        _first_name_element.send_keys("Eddi")

        #Radio Buttons
        _gender = wd.find_element_by_xpath("//input[@name='gender' and @value = 'Male']")
        _gender.click()





        time.sleep(2)
        wd.quit()



if __name__ == '__main__':
    unittest.main()
