import plivo
from settings.config import *
from utils.logger import *


def get_connection():
    return plivo.RestAPI(auth_id, auth_token)

def search_buy_2num(country_iso = 'US', num_type='Any', services='voice,sms',
                    pattern=None, limit = 2, offset = 0,log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        search_payload = {'country_iso': country_iso,
                                        'type': num_type,
                                        'services': services,
                                        'pattern': pattern,
                                        'limit': limit,
                                        'offset': offset,
                                    }
        conn = get_connection()
        (response_code, response_json)= conn.search_phone_numbers(
                                                                  search_payload)
        log.info("For searching 2 numbers response_code is %s ",
                        response_code)
        log.info("For searching 2 numbers response_json is %s ",
                        response_json)
        buy_payload_0 = {'number' : response_json['objects'] [0]['number'],
                                        }
        buy_payload_1 = {'number' : response_json['objects'] [1]['number'],
                                        }
        log.info("Two selected numbers are %s and %s ",
                        response_json['objects'] [0]['number'],
                        response_json['objects'] [1]['number'])
        (buying_response_code_0, buying_response_json_0) = conn.buy_phone_number(buy_payload_0)
        (buying_response_code_1, buying_response_json_1) = conn.buy_phone_number(buy_payload_1)
        log.info("For buying 2 numbers response_code are %s and %s",
                        buying_response_code_0, buying_response_code_1)
        log.info("For buying 2 numbers response_json are %s and %s",
                        buying_response_json_0, buying_response_json_1)
        src_num = response_json['objects'] [0]['number']
        dest_num = response_json['objects'] [1]['number']
        return (src_num, dest_num)
    except Exception as e:
        log.error("Exception occured while searching and buying 2 numbers \n"+str(e))

