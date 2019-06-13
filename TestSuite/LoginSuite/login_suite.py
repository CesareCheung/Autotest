# 登录测试套件

import unittest

from TestCase.LoginCase import login_case


def return_suite():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(login_case.Test_login))

    return suite
