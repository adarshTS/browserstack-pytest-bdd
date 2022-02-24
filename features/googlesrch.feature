Feature: Google\'s Search Functionality
    Scenario: can find search results
        Given I visit url "http://www.google.com/ncr"
        When I search for "BrowserStack"
        Then title changes to "BrowserStack - Google Search"