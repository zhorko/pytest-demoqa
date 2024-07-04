from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from pages.elements_page import CatPage
from pages.radio_page import RadioPage
from pages.form_page import FormPage

import pandas as pd
from bs4 import BeautifulSoup

import json

def test_radio(_browser):

    wait = WebDriverWait(_browser, 10)

    # Initializations
    home_page = HomePage(_browser)
    cat_page = CatPage(_browser)
    radio_page = RadioPage(_browser)

    # Loads page for driver
    home_page.load()

    home_page.open_elements(wait)
    cat_page.open_radio(wait)

    radio_page.click_radio(wait, "YeS")
    assert radio_page.get_radio_status(wait, "yes") is True

    radio_page.click_radio(wait, "impressive")
    assert radio_page.get_radio_status(wait, "impressive") is True

def test_form(_browser):

    wait = WebDriverWait(_browser, 10)
    
    with open('./data/test_data.json', 'r') as JF:
        json_data = json.load(JF)

    # Initialization
    form_page = FormPage(_browser)
    home_page = HomePage(_browser)
    cat_page = CatPage(_browser)

    # Open "Form" page
    home_page.load()
    home_page.open_forms(wait)
    cat_page.open_forms(wait)

    # Fill form
    form_page.fill_name([json_data["form"]["first_name"], json_data["form"]["last_name"]])
    form_page.fill_email(json_data["form"]["email"])
    form_page.fill_gender(json_data["form"]["gender"])
    form_page.fill_phone(json_data["form"]["phone"])
    form_page.fill_dob(json_data["form"]["dob"])
    form_page.fill_subjects(wait, json_data["form"]["subjects"])
    form_page.fill_hobbies(wait, dict(json_data["form"]["hobbies"]))
    form_page.fill_address(json_data["form"]["address"])
    form_page.fill_state(wait, json_data["form"]["state"])
    form_page.fill_city(wait, json_data["form"]["city"])
    form_page.submit()

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

    # Checks whether 'True' values in dictionary are dispalyed on form
    for index, val in dict(json_data["form"]["hobbies"]).items():
            if val is True:
                assert index in df[0].iat[6,1].lower().replace(',', '').split()

    assert df[0].iat[8,1] == json_data["form"]["address"]
    assert df[0].iat[9,1].split()[0] == json_data["form"]["state"]
    assert df[0].iat[9,1].split()[1] == json_data["form"]["city"]