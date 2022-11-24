import os

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

KRASDIVAN_USER_PHONE: str = os.getenv("KRASDIVAN_USER_PHONE")
KRASDIVAN_PASSWORD: str = os.getenv("KRASDIVAN_PASSWORD")


class TestShoppingCart:
    START_PAGE_PATH: str = "https://krasdivan.shop/auth/"
    NAME_USER_NAME_INPUT: str = 'USER_LOGIN'
    NAME_USER_PASSWORD_INPUT: str = 'USER_PASSWORD'
    CLASSNAME_CLEAN_CARD: str = 'remove-order'

    CSS_SELECTOR_USERNAME: str = '.top .personal-link span'

    @pytest.mark.parametrize(
        "phone,password,awaited_username",
        [
            pytest.param(KRASDIVAN_USER_PHONE, KRASDIVAN_PASSWORD, "Sergunya", id="valid_credentials"),
            # pytest.param(KRASDIVAN_USER_PHONE, "12345", None, id="wrong_credentials"),
        ],
    )
    def test_login(self, driver: WebDriver, logout, phone, password, awaited_username):
        """Тестирование входа в личный кабинет."""
        driver.get(self.START_PAGE_PATH)

        driver.find_element(By.NAME, self.NAME_USER_NAME_INPUT).send_keys(phone)
        driver.find_element(By.NAME, self.NAME_USER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.NAME, "Login").click()

        username: str | None = None
        try:
            username = driver.find_element(By.CSS_SELECTOR, self.CSS_SELECTOR_USERNAME).text
        except NoSuchElementException:
            pass

        assert username == awaited_username
