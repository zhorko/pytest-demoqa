from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class DemoRadioPage:

    def __init__(self, driver):
        self.driver = driver        

    def __find_radio(self, wait, radio_text):
        # Find specified radio button
        match radio_text.lower():
            case "yes":
                try:
                    radio_yes = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#yesRadio"))
                    )
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('radio_yes', e))
                    return "Unable to find element"

                return radio_yes
        
            case "impressive":
                try:
                    radio_impressive = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#impressiveRadio"))
                    )
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('radio_impressive', e))
                    return "Unable to find element"
                
                return radio_impressive
            
            case _:
                return 1, "Wrong text for selector"

    def click_radio(self, wait, radio_text):
        # Click on radio button
        radio_button = self.__find_radio(wait, radio_text)
        
        self.driver.execute_script("arguments[0].click();", radio_button)
        
    def get_radio_status(self, wait, radio_text) -> bool:
        # Check type to proceed
        if type(self.__find_radio(wait, radio_text)) is tuple:
            return False
        
        else:
            # Return radio button status        
            return self.__find_radio(wait, radio_text).is_selected()
        
    def get_home(self):
        # return to home page
        self.driver.find_element(By.CSS_SELECTOR, "#app a").click()