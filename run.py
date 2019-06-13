# 脚本运行文件
import unittest
from TestSuite.LinesSuite import lines_suite
from TestSuite.LinesSuite import itinerary_suite

import HTMLReport

suite = unittest.TestSuite()

# suite.addTests(login_suite.return_suite())
suite.addTests(lines_suite.return_suite())
# suite.addTests(itinerary_suite.return_suite())

HTMLReport.TestRunner(
    report_file_name="test",
    title='WEB UI 自动化',
    description='ERP项目',
    thread_count=3
).run(suite)
