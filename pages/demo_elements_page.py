from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class DemoCatPage:

    def __init__(self, driver):
        self.driver = driver        

    def open_radio(self, wait):
        # Open "Radio Button" page
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li#item-2"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('open_radio', e))

    def get_home(self):
        # Open to home page
        self.driver.find_element(By.CSS_SELECTOR, "#app a").click()

    def open_forms(self, wait):
        # Open to form page
        try:
            elements = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".accordion > div"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('open_form', e))

        elements[1].find_element(By.CSS_SELECTOR, "li#item-0").click()