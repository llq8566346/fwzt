
import unittest
import os
from common.handlepath import CASEDIR,REPORTDIR
from HTMLTestRunnerNew import HTMLTestRunner
from common.handle_email import send_email

# 第一步：创建套件

suite = unittest.TestSuite()

# 第二步：加载用例到套件

loader = unittest.TestLoader()

suite.addTest(loader.discover(CASEDIR))

report_file = os.path.join(REPORTDIR,"report1.html")

# 第三步：执行用例

runner = HTMLTestRunner(stream=open(report_file, "r+b"),
                        description="第一次接口测试报告",
                        title="py26测试报告",
                        tester="musen"
                        )

runner.run(suite)

send_email(report_file,"1点01分的邮件.html")
