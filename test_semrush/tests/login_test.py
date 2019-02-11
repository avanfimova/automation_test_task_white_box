import unittest
from selenium import webdriver
from pages.pages import HomePage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.get("https://www.semrush.com/")
        self.driver.implicitly_wait(10)

    def test_user_login(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_main_button()
        # LoginPage
        login_page.set_user("avanfimova@mail.ru", "c1103881474")
        user_page = login_page.click_login_button()
        # UserPage
        menu_page = user_page.click_user_menu_button()
        # MenuPage
        assert menu_page.assert_email, "avanfimova@mail.ru"

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
