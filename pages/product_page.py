from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        # self.should_be_product_url()
        self.should_be_basket_form()
        self.add_to_basket()
        self.should_be_success()
        # self.should_not_be_success_message()
        # self.should_is_disappeared()

    def should_be_product_url(self):
        assert ProductPageLocators.PRODUCT_URL in self.browser.current_url

    def should_be_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_FORM), "Basket button form is not presented"

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        link.click()
        # self.solve_quiz_and_get_code()

    def should_be_success(self):
        book = self.browser.find_element(*ProductPageLocators.SUCCESS_FORM)
        assert "Coders at Work" == book.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_FORM), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_FORM), "Success message is disappeared"
