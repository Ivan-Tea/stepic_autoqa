from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_AGAIN = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_BUTTON_SUCCESS = (By.XPATH, '//*[@id="messages"]/div/div')


class ProductPageLocators():
    PRODUCT_URL = "?promo=offer"
    BASKET_FORM = (By.ID, "add_to_basket_form")
    BUTTON_BASKET = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    SUCCESS_FORM = (By.XPATH, '//*[@id="messages"]/*[1]/*[2]/strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '[class="btn btn-default"][href="/ru/basket/"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.ID, "logout_link")

class BasketPageLocators():
    BASKET_URL = '/ru/basket/'
    BASKET_EMPTY = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')
    BASKET_EMPTY_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')
