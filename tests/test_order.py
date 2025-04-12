import allure
import pytest
from data import test_data
from datetime import datetime, timedelta

class TestOrderCreation:

    @allure.title("Проверка создания заказа")
    @pytest.mark.parametrize("colors", [
        test_data.first_color(),
        test_data.second_color(),
        test_data.both_colors(),
        [],
    ])
    def test_create_order_with_colors(self, order_api, colors):
        delivery_date = datetime.now()+timedelta(days=3)
        response = order_api.create(
            "test", "user", "test street", 4,
            "+7 999 000 00 00", 5, delivery_date.strftime("%Y-%m-%d"),
            "test order", colors
        )
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Проверка получения списка заказов")
    def test_get_orders_list(self, order_api):
        response = order_api.list()
        assert response.status_code == 200
        assert "orders" in response.json()
