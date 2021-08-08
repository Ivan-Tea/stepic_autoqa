from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators():
    PRODUCT_URL = "?promo=offer"
    BASKET_FORM = (By.ID, "add_to_basket_form")
    BUTTON_BASKET = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    SUCCESS_FORM = (By.XPATH, '//*[@id="messages"]/*[1]/*[2]/strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '[class="btn btn-default"][href="/ru/basket/"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_URL = '/ru/basket/'
    BASKET_EMPTY = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')
    BASKET_EMPTY_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')
