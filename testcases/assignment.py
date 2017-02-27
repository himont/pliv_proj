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


    def test_01_assignment(self):
        self.log.info("--- Running %s -----", self.testName)
        before_credits = get_account_credits(self.log)
        self.log.info(" Total number of credits  before sms is sent %s", before_credits)
        message_uuid = send_sms(self.src_num, self.dest_num, "test text", self.log)
        msg_price = get_msg_price(message_uuid, self.log)
        self.log.info("Price of the SMS as per get_message api is %s ", msg_price)
        price_per_message = country_msg_pricing(self.data['country_iso'], self.log)
        self.log.info("Price of the SMS as per Pricing api is %s ",
                        price_per_message)
        after_credits = get_account_credits(self.log)
        self.log.info(" Total number of credits  after sms is sent %s", after_credits)
        deducted_credits = before_credits - after_credits
        self.log.info(" Total number of credits deducted from the account %s", deducted_credits)

        self.assertEqual(msg_price, price_per_message,
                        'Price as per get_message api is '+ str(msg_price)+
                        ' and as per pricing api is '+str(price_per_message)
                        )
        self.assertEqual(str(msg_price), str(deducted_credits),
                        'Price as per get_message api is '+ str(msg_price)+
                        ' and as per credit deducted from account is '+str(deducted_credits)
                        )

    def tearDown(self):
        unrent_num(self.src_num,self.log)
        unrent_num(self.dest_num,self.log)





