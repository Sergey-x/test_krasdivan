from enum import Enum

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CatalogSectionPaths(str, Enum):
    READY_MADE_INTERIORS = "/gotovie"
    BEDROOM_PRODUCTS = "/tovary_dlya_spalni"
    LIVING_ROOM_FURNITURE = "/mebel_dlya_gostinoy"
    NURSERY_FURNITURE = "/mebel_dlya_detskoy"
    FINAL_PRICES = "/rasprodazha"
    WARDROBES = "/shkafy_kupe"
    HOUSEHOLD_GOODS = "/tovary_dlya_doma"
    UPHOLSTERY_FABRICS = "/obivochnye_tkani"


class CatalogSectionTitles(str, Enum):
    READY_MADE_INTERIORS = "Готовые интерьеры"
    BEDROOM_PRODUCTS = "Товары для спальни"
    LIVING_ROOM_FURNITURE = "Мебель для гостиной"
    NURSERY_FURNITURE = "Мебель для детской"
    FINAL_PRICES = "Финальные цены"
    WARDROBES = "Шкафы-купе"
    HOUSEHOLD_GOODS = "Товары для дома"
    UPHOLSTERY_FABRICS = "Обивочные ткани"


class CatalogSections(str, Enum):
    READY_MADE_INTERIORS = "READY_MADE_INTERIORS"
    BEDROOM_PRODUCTS = "BEDROOM_PRODUCTS"
    LIVING_ROOM_FURNITURE = "LIVING_ROOM_FURNITURE"
    NURSERY_FURNITURE = "NURSERY_FURNITURE"
    FINAL_PRICES = "FINAL_PRICES"
    WARDROBES = "WARDROBES"
    HOUSEHOLD_GOODS = "HOUSEHOLD_GOODS"
    UPHOLSTERY_FABRICS = "UPHOLSTERY_FABRICS"


class TestCatalogSections:
    BASE_PATH: str = "https://krasdivan.shop/"
    TITLE_ID: str = "pagetitle"

    def _get_catalog_page_uri(self, catalog_section: str) -> str:
        catalog_section_path: str = CatalogSectionPaths[catalog_section]
        path: str = f"{self.BASE_PATH}catalog{catalog_section_path}/"
        return path

    @pytest.mark.parametrize(
        'catalog_section',
        [
            CatalogSections.READY_MADE_INTERIORS,
            CatalogSections.BEDROOM_PRODUCTS,
            CatalogSections.LIVING_ROOM_FURNITURE,
            CatalogSections.NURSERY_FURNITURE,
            CatalogSections.FINAL_PRICES,
            CatalogSections.WARDROBES,
            CatalogSections.HOUSEHOLD_GOODS,
            CatalogSections.UPHOLSTERY_FABRICS,
        ]
    )
    def test_titles(self, driver: WebDriver, catalog_section: str):
        """Тестирование переходов по базовым разделам."""
        catalog_section_path: str = self._get_catalog_page_uri(catalog_section)
        driver.get(catalog_section_path)
        elem: WebElement = driver.find_element(By.ID, self.TITLE_ID)
        page_title: str = elem.text
        assert page_title == CatalogSectionTitles[catalog_section]
