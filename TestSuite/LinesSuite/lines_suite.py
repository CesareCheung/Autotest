# 线路模块测试套件
import unittest
from TestCase.BusinessCase.LinesCase import lines_case


def return_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(lines_case.Test_Business))

    return suite
