# -*- coding: UTF-8 -*-
import unittest


from iot_push_Statistics import Statistics


class WidgetTestCase(unittest.TestCase, Statistics):
    def setUp(self):
        print(1111)

    def setUd(self):
        print(2222)

    def test1(self):
        self.dowm()
        self.iot_assertion()

    def test2(self):

        self.assertEqual(4, 5, '222')

    def test3(self):

        self.assertEqual(4, 5, '333')


if __name__ == "__main__":
    unittest.main()
