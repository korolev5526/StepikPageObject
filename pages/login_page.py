
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "String \"login\" not in url login page"

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM), "Login form not in login page"

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FORM), "Registration form not in login page"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        register_btn = self.browser.find_element(
            *LoginPageLocators.SUBMIT_REGISTER_BUTTON)
        register_btn.click()
