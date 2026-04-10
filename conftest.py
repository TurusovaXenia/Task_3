import pytest
from selenium import webdriver

from stellar_burgers.application import Application
from stellar_burgers.urls import Urls


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def app(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    app_instance = Application(driver, Urls.BASE_URL)

    yield app_instance

    driver.quit()
