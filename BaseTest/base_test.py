from BasePage.base_nav import BaseElement



class Asserts(BaseElement):

    def assert_current(self, link):
        assert link in self.current_url(), 'Incorrect url was opened.'


    def assert_equal_game_genre(self, selector, genres):
        x = self.find_element(selector).text
        assert x in genres, 'Incorrect game genre was opened.'


    def assert_tab_opened(self, tab_name):
        assert tab_name in self.current_url(), 'Incorrect tab was opened'


    def assert_equal(self, first_value, second_value):
        assert all(elem in second_value for elem in first_value), 'Values is not equal.'



