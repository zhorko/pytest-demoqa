import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert acceptable values
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Headless Firefox']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture()
def _browser(config):

    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()

    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opts)

    elif config['browser'] == 'Headless Firefox':
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument('-headless')
        driver = selenium.webdriver.Firefox(options=opts)

    # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])
    
    driver.maximize_window()
    
    yield driver

    driver.quit()