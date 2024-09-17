import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from web_pages.MainPage import MainPage
from web_pages.ResultPage import ResultPage


@pytest.mark.ui_test
@allure.title("Тест открытия страницы корзины")
@allure.description("Проверка, что текст заголовка страницы корзины соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_cart_page():
    """Тест для открытия страницы корзины и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_cart()

        cart_page = ResultPage(browser)
        cart_text = cart_page.get_cart_text()

        with allure.step("Проверка текста заголовка корзины"):
            assert cart_text == "КОРЗИНА", f"Expected 'Корзина' but got '{cart_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы акций")
@allure.description("Проверка, что текст заголовка страницы акций соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_promotions_page():
    """Тест для открытия страницы акций и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_promotions()

        promotions_page = ResultPage(browser)
        promotions_text = promotions_page.get_promotions_text()

        with allure.step("Проверка текста заголовка акций"):
            assert promotions_text == "АКЦИИ", f"Expected 'АКЦИИ' but got '{promotions_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы распродаж")
@allure.description("Проверка, что текст заголовка страницы распродаж соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_sales_page():
    """Тест для открытия страницы распродаж и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_sales()

        sales_page = ResultPage(browser)
        sales_text = sales_page.get_sales_text()

        with allure.step("Проверка текста заголовка распродаж"):
            assert sales_text == "РАСПРОДАЖА", f"Expected 'РАСПРОДАЖА' but got '{sales_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы магазинов")
@allure.description("Проверка, что текст заголовка страницы магазинов соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_shops_page():
    """Тест для открытия страницы магазинов и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_shops()

        shops_page = ResultPage(browser)
        shops_text = shops_page.get_shops_text()

        with allure.step("Проверка текста заголовка магазинов"):
            assert shops_text == "НАШИ МАГАЗИНЫ", f"Expected 'НАШИ МАГАЗИНЫ' but got '{shops_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы журнала")
@allure.description("Проверка, что текст заголовка страницы журнала соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_articles_page():
    """Тест для открытия страницы журнала и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_articles()

        articles_page = ResultPage(browser)
        articles_text = articles_page.get_articles_text()

        with allure.step("Проверка текста заголовка журнала"):
            assert articles_text == "ЧИТАЙ-ЖУРНАЛ", f"Expected 'ЧИТАЙ-ЖУРНАЛ' but got '{articles_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Проверка заголовка первой книги после поиска")
@allure.description(
    "Проверяем, что заголовок первой книги на странице результатов поиска соответствует ожидаемому значению.")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.NORMAL)
def test_find_first_book_title():
    search_value = "Стивен Кинг идет в кино"  # Ожидаемый заголовок первой книги
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        main_page = MainPage(browser)
        main_page.find_books(search_value)  # Ищем книгу по названию

        result_page = ResultPage(browser)
        first_book_title = result_page.get_book_title()  # Получаем заголовок первой книги

        assert first_book_title == search_value, f"Expected '{search_value}' but got '{first_book_title}'"
    finally:
        browser.quit()