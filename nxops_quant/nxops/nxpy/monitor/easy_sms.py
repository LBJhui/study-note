# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-08-17 16:01:04
LastEditTime : 2021-08-17 16:01:04
LastEditors  : yi.mt
Description  : 
'''

import rapidjson
import requests
import time

from nxpy.log.logger import LoggerUtils

class EasySMS:
    def __init__(self, config):
        self.config = config

    def send(self, mobile, message):
        server_config = self.config.get("server")
        auth_config = self.config.get("auth")
        retry_config = self.config.get("retry")

        server_url = server_config.get("url")
        server_host = server_config.get("host")
        server_port = server_config.get("port")
        server_timeout = server_config.get("timeout")

        auth_user_id = auth_config.get("user_id")
        auth_password = auth_config.get("password")

        soap_message = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance 
                " xmlns:xsd="http://www.w3.org/2001/XMLSchema 
                " xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/ 
                ">
                  <soap:Body>
                    <MongateCsSpSendSmsNew xmlns="http://tempuri.org/">
                         <userId>{auth_user_id}</userId>
                         <password>{auth_password}</password>
                         <pszMobis>{mobile}</pszMobis>
                         <pszMsg>{message}</pszMsg>
                         <iMobiCount>1</iMobiCount>
                         <pszSubPort>*</pszSubPort>
                    </MongateCsSpSendSmsNew>
                  </soap:Body>
                </soap:Envelope>"""
        soap_message = soap_message.encode("UTF-8")

        http_headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
                        "Content-type": "text/xml; charset=\"UTF-8\"",
                        "Accept": "text/xml",
                        "Content-Length": "%d" % len(soap_message),
                        "Host": f"{server_host}:{server_port}"
                        }
        
        req_times = 0
        while True:
            req_times += 1
            resp = requests.post(url=server_url, data=soap_message, headers=http_headers, timeout=server_timeout)
            req_times
            if resp.status_code != 200 and retry_config:
                max_times = retry_config.get("max_times", 2)
                interval = retry_config.get("interval", 30)
                if max_times > req_times:
                    time.sleep(interval)
                    continue
            break
    
class EasySMSUtils:
    smses = {}

    @staticmethod
    def load_smses(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (sms_id, sms_config) in config.items():
                EasySMSUtils.smses.update({sms_id: EasySMS(sms_config)})

    @staticmethod
    def get_sms(sms_id):
        return EasySMSUtils.smses.get(sms_id)