from masterTest import *
from utils.common_utils import *
from settings.config import *


class test_assignment(masterTest):
    def __init__(self, testName, data, log):
        super(test_assignment, self).__init__(testName)
        self.data = data
        self.log = log
        self.testName = testName
        self.conn = get_connection()

    def setUp(self):
        self.startTime = time.time()
        self.log.info("Running setup()")
        (self.src_num,self.dest_num) = search_buy_2num(self.data['country_iso'], self.data['type'],
                                      self.data['services'], self.data['pattern'], self.data['limit'], self.data['offset'], self.log)
        #self.src_num = '13308702638'
        #self.dest_num = '13308702036'

    def test_01_assignment(self):
        self.log.info("--- Running %s -----", self.testName)
        (before_response_code, before_response_json) = self.conn.get_account()
        before_credits = before_response_json['cash_credits']
        self.log.info(" Total number of credits  before sms is sent %s", before_credits)
        sms_payload = {
            'src': self.src_num,
            'dst' : self.dest_num,
            'text' : u"Am I recieved?",
        }
        (sms_response_code, sms_response_json) = self.conn.send_message(sms_payload)
        self.log.info("For sending SMS response_code is %s  and response_json is %s",
                        sms_response_code, sms_response_json)
        msg_payload = {'message_uuid' : sms_response_json['message_uuid'][0]
                                    }
        (msg_response_code, msg_response_json) = self.conn.get_message(msg_payload)
        self.log.info("For getting SMS details response_code is %s  and response_json is %s",
                        msg_response_code, msg_response_json)
        msg_price = float(msg_response_json['total_amount'])
        self.log.info("Price of the SMS as per get_message api is %s ", msg_price)

        pricing_payload = { 'country_iso' : self.data['country_iso'] }
        (pricing_reponse_code, pricing_response_json) = self.conn.pricing(pricing_payload)
        self.log.info("For getting pricing details api response_code is %s  and response_json is %s",
                        pricing_reponse_code, pricing_response_json)
        price_per_message = float(pricing_response_json['message']['outbound']['rate'])
        self.log.info("Price of the SMS as per Pricing api is %s ",
                        price_per_message)
        (after_response_code, after_response_json) = self.conn.get_account()
        after_credits = after_response_json['cash_credits']
        self.log.info(" Total number of credits  after sms is sent %s", after_credits)
        deducted_credits = float(before_credits) - float(after_credits)

        self.assertEqual(msg_price, price_per_message,
                        'Price as per get_message api is '+ str(msg_price)+
                        ' and as per pricing api is '+str(price_per_message)
                        )
        self.assertEqual(str(msg_price), str(deducted_credits),
                        'Price as per get_message api is '+ str(msg_price)+
                        ' and as per credit deducted from account is '+str(deducted_credits)
                        )





