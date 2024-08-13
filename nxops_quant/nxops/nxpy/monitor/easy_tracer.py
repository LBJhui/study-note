# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2022-05-13 10:36:07
LastEditTime : 2022-07-12 10:33:34
LastEditors  : yi.mt
Description  : 
'''

import time

from nxpy.monitor.easy_monitor import EasyMonitor, EasyMonitorUtils


class EasyTracer(EasyMonitor):
    def __init__(self, config):
        self.config = config
        self.traces = []
        self.monitor = EasyMonitorUtils.create_monitor(config)

    def report(self, module, title, content):
        info = f"{title}: {content}"
        self.trace(info)

    def trace(self, info):
        trace_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.traces.append(dict(ts=trace_time, info=info))

    def commit(self, kwargs):
        content = "\n".join([f"{trace['ts']} {trace['info']}" for trace in self.traces])
        self.monitor.report(self.config.get("module", "tracer"), self.config.get("title", "report"), content)


class EasyTracerUtils:
    @staticmethod
    def create_tracer(config):
        return EasyTracer(config)
        