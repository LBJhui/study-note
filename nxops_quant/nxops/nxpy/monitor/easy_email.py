# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2022-05-09 11:19:08
LastEditTime : 2022-09-23 18:06:30
LastEditors  : yi.mt
Description  : 
'''

import os
import base64
import rapidjson
import smtplib

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from nxpy.log.logger import LoggerUtils


class EasyEmail:
    def __init__(self, config):
        self.config = config
        self.smtp = None

    def __connect(self):
        try:
            smtp_config = self.config.get("smtp")
            smtp_host = smtp_config.get("host")
            smtp_port = smtp_config.get("port")
            timeout = smtp_config.get("timeout", 60)

            self.smtp = smtplib.SMTP_SSL(host=smtp_host, port=smtp_port, timeout=timeout)

            if self.smtp:
                self.smtp.login(self.config.get("account"), self.config.get("password"))

        except Exception as e:
            LoggerUtils.error(f"connect email error: [{e}]")

    def close(self):
        if self.smtp:
            self.smtp.quit()

    def send(self, receivers, cc_receivers=[], bcc_receivers=[], attaches=[], mime_type="plain", subject="", content=""):
        try:
            if not self.smtp:
                self.__connect()
                
            mail_data = MIMEMultipart()

            mail_data["Subject"] = Header(subject, charset="UTF-8").encode()
            mail_data["From"] = formataddr((str(Header(self.config.get("name", ""), "UTF-8")), self.config.get("account")))
            mail_data["To"] = ";".join(receivers)
            mail_data["Cc"] = ";".join(cc_receivers)
            mail_data["Bcc"] = ";".join(bcc_receivers)

            mail_data.attach(MIMEText(content, mime_type, "UTF-8"))

            for attach_file_path in attaches:
                attach_data = MIMEText(open(attach_file_path, 'rb').read(), 'base64', 'UTF-8')
                attach_data["Content-Type"] = 'application/octet-stream'
                file_name = os.path.basename(attach_file_path)
                file_name = '=?UTF-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                attach_data["Content-Disposition"] = 'attachment; filename=' + file_name
                mail_data.attach(attach_data)

            send_errs = self.smtp.sendmail(from_addr=self.config.get("account"), to_addrs=receivers + cc_receivers + bcc_receivers, msg=mail_data.as_string())
            if send_errs:
                LoggerUtils.error(f"send email error: [{send_errs}]")

        except Exception as e:
            LoggerUtils.error(f"send email error: [{e}]")
    

class EasyEmailUtils:
    emails = {}

    @staticmethod
    def load_emails(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (email_id, email_config) in config.items():
                EasyEmailUtils.emails.update({email_id: EasyEmail(email_config)})

    @staticmethod
    def get_email(email_id):
        return EasyEmailUtils.emails.get(email_id)