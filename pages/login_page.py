from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "register form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_form.send_keys(password)
        password_again_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_AGAIN)
        password_again_form.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        self.browser.implicitly_wait(10)
        registration_success = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_SUCCESS)
        assert "Спасибо за регистрацию!" in registration_success.text
