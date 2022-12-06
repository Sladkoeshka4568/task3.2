class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def current_url(self):
        url = self.driver.current_url
        return url