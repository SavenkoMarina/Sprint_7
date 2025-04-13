import allure
import pytest
from data import test_data
from helpers import register_new_courier_and_return_login_password

class TestCourier:

    @allure.title("Проверка создания курьера")
    def test_create_courier_success(self):
        courier, response = register_new_courier_and_return_login_password()
        assert len(courier) == 3
        assert response.json()["ok"]
        assert response.status_code == 201

    @allure.title("Проверка создания двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier_api, courier):
        response = courier_api.create(courier[0], courier[1], courier[2])
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    @allure.title("Проверка обязательных полей при создании курьера")
    @pytest.mark.parametrize("data", [
        test_data.COURIER_MISSING_LOGIN,
        test_data.COURIER_MISSING_PASSWORD,
        test_data.COURIER_MISSING_FIRSTNAME
    ])
    def test_create_courier_missing_fields(self, courier_api, data):
        response = courier_api.create(*data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
