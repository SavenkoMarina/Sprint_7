import allure
import pytest
from data import test_data
from helpers import (
    generate_random_string,
)

class TestCourierLogin:

    @allure.title("Проверка успешного логина")
    def test_login_success(self, courier_api, courier):
        response = courier_api.login(courier[0], courier[1])
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Проверка обязательных полей")
    @pytest.mark.parametrize("data", [
        test_data.COURIER_LOGIN_MISSING_LOGIN,
        test_data.COURIER_LOGIN_MISSING_PASSWORD
    ])
    def test_login_missing_fields(self, courier_api, data):
        response = courier_api.login(*data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка логина с несуществующим пользователем")
    def test_login_courier_doesnt_exist(self, courier_api):
        login = generate_random_string(10)
        password = generate_random_string(10)

        response = courier_api.login(login, password)
        assert response.status_code == 404

    @allure.title("Проверка логина с некорректным паролем")
    def test_login_wrong_password(self, courier_api, courier):
        password = generate_random_string(10)
        response = courier_api.login(courier[0], password)
        assert response.status_code == 404
