# -*- coding:utf-8 -*-
import unittest

import seleniuk
from seleniuk.chrome.webdriver import *


class TestMain(unittest.TestCase):

    def setUp(self):
        self.options = seleniuk.chrome.Options()
        self.options.add_argument("--headless")

    def test_get(self):
        with seleniuk.Chrome(options=self.options) as driver:
            driver.get('https://google.com')
            self.assertIn('google', driver.title.lower())


class TestOption(unittest.TestCase):

    def setUp(self):
        self.options = (
            OP_HEADLESS,
            OP_DISABLE_GPU,
            OP_DISABLE_EXTENSIONS,
            OP_LANG_EN_US,
            OP_UA_OSX_HIGH_SIERRA,
        )

    def test_get(self):
        with seleniuk.Chrome(options=self.options) as driver:
            driver.get('https://google.com')
            self.assertIn('google', driver.title.lower())


if __name__ == "__main__":
    unittest.main()
