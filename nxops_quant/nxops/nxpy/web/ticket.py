# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author         : yi.mt
Date           : 2020-08-19 10:51:08
LastEditTime   : 2020-08-19 18:10:35
LastEditors    : yi.mt
Description    : 
'''


import uuid

import nxpy.tornado.handlers

from nxpy.log.logger import LoggerUtils

from nxpy.security.cipher import EasyCipherUtils

from nxpy.cache.easy_beaker import EasyCacheUtils

ticket_goals = {"ws": {"expire": 6000000}}


class TicketServiceHandler(nxpy.tornado.handlers.AsyncServiceHandler):
    def _generate_ticket(self):
        return uuid.uuid4().hex

    def do_service(self, *args, **kwargs):
        goal = kwargs.get("goal")
        if goal not in ticket_goals:
            return False

        settings = ticket_goals.get(goal)

        client_ticket = self.parameters.get("ticket")
        server_ticket = client_ticket + ":" + self._generate_ticket()

        print(server_ticket)
        encrypted_ticket = EasyCipherUtils.symmetric_encrypt(server_ticket, client_ticket)
        
        session_id = self.get_session().id
        
        EasyCacheUtils.get_cache(goal, **settings).set_value(server_ticket, session_id)
        self.response.update({"content": encrypted_ticket})

        return True