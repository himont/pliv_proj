from masterTest import *
from utils.common_utils import *
from settings.config import *


class test_search_number(masterTest):
    def __init__(self, testName, data, log):
        super(test_search_number, self).__init__(testName)
        self.data = data
        self.log = log
        self.testName = testName
        self.conn = get_connection()

    def setUp(self):
        self.startTime = time.time()
        self.data['limit'] =3

    def test_01_search_number(self):
        search_payload = {'country_iso': self.data['country_iso'],
                                        'type': self.data['type'],
                                        'services': self.data['services'],
                                        'pattern': self.data['pattern'],
                                        'limit': self.data['limit'],
                                        'offset': self.data['offset'],
                                    }
        self.log.info("Running %s", self.testName)
        (response_code, response_json)= self.conn.search_phone_numbers(
                                                                  search_payload)
        self.log.info("Actual Response code is %s and expected response code is 200",
                      response_code)
        assert str(response_code) == '200', ("Response code did not match"+
                                             str(response_code))
        self.log.info("Response json is %s", response_json)
        assert len(response_json['objects'] ) == 3, ("Limit Parameter not working "+
                                                     str(len(response_json['objects'] )))

    def test_02_search_number(self):
        search_payload = {'country_iso': self.data['country_iso'],
                                            'type': self.data['type'],
                                            'services': self.data['services'],
                                            'pattern': self.data['pattern'],
                                            'limit': self.data['limit'],
                                            'offset': self.data['offset'],
                                        }
        self.log.info("Running %s", self.testName)
        (response_code, response_json) = self.conn.search_phone_numbers(search_payload)
        assert str(response_code) == '200', ("Response code did not match"+str(response_code))
        self.log.info("Actual Response code is %s and expected response code is 200", response_code)
        expected_pattern = country_codes[self.data['country_iso']]+str(self.data['pattern'])
        for elem in response_json['objects']:
            self.assertTrue(
                            str(elem['number']).startswith(expected_pattern),
                            ("Pattern did not match. Expected "+ expected_pattern +
                             " Actual Number "+
                             str(elem['number'])))
            self.log.info(
                          "Number selected is : %s, Number should start with : %s",
                          str(elem['number']),
                          expected_pattern )

