import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestShoppingCart:
    START_PAGE_PATH: str = "https://krasdivan.shop/personal/cart/"
    CLASSNAME_CLEAN_CARD: str = 'remove-order'
    CLASSNAME_ADD_TO_CARD_BTN: str = 'inCart'
    CLASSNAME_SHOPPING_CARD_BADGE: str = 'items-counter'
    CLASSNAME_PRODUCT_NUMBER: str = 'basket-items-list-header-count'
    CLASSNAME_DROP_PRODUCT: str = 'basket-item-actions-remove'
    XPATH_EMPTY_TEXT: str = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]'

    def test_clean_cart(self, driver: WebDriver, product_in_cart):
        """Тестирование очищения корзины товаров с наличием там товаров."""
        driver.get(self.START_PAGE_PATH)
        driver.find_element(By.CLASS_NAME, self.CLASSNAME_CLEAN_CARD).click()
        assert driver.find_element(By.XPATH, self.XPATH_EMPTY_TEXT).text == "Ваша корзина пуста"

    def test_edit_cart(self, driver: WebDriver, empty_cart, product_in_cart, product2_in_cart):
        """Тестирование изменения количества товаров в корзине."""
        driver.get(self.START_PAGE_PATH)
        assert int(driver.find_element(By.CLASS_NAME, self.CLASSNAME_PRODUCT_NUMBER).text.split(" ")[0]) == 2
        # Удаляем товар из корзины
        driver.find_element(By.CLASS_NAME, self.CLASSNAME_DROP_PRODUCT).click()
        time.sleep(5)
        assert int(driver.find_element(By.CLASS_NAME, self.CLASSNAME_PRODUCT_NUMBER).text.split(" ")[0]) == 1
