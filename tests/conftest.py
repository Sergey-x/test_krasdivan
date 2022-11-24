import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# class, module, package or session
@pytest.fixture(scope="class")
def driver() -> WebDriver:
    """Фикстура создает драйвер для работы с веб-страницами."""
    driver = webdriver.Firefox()
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def product_in_cart(driver: WebDriver) -> None:
    """Фикстура добавляет товар в корзину."""
    driver.get("https://krasdivan.shop/catalog/gotovie%20/25525/")
    driver.find_element(By.CLASS_NAME, "inCart").click()


@pytest.fixture(scope="function")
def product2_in_cart(driver: WebDriver) -> None:
    """Фикстура добавляет товар в корзину."""
    driver.get("https://krasdivan.shop/catalog/divany/23852/")
    driver.find_element(By.CLASS_NAME, "inCart").click()


@pytest.fixture(scope="function")
def empty_cart(driver: WebDriver) -> None:
    """Фикстура очищает корзину."""
    driver.get("https://krasdivan.shop/personal/cart/")
    try:
        driver.find_element(By.CLASS_NAME, "remove-order").click()
    except NoSuchElementException:
        pass


@pytest.fixture(scope="function")
def logout(driver: WebDriver) -> None:
    """Фикстура выхода."""
    driver.get("https://krasdivan.shop/")
    XPATH_LOGOUT_BTN: str = '/html/body/div[2]/div[2]/div[2]/div/div/ul/li[8]/a'

    try:
        driver.find_element(By.CLASS_NAME, "personal-link").click()
        driver.find_element(By.XPATH, XPATH_LOGOUT_BTN).click()
    except NoSuchElementException:
        pass
