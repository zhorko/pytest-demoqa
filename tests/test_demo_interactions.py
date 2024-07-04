from selenium.webdriver.support.wait import WebDriverWait 

from pages.demo_home_page import DemoHomePage
from pages.demo_elements_page import DemoCatPage
from pages.demo_radio_page import DemoRadioPage
from pages.demo_form_page import DemoFormPage

import pandas as pd
from bs4 import BeautifulSoup

import json

def test_demo_interactions(_browser):
    
    URL = "https://demoqa.com/"
    wait = WebDriverWait(_browser, 10)
    name_list = []

    _browser.maximize_window()
    _browser.get(URL)
    
    # Open json file
    with open('./data/test_data.json', 'r') as JF:
        json_data = json.load(JF)

    # Initializations
    demo_home_page = DemoHomePage(_browser)
    demo_elem_page = DemoCatPage(_browser)
    demo_radio_page = DemoRadioPage(_browser)
    demo_form_page = DemoFormPage(_browser)

    demo_home_page.open_elements(wait)
    demo_elem_page.open_radio(wait)
    
    demo_radio_page.click_radio(wait, "YeS")
    assert demo_radio_page.get_radio_status(wait, "yes") is True

    demo_radio_page.click_radio(wait, "impressive")
    assert demo_radio_page.get_radio_status(wait, "impressive") is True
    # Open "Form" page
    demo_radio_page.get_home()
    demo_home_page.open_forms(wait)
    demo_elem_page.open_forms(wait)
    
    name_list.append(json_data["form"]["first_name"])
    name_list.append(json_data["form"]["last_name"])
    demo_form_page.fill_name(name_list)
    
    # Fill form
    demo_form_page.fill_email(json_data["form"]["email"])
    demo_form_page.fill_gender(json_data["form"]["gender"])
    demo_form_page.fill_phone(json_data["form"]["phone"])
    demo_form_page.fill_dob(json_data["form"]["dob"])
    demo_form_page.fill_subjects(wait, json_data["form"]["subjects"])
    demo_form_page.fill_hobbies(wait, dict(json_data["form"]["hobbies"]))
    demo_form_page.fill_addres(json_data["form"]["address"])
    demo_form_page.fill_state(wait, json_data["form"]["state"])
    demo_form_page.fill_city(wait, json_data["form"]["city"])
    demo_form_page.submit()
    
    # Initialize bs4
    HTML = _browser.page_source
    soup = BeautifulSoup(HTML, "html.parser")
    tbl = soup.select_one("table.table")
    df = pd.read_html(str(tbl))
    
    # Assert data after submit form
    assert df[0].iat[0,1] == (json_data["form"]["first_name"] + " " + json_data["form"]["last_name"])
    assert df[0].iat[1,1] == json_data["form"]["email"]
    assert df[0].iat[2,1] == json_data["form"]["gender"]
    assert df[0].iat[3,1] == json_data["form"]["phone"]
    assert bool(set(json_data["form"]["dob"].split()).intersection(df[0].iat[4,1].replace(',', ' ').split()))
    assert df[0].iat[5,1].replace(',', ' ').split() == json_data["form"]["subjects"]
    assert f"{df[0].iat[6,1].replace(',', '').split() = }"
    
    for index, val in dict(json_data["form"]["hobbies"]).items():
            if val is True:
                assert index in df[0].iat[6,1].lower().replace(',', '').split()
    
    assert df[0].iat[8,1] == json_data["form"]["address"]
    assert df[0].iat[9,1].split()[0] == json_data["form"]["state"]
    assert df[0].iat[9,1].split()[1] == json_data["form"]["city"]