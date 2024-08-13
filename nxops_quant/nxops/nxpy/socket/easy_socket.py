# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-08-18 10:24:20
LastEditTime : 2021-08-18 10:24:20
LastEditors  : yi.mt
Description  : 
'''

import socket

class EasySocket:
    @staticmethod
    def send(host, port, data):
        send_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        send_socket.connect((host, port))
        send_socket.sendall(data)
        send_socket.close()