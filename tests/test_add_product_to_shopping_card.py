import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestAddShoppingCard:
    START_PAGE_PATH: str = "https://krasdivan.shop/catalog/divany/25446/"
    CLASSNAME_PRODUCT_CARD: str = 'product-card'
    CLASSNAME_ADD_TO_CARD_BTN: str = 'inCart'
    CLASSNAME_SHOPPING_CARD_BADGE: str = 'items-counter'

    def _get_shopping_card_badge_value(self, driver: WebDriver) -> int:
        shopping_badge: int = int(driver.find_element(By.CLASS_NAME, self.CLASSNAME_SHOPPING_CARD_BADGE).text)
        return shopping_badge

    def test_add_to_shopping_card(self, driver: WebDriver):
        """Тестирование добавления товара в корзину.

        Добавляется первый товар. Сравнивается количество товаров в корзине до и после добавления.
        """
        driver.get(self.START_PAGE_PATH)

        # Количество товаров в корзине до добавления товара
        shopping_badge_before: int = self._get_shopping_card_badge_value(driver)

        # Добавление или удаление товара из корзины
        driver.find_element(By.CLASS_NAME, self.CLASSNAME_ADD_TO_CARD_BTN).click()

        time.sleep(10)
        # Количество товаров в корзине после добавления товара
        shopping_badge_after: int = self._get_shopping_card_badge_value(driver)
        assert abs(shopping_badge_after - shopping_badge_before) == 1
