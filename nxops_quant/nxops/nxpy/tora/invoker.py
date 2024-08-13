# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-09-07 14:51:41
LastEditTime : 2020-09-07 14:51:45
LastEditors  : yi.mt
Description  : 
'''

import os
import delegator

from autobahn.wamp.types import RegisterOptions

from nxpy.log.logger import LoggerUtils
from nxpy.crossbar.wamp import EasyServiceUtils

in_apphub = False
cwd = "/home/nxapp/abacus"
if "RUNNING_IN_APPHUB" in os.environ and os.environ["RUNNING_IN_APPHUB"] == "true":
    in_apphub = True
    cwd = os.environ["APPHUB_HOME"]

traders = {}

t_component = EasyServiceUtils.create_component(name="trader_invoker")

def invoke_trader(node_id, trader_id):
    command = ""
    if in_apphub:
        command = "nohup apphub abacus_trader {}_{} >> {}/log/trader_{}_{}.log 2>&1 &".format(node_id, trader_id, cwd, node_id, trader_id)
        r = delegator.run(command, binary=in_apphub, cwd=cwd + "/bin", env={"Node_ID": node_id, "Trader_ID": trader_id})
    else:
        command = "nohup python3 -u abacus_trader.py --node_id {} --trader_id {} >> {}/trader_{}_{}.log 2>&1 &".format(node_id, trader_id, cwd, node_id, trader_id)
        r = delegator.run(command, binary=in_apphub, cwd=cwd, env={"Node_ID": node_id, "Trader_ID": trader_id})
    r.block()
    
    if r.return_code != 0:
        LoggerUtils.info("service[{}] CreateTstpTraderApi: [{}][{}] failed".format(t_component._session.authid, node_id, trader_id))
    else:
        LoggerUtils.info("service[{}] CreateTstpTraderApi: [{}][{}] success".format(t_component._session.authid, node_id, trader_id))

@t_component.register(
    "trader.CreateTstpTraderApi",
    options=RegisterOptions(details=True),
)
async def CreateTstpTraderApi(node_id, trader_id, details):
    LoggerUtils.info("service[{}] CreateTstpTraderApi: [{}]".format(t_component._session.authid, trader_id))

    api_id = node_id + "_" + trader_id
    if api_id in traders:
        LoggerUtils.info("service[{}] CreateTstpTraderApi: [{}][{}] existed".format(t_component._session.authid, node_id, trader_id))
        t_component.publish(node_id + "_trader_" + trader_id + ".RTN", "OnCreateTstpTraderApi")
    else:
        invoke_trader(node_id, trader_id)
        traders.update({api_id: 1})


mders = {}

m_component = EasyServiceUtils.create_component(name="mder_invoker")

def invoke_mder(node_id, mder_id):
    command = ""
    if in_apphub:
        command = "nohup apphub abacus_mder {} >> {}/log/mder_{}.log 2>&1 &".format(node_id, cwd, node_id)
        r = delegator.run(command, binary=in_apphub, cwd=cwd + "/bin", env={"Node_ID": node_id})
    else:
        command = "nohup python3 -u abacus_mder.py --node_id {} >> {}/mder_{}.log 2>&1 &".format(node_id, cwd, node_id)
        r = delegator.run(command, binary=in_apphub, cwd=cwd, env={"Node_ID": node_id})
    r.block()
    
    if r.return_code != 0:
        LoggerUtils.info("service[{}] CreateTstpMdApi: [{}] failed".format(m_component._session.authid, node_id))
    else:
        LoggerUtils.info("service[{}] CreateTstpMdApi: [{}] success".format(m_component._session.authid, node_id))

@m_component.register(
    "mder.CreateTstpMdApi",
    options=RegisterOptions(details=True),
)
async def CreateTstpMdApi(node_id, mder_id, details):
    LoggerUtils.info("service[{}] CreateTstpMdApi: [{}]".format(m_component._session.authid, mder_id))

    api_id = node_id
    if api_id in mders:
        LoggerUtils.info("service[{}] CreateTstpMdApi: [{}] existed".format(m_component._session.authid, node_id))
        m_component.publish(node_id + "_mder" + ".RTN", "OnCreateTstpMdApi")
    else:
        invoke_mder(node_id, mder_id)
        mders.update({api_id: 1})

def get_components():
    return [t_component, m_component]