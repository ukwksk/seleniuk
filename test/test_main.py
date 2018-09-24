# -*- coding:utf-8 -*-
import unittest

import seleniuk


class TestMain(unittest.TestCase):

    def setUp(self):
        self.options = seleniuk.chrome.Options()
        self.options.add_argument("--headless")

    def test_get(self):
        with seleniuk.Chrome(options=self.options) as driver:
            driver.get('https://google.com')
            self.assertIn('google', driver.title.lower())


if __name__ == "__main__":
    unittest.main()
