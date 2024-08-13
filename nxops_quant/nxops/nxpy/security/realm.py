# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-03 15:43:19
@LastEditTime : 2020-08-14 13:43:44
@LastEditors  : yi.mt
@Description  : 
'''

import json
import zlib
import uuid

from abc import ABC, abstractmethod

from contextlib import contextmanager

from nxpy.context import AppRuntime
from nxpy.log.logger import LoggerUtils

from nxpy.pmx.management import Managable, Manager, ManagementGateway

AUTH_LEVEL_GUEST = 0

AUTH_LEVEL_PLAIN_USER = 100


@contextmanager
def bind_temporary_realm(*args, **kwargs):
    temporary_realms = AppRuntime.get_value("temporary_realms")
    if not temporary_realms:
        temporary_realms = []
        AppRuntime.set_value("temporary_realms", temporary_realms)
    
    temporary_realm = SecurityRealm(*args, **kwargs)
    temporary_realms.append(temporary_realm)
    try:
        yield
    finally:
        temporary_realms.remove(temporary_realm)
        if not temporary_realm:
            AppRuntime.del_value("temporary_realms")


class SecurityRealm():
    security_attr_names = ["auth_id", "auth_level", "auth_token", "roles"]

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._security_attrs_ = {
            "auth_id": None,
            "auth_level": AUTH_LEVEL_GUEST,
            "auth_token": None,
            "roles": set()
        }

        self.update(*args, **kwargs)

    def defined(self):
        return self.auth_id or self.auth_level or self.auth_token or self.roles

    def __setattr__(self, key, value):
        if key in self.security_attr_names:
            if key == "roles" and isinstance(value, list):
                value = set(value)
            self._security_attrs_[key] = value
        else:
            super().__setattr__(key, value)

    def __getattr__(self, key):
        if key in self.security_attr_names:
            return self._security_attrs_.get(key, None)
        else:
            return super().__getattr__(key)

    def __delattr__(self, key):
        if key in self.security_attr_names:
            return self._security_attrs_.pop(key, None)
        else:
            return super().__delattr__(key)

    def update(self, *args, **kwargs):
        attrs = kwargs.copy()

        role = attrs.pop("role", None)
        roles = attrs.get("roles", None)
        if roles and isinstance(roles, list):
            roles = set(roles)
            attrs.update({"roles": roles})

        self._security_attrs_.update(attrs)

        if role:
            roles = self.roles
            if roles is None:
                roles = self.roles = set()
            roles.add(role)
            

class Securable():
    def __init__(self, secure_id=uuid.uuid4().hex):
        super().__init__()

        self.secure_id = secure_id
        self.realm = None

    def __del__(self):
        SecurableZones.instance().remove(self)

    def bind_rules(self, *args, **kwargs):
        SecurableZones.instance().bind(self)

    def is_accessable(self, *args, **kwargs):
        temporary_realms = AppRuntime.get_value("temporary_realms")

        accessable = False
        if not self.realm or not self.realm.defined():
            accessable = True
        elif temporary_realms:
            for realm in temporary_realms:
                accessable = self._check_realm(realm)
                if accessable:
                    break
                
        if not accessable:
            context_realm = AppRuntime.get_value("realm")
            accessable = self._check_realm(context_realm)
        
        return accessable
        

    def _check_realm(self, realm):
        if not self.realm or (not self.realm.auth_id and not self.realm.auth_token and not self.realm.roles and not self.realm.auth_level):
            return True
        elif realm:
            accessable = True
            if accessable and self.realm.auth_id:
                accessable = self.realm.auth_id == realm.auth_id
            if accessable and self.realm.auth_token:
                accessable = self.realm.auth_token == realm.auth_token
            if accessable and self.realm.roles:
                accessable = len(self.realm.roles & realm.roles) > 0
            if accessable and self.realm.auth_level:
                accessable = realm.auth_level >= self.realm.auth_level
            return accessable
        return False


class ManagedSecurable(Managable):
    def __init__(self, secure=None):
        super().__init__()

        self.secure_id = secure.secure_id
        self.secure = secure
        self.owners = []

    def get(self):
        return self.secure

    def set(self, secure):
        self.secure = secure

    def on_manage(self, *args, **kwargs):
        return True


class SecurableZones(Manager):
    _instance = None

    def __init__(self):
        super().__init__()
        self.secures = {}
        self.zones = {
            "auth_id": {},
            "auth_token": {},
            "auth_level": {},
            "roles": {},
        }

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = SecurableZones()
            ManagementGateway.register_manager("security", cls._instance)
        return cls._instance

    def manage(self, *args, **kwargs):
        cmd = kwargs.get("cmd")
        if cmd == "flush":
            self.flush(*args, **kwargs)
        return True

    def bind(self, secure, *args, **kwargs):
        secure_id = secure.secure_id

        if secure_id in self.secures:
            managed_secure = self.secures.get(secure_id)
            if managed_secure.secure != secure:
                LoggerUtils.warning(f"securable object [{secure_id}] has been managed")

        managed_secure = ManagedSecurable(secure)
        self.secures.update({secure_id: managed_secure})
        self._bind_by_realm(managed_secure, *args, **kwargs)

    def remove(self, secure, *args, **kwargs):
        secure_id = secure.secure_id
        managed_secure = self.secures.get(secure_id, None)
        if managed_secure:
            for owner in managed_secure.owners:
                owner.pop(secure_id, None)
            self.secures.pop(secure_id, None)
            managed_secure.secure = None
            managed_secure.owners = None


    def flush(self, realm_type, realm_value, secure_ids, *args, **kwargs):
        realm_zones = self.zones.get(realm_type)
        the_zone = realm_zones.get(realm_value, {})
        for secure_id, managed_secure in the_zone.items():
            if secure_id not in secure_ids:
                managed_realm_value = getattr(managed_secure.secure.realm, realm_type)
                if (isinstance(managed_realm_value, set) or isinstance(managed_realm_value, list)):
                    if realm_value in managed_realm_value:
                        managed_realm_value.remove(realm_value)
                else:
                    setattr(managed_secure.secure.realm, realm_type, None)
            managed_secure.owners.remove(the_zone)
        the_zone.clear()
        realm_zones.update({realm_value: the_zone})

        for secure_id in secure_ids:
            managed_secure = self.secures.get(secure_id, None)
            if managed_secure:
                secure = managed_secure.secure
                if not secure.realm:
                    secure.realm = SecurityRealm()
                managed_realm_value = getattr(secure.realm, realm_type)
                if isinstance(managed_realm_value, set):
                    managed_realm_value.add(realm_value)
                elif isinstance(managed_realm_value, list) and realm_value not in managed_realm_value:
                    managed_realm_value.append(realm_value)
                else:
                    setattr(secure.realm, realm_type, realm_value)

                self._bind_by_realm(managed_secure)

    def _bind_by_realm(self, managed_secure, *args, **kwargs):
        for realm_type in ["auth_id", "auth_token", "auth_level", "roles"]:
            self._bind_secure_to_zone(realm_type, managed_secure)

    def _bind_secure_to_zone(self, realm_type, managed_secure):
        secure = managed_secure.secure
        if secure.realm:
            realm_value = getattr(secure.realm, realm_type)
            if realm_value:
                if isinstance(realm_value, set) or isinstance(realm_value, list):
                    for sub_realm_value in realm_value:
                        self._bind_secure_to_the_zone(realm_type, sub_realm_value, managed_secure)
                else:
                    self._bind_secure_to_the_zone(realm_type, realm_value, managed_secure)

    def _bind_secure_to_the_zone(self, realm_type, realm_value, managed_secure):
        realm_zones = self.zones.get(realm_type)
        the_zone = realm_zones.get(realm_value, {})
        the_zone.update({managed_secure.secure_id: managed_secure})
        if the_zone not in managed_secure.owners:
            managed_secure.owners.append(the_zone)
        realm_zones.update({realm_value: the_zone})
