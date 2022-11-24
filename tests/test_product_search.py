from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class TestProductSearch:
    START_PAGE_PATH: str = "https://krasdivan.shop"
    XPATH_SEARCH_INPUT: str = '//*[@id="title-search-input"]'
    XPATH_SEARCH_SUBMIT_BTN: str = '/html/body/div[2]/header/div[2]/div/div[3]/form/button'
    XPATH_FOUND_ELEM: str = '/html/body/div[2]/div[2]/div[2]/div/main/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/a'

    def test_good_search(self, driver: WebDriver):
        """Тестирование поиска товаров."""
        driver.get(self.START_PAGE_PATH)

        # ввод текста в поисковую строчку
        elem: WebElement = driver.find_element(By.XPATH, self.XPATH_SEARCH_INPUT)
        search_text: str = "Диваны"
        elem.send_keys(search_text)

        # нажатие кнопки "найти"
        driver.find_element(By.XPATH, self.XPATH_SEARCH_SUBMIT_BTN).click()
        first_found_product: WebElement = driver.find_element(By.XPATH, self.XPATH_FOUND_ELEM)
        assert first_found_product.text.startswith("Диван") is True
        
    def test_bad_search(self, driver: WebDriver):
        """Тестирование поиска товаров с плохим запросом."""
        driver.get(self.START_PAGE_PATH)

        # ввод текста в поисковую строчку
        elem: WebElement = driver.find_element(By.XPATH, self.XPATH_SEARCH_INPUT)
        search_text: str = "ывлоаитлыоив"
        elem.send_keys(search_text)

        # нажатие кнопки "найти"
        driver.find_element(By.XPATH, self.XPATH_SEARCH_SUBMIT_BTN).click()

        # Проверяем, что ничего не найдено
        first_found_product: WebElement = driver.find_element(By.CLASS_NAME, "empty-result")
        assert first_found_product.text == "Сожалеем, но ничего не найдено."
