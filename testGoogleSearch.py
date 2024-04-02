import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytest_bdd import scenario, given, when, then, parsers

def pytest_bdd_step_definitions(runner):
    runner.context.browser = None

@scenario('features/googleSearch.feature', 'can find search results')
def test_google_search_results():
    pass

@scenario('features/googleSearch.feature', 'search for test observability')
def test_search_test_observability():
    pass

@scenario('features/googleSearch.feature', 'search for Browserstack accessibility')
def test_search_browserstack_accessibility():
    pass

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub"
    )
    yield browser
    browser.quit()


@given(parsers.parse('I visit url "{google}"'))
def navigate_search_url(browser, google):
    browser.get(google)
    sleep(5)

@when(parsers.parse('I search for "{text}"'))
def search_for_text(browser, text):
    search_box = browser.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(text)
    search_box.submit()
    browser.implicitly_wait(10)

@then(parsers.parse('title changes to "{title}"'))
def title_change(browser, title):
    assert title == browser.title
    print(f"Actual title: {browser.title}")
