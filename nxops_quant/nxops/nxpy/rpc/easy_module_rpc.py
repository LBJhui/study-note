# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-27 15:39:55
@LastEditTime : 2020-07-29 13:55:15
@LastEditors  : yi.mt
@Description  : 
'''
import sys
import hashlib
import importlib

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

modules = {}

def import_file(module_name, module_location):
    module_spec = importlib.util.spec_from_file_location(module_name, location=module_location)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    return module

@dispatcher.add_method
def load(file_path):
    md5 = hashlib.md5()
    md5.update(bytes(file_path, encoding="UTF-8"))
    module_name = md5.hexdigest()

    module = import_file(module_name, module_location=file_path)

    if module:
        modules.update({module_name: module})
        return module_name
    else:
        return None

@dispatcher.add_method
def get_alias(module_name):
    module = modules.get(module_name, None)
    return module.alias if module and "alias" in module.__dict__ else None

@dispatcher.add_method
def get_realm(module_name, realm_type=None, easy_module_id=None):
    module = modules.get(module_name, None)
    realm = module.realm if module and "realm" in module.__dict__ else None

    if realm and easy_module_id:
            rules = realm.get("rules", None)
            realm = rules.get(easy_module_id, None) if rules else None

    result = realm
    if realm and realm_type:
        result = realm.get(realm_type, None)
    
    if isinstance(result, set):
        result = list(result)

    return result

@dispatcher.add_method
def get_easy_modules(module_name):
    module = modules.get(module_name, None)
    ware = module.ware if module and "ware" in module.__dict__ else None
    easy_module_ids = None
    if ware:
        easy_module_ids = ware.keys()
    return list(easy_module_ids) if easy_module_ids else None

@dispatcher.add_method
def get_easy_module_definition(module_name, easy_module_id):
    module = modules.get(module_name, None)
    ware = module.ware if module and "ware" in module.__dict__ else None
    easy_module_definition = None
    if ware:
        easy_module_definition = ware.get(easy_module_id, None)
    if easy_module_definition and isinstance(easy_module_definition, tuple):
        easy_module_definition = {"sql": easy_module_definition[0], "meta": easy_module_definition[1]}
    return easy_module_definition


@Request.application
def application(request):
    resp = JSONRPCResponseManager.handle(
        request.data, dispatcher)

    response = Response(resp.json, mimetype='application/json')
    
    response.headers["Access-Control-Allow-Headers"] = "x-requested-with,Content-Type"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST"
    
    return response


if __name__ == '__main__':
    sys.path.append("E:\\works\\vscode\\python\\abacus")
    run_simple('localhost', 7766, application)