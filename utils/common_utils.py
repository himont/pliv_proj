import plivo
from settings.config import *
from utils.logger import *


def get_connection():
    return plivo.RestAPI(auth_id, auth_token)

def get_account_credits(log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        conn = get_connection()
        (response_code, response_json) = conn.get_account()
        log.info("For get_account() api response_code is %s and response_json is %s ",
                        response_code, response_json)
        credits = response_json['cash_credits']
        return float(credits)
    except Exception as e:
        log.error("Exception occured while getting account detail \n"+str(e))

def send_sms(src_num, dest_num, text, log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        conn = get_connection()
        sms_payload = {
                'src': src_num,
                'dst' : dest_num,
                'text' : text,
            }
        (response_code, response_json) = conn.send_message(sms_payload)
        log.info("For send_message api response_code is %s and response_json is %s ",
                            response_code, response_json)
        return response_json['message_uuid'][0]
    except Exception as e:
        log.error("Exception occured while sending SMS \n"+str(e))

def get_msg_price(message_uuid, log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        conn = get_connection()
        payload = {'message_uuid' : message_uuid }
        (response_code, response_json) = conn.get_message(payload)
        log.info("For get_message api response_code is %s and response_json is %s ",
                            response_code, response_json)
        return float(response_json['total_amount'])
    except Exception as e:
        log.error("Exception occured while getting message detail \n"+str(e))

def country_msg_pricing(country_iso,log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        conn = get_connection()
        payload = { 'country_iso' : country_iso }
        (response_code, response_json) = conn.pricing(payload)
        log.info("For pricing api response_code is %s and response_json is %s ",
                            response_code, response_json)
        return float(response_json['message']['outbound']['rate'])
    except Exception as e:
        log.error("Exception occured while getting country pricing details for messagel \n"+str(e))

def unrent_num(number, log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        payload = {'number' : number}
        conn = get_connection()
        response_code= conn.unrent_number(payload)
        log.info("For unrenting a number response_code is %s ",
                        response_code)
    except Exception as e:
        log.error("Exception occured while unrenting a number \n"+str(e))


def search_number(country_iso = 'US', num_type='Any', services='voice,sms',
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
        log.info("For searching numbers response_code is %s ",
                        response_code)
        log.info("For searching numbers response_json is %s ",
                        response_json)
        return (response_code, response_json['objects'] )
    except Exception as e:
        log.error("Exception occured while searching numbers \n"+str(e))


def search_buy_2num(country_iso = 'US', num_type='Any', services='voice,sms',
                    pattern=None, limit = 2, offset = 0,log=None):
    try:
        if not log:
            log = logger_class.create_logger()
        (response_code, number_object_list) = search_number(country_iso, num_type,
                                    services, pattern, limit, offset, log)

        buy_payload_0 = {'number' : number_object_list[0]['number'],
                                        }
        buy_payload_1 = {'number' : number_object_list[1]['number'],
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

