from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys

class FormPage:

    def __init__(self, driver):
        self.driver = driver

    def __select_dropdown(self, wait, select_num:int, dropdown_num:int, exceptions_name:str):
        try:
            wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-"+ str(select_num) +"-option-"+ str(dropdown_num) +""))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format(exceptions_name, e))

    def fill_name(self, name:list):

        self.driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(name[0])
        self.driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys(name[1])

    def fill_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(email)

    def fill_gender(self, gender):
        gender = self.driver.find_element(By.CSS_SELECTOR, "input[value='"+ gender +"']")
        self.driver.execute_script("arguments[0].click();", gender)

    def fill_phone(self, phone):
        p = self.driver.find_element(By.CSS_SELECTOR, "#userNumber")
        p.click()
        p.send_keys(phone)

    def fill_dob(self, dob):
        date = self.driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput")
        date.send_keys(Keys.CONTROL + "a")
        date.send_keys(dob)

    def fill_subjects(self, wait, subjects:list):
        subject_form = self.driver.find_element(By.CSS_SELECTOR, "#subjectsWrapper input")

        for subject in subjects:
            subject_form.send_keys(subject)
            self.__select_dropdown(wait, 2, 0, "hobbies")

    def fill_hobbies(self, wait, hobbies:list):
        i = 0
        try:
            hobby_form = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#hobbiesWrapper > div > div"))
            )
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('hobbies', e))

        for index, val in hobbies.items():
            if val is True:
                hobby_form[i].click()
            i+=1


    def fill_address(self, addres):
        self.driver.find_element(By.CSS_SELECTOR, "#currentAddress-wrapper textarea").send_keys(addres)

    def fill_state(self, wait, state):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.CSS_SELECTOR, "#stateCity-wrapper input"))
        try:
            wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Select State')]"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('state', e))

        global global_state
        global_state = state.lower()

        match state.lower():
            case "ncr":
                self.__select_dropdown(wait, 3, 0, "state_NCR")
            case "uttar pradesh":
                self.__select_dropdown(wait, 3, 1, "state_uttar")
            case "haryana":
                self.__select_dropdown(wait, 3, 2, "state_haryana")
            case "rajasthan":
                self.__select_dropdown(wait, 3, 3, "state_rajasthan")
            case _:
                return "No such state!"

    def fill_city(self, wait, city):
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Select City')]").click()

        if global_state == "ncr":
            match city.lower():
                case "delhi":
                    self.__select_dropdown(wait, 4, 0, "city_delhi")
                case "gurgaon":
                    self.__select_dropdown(wait, 4, 1, "city_gurgaon")
                case "noida":
                    self.__select_dropdown(wait, 4, 2, "city_noida")
                case _:
                    return "No such city!"

        elif global_state == "uttar pradesh":
            match city.lower():
                    case "agra":
                        self.__select_dropdown(wait, 4, 0, "city_agra")
                    case "lucknow":
                        self.__select_dropdown(wait, 4, 1, "city_lucknow")
                    case "merrut":
                        self.__select_dropdown(wait, 4, 2, "city_merrut")
                    case _:
                        return "No such city!"

        elif global_state == "haryana":
            match city.lower():
                    case "karnal":
                        self.__select_dropdown(wait, 4, 0, "city_karnal")
                    case "panipat":
                        self.__select_dropdown(wait, 4, 1, "city_panipat")
                    case _:
                        return "No such city!"

        elif global_state == "rajasthan":
            match city.lower():
                    case "jaipur":
                        self.__select_dropdown(wait, 4, 0, "city_jaipur")
                    case "jaiselmer":
                        self.__select_dropdown(wait, 4, 1, "city_jaiselmer")
                    case _:
                        return "No such city!"

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()