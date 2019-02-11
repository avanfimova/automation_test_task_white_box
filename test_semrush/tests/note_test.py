import unittest
from selenium import webdriver
from pages.pages import HomePage


class NoteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.get("https://www.semrush.com/")
        self.driver.implicitly_wait(10)

    def test_note(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_main_button()
        # LoginPage
        login_page.set_user("avanfimova@mail.ru", "c1103881474")
        user_page = login_page.click_login_button()
        # UserPage
        note_page = user_page.click_note_page_button()
        # NotePage
        new_note_page = note_page.click_new_note()
        # NewNotePage
        new_note_page.set_new_note("Test title", "Test description")
        new_note = new_note_page.click_save_note_button()
        # NotePage
        assert new_note.assert_note, "Test title"
        # delete note

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
