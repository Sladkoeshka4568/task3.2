from selenium import webdriver
from CommonFunctions.data_getter_module import JsonDataGetter


class BrowserEngine:
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        browser = JsonDataGetter.browser
        url = JsonDataGetter.url

        if browser == "Firefox":
            driver = webdriver.Firefox()
        elif browser == "Chrome":
            driver = webdriver.Chrome()

        driver.get(url)
        driver.maximize_window()
        return driver

    def quit_browser(self):
        self.driver.quit()
