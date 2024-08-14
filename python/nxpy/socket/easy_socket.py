# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:24
# @Author: LBJ辉
# @File: easy_socket
# @Project: python
import socket


class EasySocket:
    @staticmethod
    def send(host, port, data):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_socket.connect((host, port))
        send_socket.sendall(data)
        send_socket.close()
