# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:21
# @Author: LBJ辉
# @File: easy_monitor
# @Project: python
import os
import time
import datetime
import json
import rapidjson
import shutil
import traceback

import socket
import select
import threading

from collections import deque

import warnings

warnings.filterwarnings("ignore")

from nxpy.context import AppContext
from nxpy.os.path import PathUtils
from nxpy.log.logger import LoggerUtils
from nxpy.monitor.easy_sms import EasySMSUtils
from nxpy.monitor.easy_email import EasyEmailUtils
from nxpy.socket.easy_socket import EasySocket


class EasyMonitorDaemon:
    def __init__(self, config_file):
        config_file_path = AppContext.get_config_path(config_file)
        with open(config_file_path, encoding="UTF-8") as pf:
            self.monitor_config = rapidjson.load(pf)

    def start_server(self, server_config):
        server_port = server_config.get("port", 42020)
        data_home = server_config.get("data_home")
        data_home = PathUtils.get_real_path(data_home)
        todo_data_home = os.path.join(data_home, "todo")

        LoggerUtils.info(f"[EasyMonitorDaemon] [Server({server_port})] starting")

        listen_sock = socket.socket()
        listen_sock.setblocking(False)
        listen_sock.bind(("0.0.0.0", server_port,))
        listen_sock.listen(10)

        read_list = deque([listen_sock])
        write_list = deque()
        error_list = deque()

        while True:
            try:
                r_list, w_list, e_list = select.select(read_list, write_list, error_list)

                for sock in r_list:
                    if sock == listen_sock:
                        conn, addr = listen_sock.accept()
                        LoggerUtils.info(f"[EasyMonitorDaemon] [Server({server_port})] accept connection from [{addr}]")
                        conn.setblocking(False)
                        read_list.append(conn)
                    else:
                        result_msg = "{\"code\":0}"
                        try:
                            data = sock.recv(1024 * 1024 * 16)
                            if len(data) > 0:
                                try:
                                    data = str(data)
                                    data_json = rapidjson.loads(eval(data.replace("\n", "")))
                                except Exception as e:
                                    LoggerUtils.warning(f"[EasyMonitorDaemon] [Server({server_port})] accept data from [{addr}] error [UTF-8][{e}]: --{data}--")
                                    try:
                                        data = str(data, encoding="GB18030")
                                        data_json = rapidjson.loads(eval(data.replace("\n", "")))
                                    except Exception as ie:
                                        result_msg = "{\"code\":-1}"
                                        LoggerUtils.error(f"[EasyMonitorDaemon] [Server({server_port})] accept data from [{addr}] error [GB18030][{ie}]: --{data}--")
                                        continue

                                sys_module = data_json.get("SysModule")
                                monitor_data = data_json.get("MonitorData")
                                data_file_name = sys_module + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                                write_file_path = os.path.join(todo_data_home, data_file_name + ".mdw")
                                with open(write_file_path, mode="w", encoding="UTF-8") as f:
                                    f.write(rapidjson.dumps(monitor_data))
                                monitor_file_path = os.path.join(todo_data_home, data_file_name + ".mtr")
                                shutil.move(write_file_path, monitor_file_path)
                                LoggerUtils.info(f"[EasyMonitorDaemon] [Server({server_port})] dumped file [{monitor_file_path}]")
                        except Exception as e:
                            LoggerUtils.error(f"[EasyMonitorDaemon] [Server({server_port})] error: [{e}]")
                            result_msg = "{\"code\":-2}"
                        finally:
                            sock.sendall(bytes(result_msg, encoding="UTF-8"))
                            sock.close()
                            read_list.remove(sock)

                for sock in e_list:
                    sock.close()
                    read_list.remove(sock)

                time.sleep(0.005)
            except Exception as e:
                LoggerUtils.error(f"[EasyMonitorDaemon] [Server({server_port})] error: [{e}]")
                traceback.print_exc()

    def start_daemon(self):
        LoggerUtils.info(f"[EasyMonitorDaemon] starting")

        servers = self.monitor_config.get("servers")
        for server_config in servers:
            th = threading.Thread(target=self.start_server, args=(server_config,))
            th.start()

        monitors = self.monitor_config.get("monitors")
        while True:
            try:
                for monitor_config in monitors:
                    sms_id = monitor_config.get("sms")
                    easy_sms = EasySMSUtils.get_sms(sms_id)

                    default_mobiles = monitor_config.get("mobiles")
                    data_home = monitor_config.get("data_home")
                    data_home = PathUtils.get_real_path(data_home)
                    todo_data_home = os.path.join(data_home, "todo")
                    done_data_home = os.path.join(data_home, "done")
                    miss_data_home = os.path.join(data_home, "miss")

                    monitor_files = os.listdir(todo_data_home)
                    monitor_files.sort()

                    for monitor_file in monitor_files:
                        if monitor_file[-4:] == ".mtr":
                            try:
                                monitor_file_path = os.path.join(todo_data_home, monitor_file)
                                backup_path = os.path.join(done_data_home, monitor_file)
                                if not os.path.exists(backup_path):
                                    shutil.copy(monitor_file_path, backup_path)
                                    LoggerUtils.info(f"[EasyMonitorDaemon] processing [{monitor_file_path}]")

                                all_processed = True
                                monitor_infos = None
                                with open(monitor_file_path, encoding="UTF-8") as f:
                                    monitor_infos = rapidjson.load(f)
                                    monitor_infos = [monitor_infos] if isinstance(monitor_infos, dict) else monitor_infos
                                    for monitor_info in monitor_infos:
                                        mobiles = monitor_info.get("Mobiles")
                                        title = monitor_info.get("Title")
                                        content = monitor_info.get("Content")

                                        process_time = monitor_info.get("ProcessTime")
                                        post_time = monitor_info.get("PostTime")
                                        current_time = datetime.datetime.now().strftime("%H:%M")
                                        if process_time is None:
                                            if post_time is None or post_time == "" or current_time == post_time:
                                                notify_mobiles = mobiles if mobiles is not None else default_mobiles
                                                notify_mobiles = [notify_mobiles] if isinstance(notify_mobiles, str) else notify_mobiles
                                                sended_count = 0
                                                mobiles_count = len(notify_mobiles)
                                                sms_content = "%s" % (content,) if title is None or len(title) == 0 else "[%s]%s" % (title, content)
                                                while sended_count < mobiles_count:
                                                    if mobiles_count - sended_count > 500:
                                                        sub_mobiles = notify_mobiles[sended_count:sended_count + 500]
                                                        sub_mobiles = [str(item) for item in sub_mobiles]
                                                        sended_count += 500
                                                        sms_mobiles = ",".join(sub_mobiles)
                                                        easy_sms.send(sms_mobiles, sms_content)
                                                        time.sleep(5)
                                                    else:
                                                        sub_mobiles = notify_mobiles[sended_count:mobiles_count]
                                                        sub_mobiles = [str(item) for item in sub_mobiles]
                                                        sended_count = mobiles_count
                                                        sms_mobiles = ",".join(sub_mobiles)
                                                        easy_sms.send(sms_mobiles, sms_content)
                                                monitor_info.update({"ProcessTime": datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")})
                                            else:
                                                all_processed = False
                                with open(monitor_file_path, mode="w", encoding="UTF-8") as f:
                                    f.write(rapidjson.dumps(monitor_infos))

                                if all_processed:
                                    prc_path = os.path.join(done_data_home, monitor_file + ".prc")
                                    shutil.move(monitor_file_path, prc_path)
                                    LoggerUtils.info(f"[EasyMonitorDaemon] processed [{monitor_file_path}]")
                            except Exception as e:
                                LoggerUtils.info(f"[EasyMonitorDaemon] process [{monitor_file_path}] error: [{e}]")
                                miss_path = os.path.join(miss_data_home, monitor_file)
                                if not os.path.exists(miss_path):
                                    shutil.move(monitor_file_path, miss_path)
                                    LoggerUtils.info(f"[EasyMonitorDaemon] missed [{monitor_file_path}] to [{miss_path}]")
            except Exception as e:
                LoggerUtils.info(f"[EasyMonitorDaemon] error: [{e}]")
                traceback.print_exc()
            finally:
                time.sleep(5)


class EasyMonitor:
    def __init__(self, config):
        self.config = config

    def report(self, module, title, content):
        pass


class EasyFileMonitor(EasyMonitor):
    def __init__(self, config):
        super().__init__(config)

        data_home = self.config.get("data_home")
        self.todo_data_home = PathUtils.get_real_path(data_home)

        LoggerUtils.info(f"[EasyFileMonitor] init [{self.todo_data_home}]")

    def report(self, module, title, content):
        mobiles = self.config.get("mobiles", [])

        monitor_data = [{"Title": title, "Content": content, "Mobiles": mobiles}]
        data_file_name = module + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        write_file_path = os.path.join(self.todo_data_home, data_file_name + ".mdw")
        with open(write_file_path, "w", encoding="UTF-8") as f:
            f.write(rapidjson.dumps(monitor_data))
        monitor_file_path = os.path.join(self.todo_data_home, data_file_name + ".mtr")
        shutil.move(write_file_path, monitor_file_path)


class EasyNetMonitor(EasyMonitor):
    def __init__(self, config):
        super().__init__(config)

        self.monitor_host = self.config.get("host")
        self.monitor_port = self.config.get("port", 42020)

        LoggerUtils.info(f"[EasyNetMonitor] init [{self.monitor_host}:self.monitor_port]")

    def report(self, module, title, content):
        mobiles = self.config.get("mobiles", [])

        monitor_data = [{"Title": title, "Content": content, "Mobiles": mobiles}]
        socket_data = {"SysModule": module, "MonitorData": monitor_data}

        EasySocket.send(self.monitor_host, self.monitor_port, socket_data)


class EasyEmailMonitor(EasyMonitor):
    def __init__(self, config):
        super().__init__(config)

        email_id = self.config.get("email")
        LoggerUtils.info(f"[EasyEmailMonitor] init [{email_id}]")

        self.email = EasyEmailUtils.get_email(email_id)

    def report(self, module, title, content):
        receivers = self.config.get("receivers", [])
        cc_receivers = self.config.get("cc_receivers", [])
        bcc_receivers = self.config.get("bcc_receivers", [])

        self.email.send(receivers=receivers, cc_receivers=cc_receivers, bcc_receivers=bcc_receivers, subject=f"[{module}]{title}", content=content)


class EasyMonitorUtils:
    @staticmethod
    def create_monitor(config):
        type = config.get("type")
        if type:
            if type == "file":
                return EasyFileMonitor(config)
            elif type == "net":
                return EasyNetMonitor(config)
            elif type == "email":
                return EasyEmailMonitor(config)

        return None
