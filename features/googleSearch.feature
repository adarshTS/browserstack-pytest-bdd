Feature: Google\'s Search Functionality
    Scenario: can find search results
        Given I visit url "http://www.google.com"
        When I search for "BrowserStack"
        Then title changes to "BrowserStack - Google Search"

   Scenario: search for test observability
        Given I visit url "http://www.google.com"
        When I search for "test observability"
        Then title changes to "test observability - Google Search"

      Scenario: search for Browserstack accessibility
        Given I visit url "http://www.google.com"
        When I search for "Browserstack accessibility"
        Then title changes to "Browserstack accessibility - Google Search"