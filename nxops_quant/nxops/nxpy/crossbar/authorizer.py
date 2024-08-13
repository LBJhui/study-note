# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-08-18 16:18:56
LastEditTime : 2020-08-19 14:49:23
LastEditors  : yi.mt
Description  : 
'''

import uuid
import types
import hashlib

from functools import wraps

from nxpy.context import AppContext
from nxpy.cache.easy_beaker import EasyCacheUtils

from twisted.internet.defer import _DefGen_Return, _cancellableInlineCallbacks
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession

ticket_cache_namespace = "ws"

def myInlineCallbacks(f):
    @wraps(f)
    def unwindGenerator(*args, **kwargs):
        try:
            gen = f(*args, **kwargs)
        except _DefGen_Return:
            raise TypeError(
                "inlineCallbacks requires %r to produce a generator; instead"
                "caught returnValue being used in a non-generator" % (f,))
        if not isinstance(gen, types.GeneratorType) and type(gen).__name__ != "generator":
            raise TypeError(
                "inlineCallbacks requires %r to produce a generator; "
                "instead got %r" % (f, gen))
        return _cancellableInlineCallbacks(gen)
    return unwindGenerator


class ServiceAuthorizer(ApplicationSession):

    @myInlineCallbacks
    def onJoin(self, details):
        self.log.info("ServiceAuthorizer.onJoin({})".format(details))
        
        EasyCacheUtils.load_settings(AppContext.get_config_path("cache.json"))

        try:
            procedure = "service.join.authorizer"
            yield self.register(self.service_join_authorize, procedure)
            self.log.info(f"ServiceAuthorizer: authorizer({procedure}) registered")

            procedure = "client.join.authorizer"
            yield self.register(self.client_join_authorize, procedure)
            self.log.info(f"ServiceAuthorizer: authorizer({procedure}) registered")
        except Exception as e:
            self.log.error("ServiceAuthorizer: failed to register authorizer procedure ({})".format(e))
            raise

    def service_join_authorize(self, realm, authid, details):
        ticket = details["ticket"]
        right_ticket = hashlib.md5(bytes(authid, encoding="UTF-8")).hexdigest()

        role = ""
        if right_ticket == ticket:
            role = "service"
        
        self.log.info("ServiceAuthorizer authorize: (authid='{}', realm='{}', ticket='{}', role='{}')".format(authid, realm, ticket, role))

        return {"role": role}

    def client_join_authorize(self, realm, authid, details):
        ticket = details["ticket"]

        ticket_cache = EasyCacheUtils.get_cache(ticket_cache_namespace)
        session_id = None
        if ticket_cache.has_key(ticket):
            session_id = ticket_cache.get_value(ticket)
            ticket_cache.remove_value(ticket)

        role = ""
        new_authid = ""
        if session_id:
            role = "client"
            new_authid = session_id + "-" + uuid.uuid4().hex[12:20]
        
        self.log.info("ServiceAuthorizer authorize: (authid='{}', realm='{}', ticket='{}', id='{}', role='{}')".format(authid, realm, ticket, new_authid, role))

        return {"authid": new_authid, "role": role}

