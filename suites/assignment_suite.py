from unittest import TestSuite
from testcases import search_number
from testcases import assignment

def get_assignment_suite(test_data,logger=None):
    if logger is None:
        logger = my_logger_class.create_logger()
    suite = TestSuite()
    suite.addTest(search_number.test_search_number('test_01_search_number', test_data,logger))
    logger.info("Added test_01_search_number in the test suite")
    suite.addTest(search_number.test_search_number('test_02_search_number', test_data,logger))
    logger.info("Added test_02_search_number in the test suite")
    suite.addTest(assignment.test_assignment('test_01_assignment', test_data,logger))
    logger.info("Added test_01_assignment in the test suite")
    return suite
