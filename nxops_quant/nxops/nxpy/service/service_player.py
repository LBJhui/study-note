# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-12-24 11:26:08
LastEditTime : 2022-02-22 15:12:20
LastEditors  : yi.mt
Description  : 
'''

import traceback
import threading
from nxpy.config.easy_config import EasyConfig

from nxpy.log.logger import LoggerUtils
from nxpy.monitor.easy_monitor import EasyMonitorUtils


class EasyMatterThread(threading.Thread):
    def __init__(self, id, group=None, target=None, name=None, callback=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.id = id
        self.result = False
        self.callback = callback
    
    def run(self):
        try:
            if self._target:
                self.result = self._target(*self._args, **self._kwargs)
            else:
                self.result = None

            if self.callback:
                self.callback(*self._args, **self._kwargs)
        except Exception as e:
            LoggerUtils.error(f"matter error: {e}")
            traceback.print_exc()
        finally:
            del self._target, self._args, self._kwargs

    def get_result(self):
        return self.result


class ServicePlayer:
    def __init__(self, options={}, config=None):
        self.options = options
        self.config = config
        if self.config:
            self.options.update(EasyConfig.load(self.config))

        self.matters = []

        self.service_id = self.options.get("service_id")

    def _set_monitors(self):
        self.monitors = []
        monitors_config = self.options.get("monitors")
        if monitors_config:
            for monitor_config in monitors_config:
                monitor = EasyMonitorUtils.create_monitor(monitor_config)
                if monitor:
                    self.monitors.append(monitor)

    def report(self, module, title, content):
        for monitor in self.monitors:
            monitor.report(module, title, content)

    def info(self, content):
        msg = content
        if self.service_id:
            msg = f"{self.service_id} {content}"
        
        LoggerUtils.info(msg)

    def error(self, content):
        msg = content
        if self.service_id:
            msg = f"{self.service_id} {content}"
        
        LoggerUtils.error(msg)

    def warning(self, content):
        msg = content
        if self.service_id:
            msg = f"{self.service_id} {content}"
        
        LoggerUtils.warning(msg)

    def debug(self, content):
        msg = content
        if self.service_id:
            msg = f"{self.service_id} {content}"
        
        LoggerUtils.debug(msg)

    def log(self, content):
        msg = content
        if self.service_id:
            msg = f"{self.service_id} {content}"
        
        LoggerUtils.log(msg)

    def fork_matter(self, id, target, options, callback=None):
        matter = EasyMatterThread(id=id, target=target, callback=callback, args=(options,), daemon=True)
        self.matters.append(matter)
        matter.start()

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass