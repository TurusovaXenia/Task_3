from pages.forgot_password_page import ForgotPasswordPage
from pages.header import Header
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage


class Application:
    def __init__(self, driver, base_url):
        self._driver = driver
        self._base_url = base_url

    @property
    def login_page(self):
        return LoginPage(self._driver, self._base_url)

    def login(self, user_data):
        self.login_page.login(user_data)
        self.home_page.wait_for_load()
        return self.home_page

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

    @property
    def order_feed_page(self):
        return OrderFeedPage(self._driver, self._base_url)
