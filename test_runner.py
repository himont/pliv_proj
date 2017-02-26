from HTMLTestRunner import HTMLTestRunner
import time
from suites.assignment_suite import *
from settings.config import *
from utils.logger import *


test_data = {'country_iso' : ISO_Country1,
                      'type' : 'any',
                      'services' : 'sms',
                      'pattern' : '33',
                      'limit' : '2',
                      'offset' : '0',
                    }
logger = logger_class.create_logger()
suite = get_assignment_suite(test_data,logger)
dateTimeStamp = time.strftime('%d-%b-%y_%X')
buf = file("/Users/himanshusharma/TestReport/TestReport_Assignment"+"_"+dateTimeStamp+".html",
               'wb')
runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            verbosity=2,
            title='Test Automation Report',
            description="Test report for assignment test"
            )
logger.info("****************** Starting execution of tests ******************")
runner.run(suite)
logger.info("****************** Completed execution of tests ******************")
buf.close()
