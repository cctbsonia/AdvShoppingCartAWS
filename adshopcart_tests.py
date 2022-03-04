import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdvantageShoppingAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_advantage_shopping():
        methods.setUp()
        methods.check_homepage()
        methods.check_top_menu()
        methods.check_logo()
        methods.check_contact_us_form()
        methods.signUp()
        methods.check_my_account_display_full_name()
        methods.check_no_order()
        methods.sign_out()
        methods.log_in()
        methods.delete_account()
        methods.check_re_login()
        methods.tearDown()

