from pages.forgot_password_page import ForgotPasswordPage
from pages.header import Header
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage
from pages.order_history_page import OrderHistoryPage


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

    @property
    def reset_password_page(self):
        return ResetPasswordPage(self._driver, self._base_url)

    @property
    def header(self):
        return Header(self._driver, self._base_url)

    @property
    def profile_page(self):
        return ProfilePage(self._driver, self._base_url)

    @property
    def orders_history_page(self):
        return OrderHistoryPage(self._driver, self._base_url)
