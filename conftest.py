import pytest
from selenium import webdriver

from api.api_client import ApiClient
from pages.application import Application
from urls import Urls
from utils import helpers


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def app(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    app_instance = Application(driver, Urls.BASE_URL)

    yield app_instance

    driver.quit()


@pytest.fixture(scope="function")
def api_client():
    return ApiClient(Urls.BASE_URL)


@pytest.fixture(scope="function")
def user_for_test(api_client):
    new_user_data = helpers.generate_new_user()
    response = api_client.create_user(new_user_data)
    access_token = response.json().get("accessToken")
    setup_data = {
        "access_token": access_token,
        "name": new_user_data["name"],
        "email": new_user_data["email"],
        "password": new_user_data["password"],
    }

    yield setup_data

    if access_token:
        api_client.delete_user(access_token)


@pytest.fixture(scope="function")
def created_order(app, user_for_test):
    app.home_page.open()
    app.login_page.click_login_button()
    app.login(user_for_test)
    app.home_page.drag_first_ingredient_and_drop_to_basket()
    app.home_page.click_create_order_button()
    order_id = app.home_page.get_order_id()
    app.home_page.click_cross_button_for_order()
    return order_id
