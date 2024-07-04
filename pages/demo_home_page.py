from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains


class DemoHomePage:

    def __init__(self, driver):
        self.driver = driver        
    
    def __open_page(self, wait, number):
        try:
            page = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".category-cards div:nth-of-type("+ str(number) +") .card-body"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('element', e))

        return page

    def open_elements(self, wait):
        # Open "Elements" page
        element = self.__open_page(wait, 1)

        ActionChains(self.driver).move_to_element(element).click().perform()

    def open_forms(self, wait):
        # Open "Forms" page
        element = self.__open_page(wait, 2)

        ActionChains(self.driver).move_to_element(element).click().perform()