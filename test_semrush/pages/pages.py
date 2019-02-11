
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def click_main_button(self):
        self.driver.find_element_by_id("srf-login-btn").click()
        return LoginPage(self.driver)


class LoginPage(BasePage):

    def set_user(self, email, password):
        self.driver.find_element_by_xpath(".//input[@name='email']").send_keys(email)
        self.driver.find_element_by_xpath(".//input[@name='password']").send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(".//button[@data-test='auth-popup__submit']").click()
        return UserPage(self.driver)


class UserPage(BasePage):

    def click_user_menu_button(self):
        self.driver.find_element_by_xpath(".//div[@data-test='header-menu__user']").click()
        return MenuPage(self.driver)

    def click_note_page_button(self):
        self.driver.find_element_by_xpath(".//a[@data-ga-label='notes']").click()
        return NotePage(self.driver)

    def click_project_page_button(self):
        self.driver.find_element_by_xpath(".//a[@data-ga-label='projects']").click()
        return ProjectPage(self.driver)


class MenuPage(BasePage):

    def assert_email(self):
        self.driver.find_element_by_xpath(".//div[@class='header-dropdown__description']").text


class NotePage(BasePage):

    def click_new_note(self):
        self.driver.find_element_by_xpath(".//button[@data-cream-action='add-note']").click()
        return NewNotePage(self.driver)

    def assert_note(self):
        self.driver.find_element_by_xpath(".//span[@class='notes-note-title']").text


class NewNotePage(BasePage):

    def set_new_note(self, title, description):
        self.driver.find_element_by_xpath(".//input[@data-cream-ui='input-title']").send_keys(title)
        self.driver.find_element_by_xpath(".//textarea[@data-cream-ui='input-note']").send_keys(description)

    def click_save_note_button(self):
        self.driver.find_element_by_xpath(".//button[@data-cream-action='save']").click()
        return NotePage(self.driver)


class ProjectPage(BasePage):

    def click_new_project(self):
        self.driver.find_element_by_xpath(".//button//span[text()='Add New Project']").click()
        return NewProjectPage(self.driver)

    def assert_project(self):
        self.driver.find_element_by_xpath(".//span[@class='pr-page__title-name']").get_attribute("title")


class NewProjectPage(BasePage):

    def set_new_project(self, domain, name):
        self.driver.find_element_by_xpath(".//input[@name='url']").send_keys(domain)
        self.driver.find_element_by_xpath(".//input[@name='name']").send_keys(name)

    def click_save_project_button(self):
        self.driver.find_element_by_xpath(".//button//span[text()='Create project']").click()
        return ProjectPage(self.driver)
