import unittest
from selenium import webdriver
from pages.pages import HomePage


class ProjectTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.get("https://www.semrush.com/")
        self.driver.implicitly_wait(10)

    def test_project(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_main_button()
        # LoginPage
        login_page.set_user("avanfimova@mail.ru", "c1103881474")
        user_page = login_page.click_login_button()
        # UserPage
        project_page = user_page.click_project_page_button()
        # ProjectPage
        new_project_page = project_page.click_new_project()
        # NewProjectPage
        new_project_page.set_new_project("http://testproject.ru", "Test Project")
        new_project = new_project_page.click_save_project_button()
        # ProjectPage
        assert new_project.assert_project, "Test Project"
        # delete project

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
