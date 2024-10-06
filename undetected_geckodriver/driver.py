# Imports #
import os

from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.remote_connection import FirefoxRemoteConnection
from selenium.webdriver.firefox.service import Service

from .mixins import WebDriverMixin
from .utils  import (
    _get_webdriver,
    _get_firefox_path,
    _get_selenium_config_path,
    _create_undetected_firefox,
    _patch_libxul,
)

# Main class #
class Firefox(RemoteWebDriver, WebDriverMixin):
    """
    A custom Firefox WebDriver that attempts to avoid detection by web services.
    """

    def __init__(
        self, options: Options = None, service: Service = None, keep_alive: bool = True
    ) -> None:
        self.webdriver = _get_webdriver()

        self._firefox_path = _get_firefox_path()
        self._selenium_config_path = _get_selenium_config_path()
        self._undetected_path = _create_undetected_firefox(
            self._firefox_path, self._selenium_config_path
        )
        _patch_libxul(self._undetected_path)

        self.service = service if service else Service()
        options = options if options else Options()
        options.binary_location = os.path.join(self._undetected_path, "firefox")

        finder = DriverFinder(self.service, options)

        self.service.path = finder.get_driver_path()
        self.service.start()

        executor = FirefoxRemoteConnection(
            remote_server_addr=self.service.service_url,
            keep_alive=keep_alive,
            ignore_proxy=options._ignore_local_proxy,
        )
        try:
            super().__init__(command_executor=executor, options=options)
        except Exception:
            self.quit()
            raise
        self._is_remote = False