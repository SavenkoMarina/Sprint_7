import allure
import pytest
from data import test_data
from datetime import datetime, timedelta

class TestOrderCreation:

    @allure.title("Проверка создания заказа")
    @pytest.mark.parametrize("colors", [
        test_data.FIRST_COLOR,
        test_data.SECOND_COLOR,
        test_data.BOTH_COLORS,
        [],
    ])
    def test_create_order_with_colors(self, order_api, colors):
        delivery_date = datetime.now()+timedelta(days=3)
        response = order_api.create(
            test_data.FIRST_NAME, test_data.LAST_NAME,
            test_data.ADDRESS, test_data.METRO_STATION,
            test_data.PHONE, test_data.RENT_TIME,
            delivery_date.strftime("%Y-%m-%d"),
            test_data.COMMENT, colors
        )
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Проверка получения списка заказов")
    def test_get_orders_list(self, order_api):
        response = order_api.list()
        assert response.status_code == 200
        assert "orders" in response.json()
