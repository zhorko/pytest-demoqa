from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys

class DemoFormPage:

    def __init__(self, driver):
        self.driver = driver        

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

            try:
                wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-2-option-0"))
                ).click()
            except exceptions.TimeoutException as e:
                print('{0} >> {1}'.format('hobbies', e))    

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


    def fill_addres(self, addres):
        self.driver.find_element(By.CSS_SELECTOR, "#currentAddress-wrapper textarea").send_keys(addres)

    def fill_state(self, wait, state):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.CSS_SELECTOR, "#stateCity-wrapper input"))
        try:
            state_form = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Select State')]"))
            ).click()
        except exceptions.TimeoutException as e:
            print('{0} >> {1}'.format('state', e))
                
        global Global_state
        Global_state = state.lower()
        
        match state.lower():
            case "ncr":
                try:
                    wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-3-option-0"))
                    ).click()
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('state_NCR', e))
            case "uttar pradesh":
                try:
                    wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-3-option-1"))
                    ).click()
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('state_uttar', e))
            case "haryana":
                try:
                    wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-3-option-2"))
                    ).click()
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('state_haryana', e))
            case "rajasthan":
                try:
                    wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-3-option-3"))
                    ).click()
                except exceptions.TimeoutException as e:
                    print('{0} >> {1}'.format('state_rajasthan', e))

    def fill_city(self, wait, city):
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Select City')]").click()
        
        if Global_state == "ncr":
            match city.lower():
                case "delhi":
                    try:
                        wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-0"))
                        ).click()
                    except exceptions.TimeoutException as e:
                        print('{0} >> {1}'.format('city_delhi', e))
                case "gurgaon":
                    try:
                        wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-1"))
                        ).click()
                    except exceptions.TimeoutException as e:
                        print('{0} >> {1}'.format('city_gurgaon', e))
                case "noida":
                    try:
                        wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-2"))
                        ).click()
                    except exceptions.TimeoutException as e:
                        print('{0} >> {1}'.format('city_noida', e))
        elif Global_state == "uttar pradesh":    
            match city.lower():
                    case "agra":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-0"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_agra', e))
                    case "lucknow":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-1"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_lucknow', e))
                    case "merrut":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-2"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_merrut', e))
        elif Global_state == "haryana":    
            match city.lower():
                    case "karnal":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-0"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_karnal', e))
                    case "panipat":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-1"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_panipat', e))
        elif Global_state == "rajasthan":    
            match city.lower():
                    case "jaipur":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-0"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_jaipur', e))
                    case "jaiselmer":
                        try:
                            wait.until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-select-4-option-1"))
                            ).click()
                        except exceptions.TimeoutException as e:
                            print('{0} >> {1}'.format('city_jaiselmer', e))
                    
    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click() 