from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from tests import utils


class TestProductSearch:
    START_PAGE_PATH: str = "https://krasdivan.shop/catalog/?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD%D1%8B"
    ID_FILTER_INPUT: str = 'searchFilter_P1_MAX'
    ID_FILTER_SUBMIT_BTN: str = 'set_filter'
    MAX_PRICE: int = 30000

    def test_filter(self, driver: WebDriver):
        """Тестирование фильтра товаров по максимальной цене."""
        driver.get(self.START_PAGE_PATH)

        # ввод максимальной цены в фильтр
        elem: WebElement = driver.find_element(By.ID, self.ID_FILTER_INPUT)
        elem.send_keys(self.MAX_PRICE)

        # нажатие кнопки "Показать"
        driver.find_element(By.ID, self.ID_FILTER_SUBMIT_BTN).click()

        # проверка, что все товары имеют цену меньше или равную `MAX_PRICE`
        prices: list[WebElement] = driver.find_elements(By.CSS_SELECTOR, ".price")
        for price in prices:
            price_int: int = utils.capture_price(price.text)
            assert price_int <= self.MAX_PRICE
