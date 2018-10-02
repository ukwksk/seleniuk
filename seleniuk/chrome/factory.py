# -*- coding:utf-8 -*-
import os

from selenium.webdriver import ChromeOptions

from .webdriver import ChromeDriver, enable_headless_download


class DriverFactory:
    @classmethod
    def __format_driverpath(cls, path=None):
        default = 'chromedriver'

        if path is None or path == default:
            path = default

        elif path.startswith('~'):
            path = os.path.expanduser(path)

        else:
            path = os.path.abspath(path)

        return path

    @classmethod
    def __setup_options(cls, options, **kwargs):
        op = dict(
            headless='--headless' in options.arguments,
            downloadpath=kwargs.get('downloadpath', None)
        )

        return op

    def __init__(self, driverpath=None, options=None,
                 setup_func=None, *args, **kwargs):

        if hasattr(options, '__iter__'):
            _options = ChromeOptions()
            for op in options:
                _options.add_argument('--no-sandbox')
            options = _options

        if options is not None \
                and not isinstance(options, ChromeOptions):
            raise TypeError("'chrome_options' must be "
                            "'webdriver.ChromeOptions' or iteration of 'str'.")

        self.driverpath = self.__format_driverpath(driverpath)
        self.options = options or ChromeOptions()
        self.driver_setup = setup_func if setup_func else self.__setup_func
        self.setup_options = \
            self.__setup_options(self.options, **kwargs)
        self.driver = None

    def __enter__(self):
        self.driver = ChromeDriver(
            executable_path=self.driverpath,
            options=self.options)
        self.driver_setup(**self.setup_options)

        self.driver.implicitly_wait(5)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()

    def __setup_func(self, headless=False, downloadpath=None):
        if headless and downloadpath:
            enable_headless_download(self.driver, downloadpath)
