import features.lib.locators.home_locators as locators

class HomePage():
    PATH = ''

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.locators = locators.HomeLocators()

    @property
    def username_field(self):
        return self.driver.find_by_id(self.locators.USERNAME_FIELD)[0]

    @property
    def submit_button(self):
        return self.driver.find_by_id(self.locators.SUBMIT_BUTTON)[0]