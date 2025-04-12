import allure
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

class CourierAPI:
    def __init__(self):
        self.base = f"{BASE_URL}/api/v1/courier"

    @allure.step("Создание курьера")
    def create(self, login, password, first_name):
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(self.base, json=data)

    @allure.step("Авторизация курьера")
    def login(self, login, password):
        data = {
            "login": login,
            "password": password,
        }
        return requests.post(f"{self.base}/login", json=data)


class OrderAPI:
    def __init__(self):
        self.base = f"{BASE_URL}/api/v1/orders"

    @allure.step("Создание заказа")
    def create(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, colors):
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": colors
        }
        return requests.post(self.base, json=data)

    @allure.step("Получение списка заказов")
    def list(self):
        return requests.get(self.base)
