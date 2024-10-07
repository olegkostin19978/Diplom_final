import pytest
import allure
from web_pages.CompanyApi import CompanyApi

API_URL = "https://web-gate.chitai-gorod.ru/api/v1"
BEARER_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDU4MjQ0LCJpYXQiOjE3MjY1ODcyNDgsImV4cCI6MTcyNjU5MDg0OCwidHlwZSI6MjB9.SZkZNCG_gtsGvEodjfl11O1-DsqU6E8X4RjA8Qo6uZo"


@allure.title("Добавить продукт в корзину")
@allure.description(
    "Тест проверяет функциональность добавления продукта в корзину"
)
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api_test
def test_add_product_to_cart():
    company_api = CompanyApi(API_URL, BEARER_TOKEN)

    product_data = {
        "id": 2366814,
        "adData": {"item_list_name": "search", "product_shelf": ""},
    }

    with allure.step("Добавление продукта в корзину"):
        response = company_api.add_product_to_cart(product_data)

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка тела ответа"):
        assert response.text == "", "Ожидался пустой ответ"


@allure.title("Получить содержимое корзины")
@allure.description(
    "Тест проверяет функциональность получения содержимого корзины"
)
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api_test
def test_retrieve_cart_contents():
    company_api = CompanyApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение содержимого корзины"):
        response = company_api.get_cart_contents()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Ожидался непустой ответ"


@allure.title("Очистить корзину")
@allure.description("Тест проверяет функциональность очистки корзины")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api_test
def test_clear_cart():
    company_api = CompanyApi(API_URL, BEARER_TOKEN)

    with allure.step("Очистка корзины"):
        response = company_api.clear_cart()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 204, "Ожидался статус код 204 No Content"

    with allure.step("Проверка тела ответа"):
        assert response.text == "", "Ожидалось пустое тело ответа"


@allure.title("Получить список магазинов")
@allure.description(
    "Тест проверяет функциональность получения списка магазинов"
)
@allure.feature("Управление магазинами")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api_test
def test_get_shops_list():
    company_api = CompanyApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка магазинов"):
        response = (
            company_api.get_shops()
        )  # Нет параметров, так как тело не нужно

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Ожидался непустой список"


@allure.title("Получить список стран, где есть магазины")
@allure.description(
    "Тест проверяет функциональность получения списка доступных стран"
)
@allure.feature("Управление странами")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api_test
def test_get_countries_list():
    company_api = CompanyApi(API_URL, BEARER_TOKEN)

    with allure.step("Получение списка стран"):
        response = company_api.get_countries()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Ожидался непустой список"
