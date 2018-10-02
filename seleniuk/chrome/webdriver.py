# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

OP_HEADLESS = '--headless'
OP_NO_SANDBOX = '--no-sandbox'
OP_DISABLE_GPU = '--disable-gpu'
OP_DISABLE_POPUP_BLOCING = '--disable-popup-blocking'
OP_DISABLE_EXTENSIONS = "--disable-extensions"
OP_START_MAXIMIZED = '--start-maximized'

OP_LANG_EN_US = '--lang=en-US'
OP_LANG_JA = '--lang=ja'

OP_UA_OSX_HIGH_SIERRA = \
    '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) ' \
    'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
    'Chrome/69.0.3497.100 Safari/605.1.15'


def enable_headless_download(driver, downloadpath):
    driver.command_executor._commands["send_command"] = \
        ("POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {'behavior': 'allow',
                   'downloadPath': downloadpath}
    }
    driver.execute("send_command", params)


class ChromeDriver(webdriver.Chrome):
    def __find_element(self, by, value, n=None):
        if n is None:
            e = self.find_element(by=by, value=value)
        else:
            e = self.find_elements(by=by, value=value)[n]

        return e

    def __click_by(self, by, value, n=None):
        e = self.__find_element(by, value, n)
        e.click()

    def click_by_xpath(self, xpath, n=None):
        self.__click_by(By.XPATH, xpath, n)

    def click_by_id(self, id_, n=None):
        self.__click_by(By.ID, id_, n)

    def click_by_link_text(self, text, n=None):
        self.__click_by(By.LINK_TEXT, text, n)

    def click_by_css(self, css, n=None):
        self.__click_by(By.CSS_SELECTOR, css, n)

    def click_by_name(self, name, n=None):
        self.__click_by(By.NAME, name, n)

    def click_by_tag(self, tag, n=None):
        self.__click_by(By.TAG_NAME, tag, n)

    def __send_keys_by(self, by, value, n=None, keys=''):
        if not isinstance(keys, str) \
                or not all((isinstance(k, str) for k in keys)):
            raise ValueError("keys must be str or Iter[str].")
        if not hasattr(keys, '__iter__'):
            keys = [keys]

        e = self.__find_element(by, value, n)
        for k in keys:
            e.send_keys(k)

    def send_keys_by_xpath(self, xpath, n=None):
        self.__send_keys_by(By.XPATH, xpath, n)

    def send_keys_by_id(self, id_, n=None):
        self.__send_keys_by(By.ID, id_, n)

    def send_keys_by_link_text(self, text, n=None):
        self.__send_keys_by(By.LINK_TEXT, text, n)

    def send_keys_by_css(self, css, n=None):
        self.__send_keys_by(By.CSS_SELECTOR, css, n)

    def send_keys_by_name(self, name, n=None):
        self.__send_keys_by(By.NAME, name, n)

    def send_keys_by_tag(self, tag, keys, n=None):
        self.__send_keys_by(By.TAG_NAME, tag, n, keys)
