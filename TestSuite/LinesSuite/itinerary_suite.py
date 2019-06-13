# 行程模块测试套件
import unittest
from TestCase.BusinessCase.TicketManagCase import itinerary_case


def return_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(itinerary_case.Test_Itinerary_Test))
    return suite
