from stellar_burgers.pages.forgot_password_page import ForgotPasswordPage
from stellar_burgers.pages.home_page import HomePage
from stellar_burgers.pages.login_page import LoginPage


class Application:
    def __init__(self, driver, base_url):
        self._driver = driver
        self._base_url = base_url

    @property
    def login_page(self):
        return LoginPage(self._driver, self._base_url)

    @property
    def forgot_password_page(self):
        return ForgotPasswordPage(self._driver, self._base_url)

    @property
    def home_page(self):
        return HomePage(self._driver, self._base_url)
