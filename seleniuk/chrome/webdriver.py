# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By


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
