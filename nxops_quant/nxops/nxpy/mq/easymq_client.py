# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-11-25 11:26:03
LastEditTime : 2021-12-24 11:38:58
LastEditors  : yi.mt
Description  : 
'''

from abc import abstractmethod
import zmq
import time
import random

import struct

import threading

EASYMQ_CHARSET_GB18030 = 0
EASYMQ_CHARSET_UTF8 = 1


def bytes_to_hex(buff):
    buff_array = ["{:02x}".format(i) for i in buff]
    result = ''.join(buff_array)
    return result


def int_to_bytes(i):
    result = bytearray(struct.pack("<I", i))
    return result
    

def bytes_to_int(buff):
    result = struct.unpack("<I", buff)[0]
    return result


class EasyMQMsg(object):
    TAG_COMMON = "0"
    TAG_HA = "1"

    BIZ_COMMON = "0000000"

    TOPIC_SIZE = 64

    def __init__(self, tag, biz, charset=EASYMQ_CHARSET_UTF8):
        self.tag = tag
        self.biz = biz
        self.charset = charset

        self.topic = None
        self.content = None

        self.count = 0
        self.index = 0
        self.content_size = 0
        self.check_sum = 0

    def set_charset(self, charset):
        self.charset = charset

    def get_charset(self):
        return self.charset

    def set_topic(self, topic):
        self.topic = topic

    def get_topic(self):
        return self.topic

    def set_content(self, content):
        self.content = content
        if self.content:
            self.content_size = len(self.content)

    def get_content(self):
        return self.content

    def get_tag(self):
        return self.tag

    def get_content_size(self):
        return self.content_size

    def reset(self):
        self.tag = "\0"
        self.biz = None
        self.count = 0
        self.index = 0
        self.content_size = 0
        self.check_sum = 0
        self.topic = None
        self.content  =None

    def to_chunk(self):
        charset_name = "GB18030" if self.charset == EASYMQ_CHARSET_GB18030 else "UTF-8"

        buff = ""
        buff += bytes_to_hex(bytearray(self.tag, charset_name))
        buff += bytes_to_hex(bytearray(self.biz, charset_name))
        topic_bytes = bytearray(self.topic, charset_name)
        buff += bytes_to_hex(topic_bytes)
        if len(topic_bytes) < 64:
            fill_bytes = bytearray(64 - len(topic_bytes))
            buff += bytes_to_hex(fill_bytes)
        buff += bytes_to_hex(int_to_bytes(self.count))
        buff += bytes_to_hex(int_to_bytes(self.index))
        buff += bytes_to_hex(int_to_bytes(self.content_size))
        if self.content_size > 0:
            content_bytes = bytearray(self.content, charset_name)
            buff += bytes_to_hex(content_bytes)
        buff += bytes_to_hex(int_to_bytes(self.charset))
        buff += bytes_to_hex(int_to_bytes(self.check_sum))

        return bytearray.fromhex(buff)

    def from_chunk(self, buffer):
        index = 0
        tag_bytes = buffer[index:index + 1]
        self.tag = str(tag_bytes)
        index += 1
        biz_bytes = buffer[index:index + 7]
        self.biz = str(biz_bytes)
        index += 7
        topic_bytes = buffer[index:index + 64]
        index += 64
        int_bytes = buffer[index:index + 4]
        self.count = bytes_to_int(int_bytes)
        index += 4
        int_bytes = buffer[index:index + 4]
        self.index = bytes_to_int(int_bytes)
        index += 4
        int_bytes = buffer[index:index + 4]
        self.content_size = bytes_to_int(int_bytes)
        index += 4
        if self.content_size > 0:
            content_bytes = buffer[index:index + self.content_size]
            index += self.content_size
        int_bytes = buffer[index:index + 4]
        self.charset = bytes_to_int(int_bytes)

        charset_name = "GB18030" if self.charset == EASYMQ_CHARSET_GB18030 else "UTF-8"
        self.topic = topic_bytes.decode(charset_name).rstrip()
        if self.content_size > 0:
            self.content = content_bytes.decode(charset_name)

        index += 4
        int_bytes = buffer[index:index + 4]
        self.check_sum = bytes_to_int(int_bytes)


class HAEasyMQMsg(EasyMQMsg):
    def __init__(self):
        super(HAEasyMQMsg, self).__init__(EasyMQMsg.TAG_HA, EasyMQMsg.BIZ_COMMON)


class CommonEasyMQMsg(EasyMQMsg):
    def __init__(self, charset=EASYMQ_CHARSET_UTF8):
        super(CommonEasyMQMsg, self).__init__(EasyMQMsg.TAG_COMMON, EasyMQMsg.BIZ_COMMON)
    

class EasyMQClient:
    MODE_PUB_SUB = 0
    MODE_ONLY_PUB = 1
    MODE_ONLY_SUB = 2

    random = random.Random(time.time)

    def __init__(self, mode=MODE_PUB_SUB):
        self.mode = mode
        self.charset = EASYMQ_CHARSET_UTF8

        self.runtime = EasyMQClient.Runtime(self)
        self.runtime.inproc_address = "inproc://mq-{0}-{1}".format(int(self.random.random() * 1000000), int(self.random.random() * 10000))

    def init(self):
        self.runtime.context = zmq.Context()

        if self.mode != self.MODE_ONLY_SUB:
            pub_thread = threading.Thread(target=self.publish_d, args=())
            pub_thread.setDaemon(True)
            pub_thread.start()

        if self.mode != self.MODE_ONLY_PUB:
            sub_thread = threading.Thread(target=self.subscribe_d, args=())
            sub_thread.setDaemon(True)
            loop_thread = threading.Thread(target=self.loop_d, args=())
            loop_thread.setDaemon(True)
            sub_thread.start()
            loop_thread.start()

        while True:
            if self.runtime.status == 1 or self.mode == self.MODE_ONLY_PUB:
                break
            else:
                self.send_ha_msg()
                time.sleep(0.003)

    def set_pub_address(self, pub_address):
        self.runtime.pub_address = pub_address

    def set_sub_address(self, sub_address):
        self.runtime.sub_address = sub_address

    def set_charset(self, charset):
        self.charset = charset

    def get_charset(self):
        return self.charset

    def send_ha_msg(self):
        if self.runtime.pub_socket:
            msg = HAEasyMQMsg()
            msg.set_topic(self.runtime.inproc_address)
            self.runtime.pub_socket.send(msg.to_chunk())

    def publish(self, topic, content):
        result = False
        if self.runtime and self.runtime.pub_socket:
            msg = CommonEasyMQMsg(self.charset)
            msg.set_topic(topic)
            msg.set_content(content)

            result = self.runtime.pub_socket.send(msg.to_chunk())
        else:
            print("publish transport is not ready\n")
        return result

    def subscribe(self, topic, resolver):
        result = False
        if self.runtime and self.runtime.sub_socket:
                sub_topic = "{0}{1}{2}".format(EasyMQMsg.TAG_COMMON, EasyMQMsg.BIZ_COMMON, topic)
                self.runtime.sub_socket.subscribe(sub_topic)

                resolvers = self.runtime.resolvers.get(topic)
                if not resolvers:
                    resolvers = []
                    self.runtime.resolvers.update({topic: resolvers})
                if resolver not in resolvers:
                    resolvers.append(resolver)
        else:
            print("publish transport is not ready\n")

    def publish_d(self):
        self.runtime.pub_socket = self.runtime.context.socket(zmq.PUSH)
        self.runtime.pub_socket.connect(self.runtime.pub_address)

        while True:
            time.sleep(3600)
    
    def subscribe_d(self):
        self.runtime.sub_socket = self.runtime.context.socket(zmq.SUB)
        inproc_topic = "{0}{1}{2}".format(EasyMQMsg.TAG_HA, EasyMQMsg.BIZ_COMMON, self.runtime.inproc_address)
        self.runtime.sub_socket.subscribe(inproc_topic)

        self.runtime.sub_socket.connect(self.runtime.sub_address)

        #self.runtime.inproc_push_socket = self.runtime.context.socket(zmq.PUSH)
        #self.runtime.inproc_push_socket.connect(self.runtime.inproc_address)

        #zmq.proxy_steerable(self.runtime.sub_socket, self.runtime.inproc_push_socket, None)

        while True:
            time.sleep(3600)

    def loop_d(self):
        #self.runtime.inproc_pull_socket = self.runtime.context.socket(zmq.PULL)
        #self.runtime.inproc_pull_socket.connect(self.runtime.inproc_address)

        charset_name = "GB18030" if self.charset == EASYMQ_CHARSET_GB18030 else "UTF-8"
        ha_tag = bytearray(EasyMQMsg.TAG_HA, charset_name)[0]

        common_msg = CommonEasyMQMsg(self.charset)
        while True:
            buffer = self.runtime.sub_socket.recv()

            if len(buffer) > 0:
                buffer = bytearray(buffer)
                if buffer[0] == ha_tag:
                    self.runtime.status = 1
                else:
                    common_msg.reset()
                    common_msg.from_chunk(buffer)

                    resolvers = self.runtime.resolvers.get(common_msg.get_topic())
                    if resolvers:
                        for resolver in resolvers:
                            resolver.resolve(self.runtime, common_msg)


    class Runtime:
        def __init__(self, client):
            self.client = client
            self.status = 0
            self.pub_address = None
            self.sub_address = None
            self.inproc_address = None
            self.context = None
            self.pub_socket = None
            self.sub_socket = None
            self.inproc_push_socket = None
            self.inproc_pull_socket = None

            self.resolvers = dict()

class EasyMQMsgResolver:
    @abstractmethod
    def resolve(self, runtime, msg):
        pass

class EasyMQClientContext:
    clients = dict()

    @classmethod
    def get_easymq_client(clazz, charset, pub_address, sub_address):
        client_id = "{0}-{1}-{2}".format(charset, pub_address, sub_address)

        if client_id in clazz.clients:
            return clazz.clients.get(client_id)
        else:
            client = EasyMQClient()
            client.set_charset(charset)
            client.set_pub_address(pub_address)
            client.set_sub_address(sub_address)

            client.init()

            clazz.clients.update({client_id : client})

            return client
