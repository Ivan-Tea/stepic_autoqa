from .base_page import BasePage
from .locators import BasketPageLocators
# проверяем что в корзине нет товаров


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_empty_basket()
        self.should_be_text_empty_basket()

    def should_be_basket_url(self):
        assert BasketPageLocators.BASKET_URL in self.browser.current_url

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"

    def should_be_text_empty_basket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        assert "Ваша корзина пуста" in basket_text.text



