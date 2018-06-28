from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select


wd = webdriver.Chrome()

#Selectors
gender_xpath = "//input[@name='gender' and @value = 'Male']"
first_name_id = "firstname"
female_xpath ="//input[@value='c# ']"
age_name = "age"
age_value = "30 to 39"
link_xpath = "//a[@href='http://www.teachmeselenium.com/teachmeselenium/automation-practice/']"

alert_text_xapth = "//a[contains(text(),'Click Me to get Alert')]"

class TestSelenium(unittest.TestCase):

    def test_elements(self):
        wd.get(("http://www.teachmeselenium.com/automation-practice/"))

        #Text Box: Populate the first name
        first_name_element= wd.find_element_by_id(first_name_id)
        first_name_element.send_keys("Eddi")

        #Radio Buttons: select mail option
        gender = wd.find_element_by_xpath(gender_xpath)
        gender.click()

        #Check Box: select C#
        checkbox = wd.find_element_by_xpath(female_xpath)
        checkbox.click()

        #Drop Down: Select age
        dropdown = Select(wd.find_element_by_name(age_name))
        dropdown.select_by_value(age_value)

        #Submit Button: Click Submit
        submit = wd.find_element_by_name("submit")
        submit.click()

        #Link: Click on the link
        link = wd.find_element_by_xpath(link_xpath)
        link.click()

        #Alert JS Button: Click on the button and then on JS popup
        alert_button=wd.find_element_by_xpath(alert_text_xapth)
        alert_button.click()
        alert = wd.switch_to.alert()
        alert.accept()



        time.sleep(2)
        wd.quit()



if __name__ == '__main__':
    unittest.main()
