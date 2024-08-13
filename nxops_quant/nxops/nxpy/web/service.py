# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-10 17:42:30
@LastEditTime : 2020-08-13 17:01:27
@LastEditors  : yi.mt
@Description  : 
'''
import platform

import asyncio

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from abc import ABC, abstractmethod

import tornado.httpserver
import tornado.netutil

import nxpy.web.constants

from nxpy.os.path import PathUtils
from nxpy.context import AppContext

from nxpy.tornado.handlers import NotFoundServiceHandler

from web.management import ManagementHandler


class WebService():
    def __init__(self):
        super().__init__()

        self.server_settings = {"port": 8080}

    def mount(self, *args, **kwargs):
        pass

    def build(self, *args, **kwargs):
        handlers = []
        if "management" in self.server_settings:
            management_settings = self.server_settings.get("management")
            handlers.append((r"/mx/(?P<version>.*)/(?P<manager>.*)/(?P<cmd>.*)", ManagementHandler, {"hosts": {management_settings.get("host", None)}, "ports": {management_settings.get("port")}}))

        handlers = handlers + self.load_handlers(*args, **kwargs)

        handlers.append((r".*", NotFoundServiceHandler))

        application = tornado.web.Application(
            handlers=handlers,
            cookie_secret=nxpy.web.constants.CONST_COOKIE_SECRET,
        )

        return application

    def loop(self, application, *args, **kwargs):
        server = tornado.httpserver.HTTPServer(application, xheaders=True)

        web_sockets = tornado.netutil.bind_sockets(self.server_settings.get("port"))
        server.add_sockets(web_sockets)

        if "management" in self.server_settings:
            management_settings = self.server_settings.get("management")
            manage_sockets = tornado.netutil.bind_sockets(port=management_settings.get("port"), address=management_settings.get("host", None))
            server.add_sockets(manage_sockets)

        tornado.ioloop.IOLoop.current().start()

    def start(self, *args, **kwargs):
        application = self.build(*args, **kwargs)
        if application:
            self.loop(application, *args, **kwargs)

    @abstractmethod
    def load_handlers(self, *args, **kwargs):
        return []
