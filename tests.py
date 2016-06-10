import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_input_form_required(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        self.assertIn("Contact Form", driver.title)

        user = driver.find_element_by_id('Name')
        user.send_keys("Test User")

        user = driver.find_element_by_id('Phone')
        user.send_keys("7045785610")

        user = driver.find_element_by_id('Email')
        user.send_keys("guitarmasterctd@aol.com")

        user = driver.find_element_by_id('Service')
        user.send_keys(Keys.ARROW_DOWN)

        user = driver.find_element_by_id('time')
        user.send_keys(Keys.ARROW_DOWN)

        driver.implicitly_wait(1500)  # seconds
        user = driver.find_element_by_id('submit')
        user.send_keys(Keys.RETURN)
        driver.implicitly_wait(1500)  # seconds

        assert "sendmessage.php" in driver.current_url

    # def test_input_form_missinginfo(self):
    #     driver = self.driver
    #     driver.get("http://localhost:5000")
    #     self.assertIn("Contact Form", driver.title)
    #
    #     user = driver.find_element_by_id('Name')
    #     user.send_keys("Test User")
    #
    #     user = driver.find_element_by_id('Phone')
    #     user.send_keys("")
    #
    #     user = driver.find_element_by_id('Email')
    #     user.send_keys("guitarmasterctd@aol.com")
    #
    #     user = driver.find_element_by_id('Service')
    #     user.send_keys(Keys.ARROW_DOWN)
    #
    #     user = driver.find_element_by_id('time')
    #     user.send_keys(Keys.ARROW_DOWN)
    #
    #     driver.implicitly_wait(1500)  # seconds
    #     user = driver.find_element_by_id('submit')
    #     user.send_keys(Keys.RETURN)
    #     driver.implicitly_wait(1500)  # seconds
    #     driver._switch_to.alert.accept()


if __name__ == "__main__":
    unittest.main()
