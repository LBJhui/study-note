# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-09-09 13:07:58
LastEditTime : 2020-09-09 13:08:02
LastEditors  : yi.mt
Description  : 
'''

import inspect
import traderapi

API_CLAZZ_TEMPLATE = """
package com.nxapp.tora.trader;

import cn.hutool.core.bean.BeanUtil;
import cn.hutool.core.lang.UUID;
import cn.hutool.core.util.ReflectUtil;
import cn.hutool.crypto.digest.MD5;
import io.crossbar.autobahn.wamp.Client;
import io.crossbar.autobahn.wamp.Session;
import io.crossbar.autobahn.wamp.auth.TicketAuth;
import io.crossbar.autobahn.wamp.types.CallResult;
import io.crossbar.autobahn.wamp.types.EventDetails;
import io.crossbar.autobahn.wamp.types.SessionDetails;

import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

class EasyAgentAuthenticator extends TicketAuth {{

    public EasyAgentAuthenticator(String authId) {{
        super(authId, MD5.create().digestHex(authId, "UTF-8"));
    }}
}}

public class EasyAgentTraderApi {{
    private final String AUTH_ID_PREFIX = "_trader_agent_";

    private String nodeId = null;

    private String traderId = null;

    private String authId = null;

    private String frontAddress = null;

    private EasyAgentTraderSpi spi = null;

    private Session session = null;

    private boolean created = false;

    public EasyAgentTraderApi(String traderId) {{
        this("tora", traderId);
    }}

    public EasyAgentTraderApi(String nodeId, String traderId) {{
        this.nodeId = nodeId;
        this.traderId = traderId;
        this.authId = this.nodeId + AUTH_ID_PREFIX + this.traderId + "_" + UUID.randomUUID().toString().substring(0, 8);
        this.session = new Session();

        this.session.addOnJoinListener(this::onSessionJoin);
    }}

    private Object[] parseArgs(List<Object> args) {{
        Object[] nargs = new Object[args.size() - 1];

        for (int i = 1; i < args.size(); ++i) {{
            nargs[i - 1] = args.get(i);
        }}

        return nargs;
    }}

    private void onCreateTstpTraderApi() {{
        this.created = true;
    }}

    private void dispatchResponse(List<Object> args, Map<String, Object> kwargs, EventDetails details) {{
        String procedure = (String) args.get(0);
        if (this.spi != null) {{
            Object[] iargs = this.parseArgs(args);
            ReflectUtil.invoke(this, procedure, iargs);
        }}
    }}

    private void dispatchReturn(List<Object> args, Map<String, Object> kwargs, EventDetails details) {{
        String procedure = (String) args.get(0);
        if ("OnCreateTstpTraderApi".equals(procedure)) {{
            this.onCreateTstpTraderApi();
        }} else if (this.spi != null) {{
            Object[] iargs = this.parseArgs(args);
            ReflectUtil.invoke(this, procedure, iargs);
        }}
    }}

    private void onSessionJoin(Session session, SessionDetails details) {{
        session.subscribe(this.nodeId + "_trader_" + this.traderId + ".RSP." + this.authId, this::dispatchResponse);
        session.subscribe(this.nodeId + "_trader_" + this.traderId + ".RTN", this::dispatchReturn);
        CompletableFuture<CallResult> callFuture = session.call("trader.CreateTstpTraderApi", this.nodeId, this.traderId);
    }}

    private int getReqMethodResult(CompletableFuture<CallResult> callFuture) {{
        int result = -1;
        try {{
            result = (int) callFuture.get().results.get(0);
        }} catch (Exception e) {{
            e.printStackTrace();
        }}
        return result;
    }}

    public Session getSession() {{
        return this.session;
    }}

    public void RegisterFront(String frontAddress) {{
        this.frontAddress = frontAddress;
    }}

    public void RegisterSpi(EasyAgentTraderSpi spi) {{
        this.spi = spi;
    }}

    public void Init() {{
        Client client = new Client(this.session, this.frontAddress, "toraservice", new EasyAgentAuthenticator(authId));
        client.connect();

        int count = 0;
        while (!this.created) {{
            try {{
                Thread.sleep(1);
                ++count;

                if(count >= 5000) {{
                    count = 0;
                    CompletableFuture<CallResult> callFuture = this.session.call("trader.CreateTstpTraderApi", this.nodeId, this.traderId);
                }}
            }} catch (Exception e) {{
            }}
        }}

        CompletableFuture<CallResult> callFuture = this.session.call(this.nodeId + "_trader_" + this.traderId + ".REQ", "Init");
    }}
    {req_methods_code}
    {rsp_methods_code}
}}
"""

REQ_METHOD_TEMPLATE = """
    public int {method_name}(com.nxapp.tora.trader.{field_arg_class} {field_arg_name}, int nRequestID) {{
        CompletableFuture<CallResult> callFuture = this.session.call(this.nodeId + "_trader_" + this.traderId + ".REQ", "{method_name}", {field_arg_name}, nRequestID);

        return this.getReqMethodResult(callFuture);
    }}
"""
PROXY_RSP_METHOD_TEMPLATE = """
    private void {method_name}({method_args}) {{
        if (this.spi != null) {{
            {parse_fields_from_map}
            this.spi.{method_name}({call_method_args});
        }}
    }}
"""
PARSE_FIELD_TEMPLATE = """
            {field_arg_class} {field_arg_name} = null;
            if ({field_arg_name}Map != null) {{
                {field_arg_name} = new {field_arg_class}();
                BeanUtil.fillBeanWithMap({field_arg_name}Map, {field_arg_name}, true);
            }}
"""
def build_api_methods():
    req_methods_code = ""
    for method_name, method_obj in traderapi.CTORATstpTraderApi.__dict__.items():
        if method_name[0:3] == "Req":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            field_arg_name = args[1]
            field_arg_class = "CTORATstp" + field_arg_name[1:]

            req_methods_code += REQ_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class, field_arg_name=field_arg_name)

    rsp_methods_code = ""
    for method_name, method_obj in traderapi.CTORATstpTraderSpi.__dict__.items():
        if method_name[0:2] == "On":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            method_args = []
            call_method_args = []
            parse_fields_from_map = ""
            for arg_name in args:
                if arg_name[0:1] == "p":
                    method_args.append("Map<String, Object> " + arg_name + "Map")
                    call_method_args.append(arg_name)
                    parse_fields_from_map += PARSE_FIELD_TEMPLATE.format(field_arg_name=arg_name, field_arg_class="com.nxapp.tora.trader.CTORATstp" + arg_name[1:] + ("" if arg_name[-5:] == "Field" else "Field"))
                elif arg_name[0:1] == "n":
                    method_args.append("int " + arg_name)
                    call_method_args.append(arg_name)
                elif arg_name[0:1] == "b":
                    method_args.append("boolean " + arg_name)
                    call_method_args.append(arg_name)

            method_args = ", ".join(method_args)
            call_method_args = ", ".join(call_method_args)
            rsp_method = PROXY_RSP_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, parse_fields_from_map=parse_fields_from_map, call_method_args=call_method_args)
            rsp_methods_code += rsp_method

    api_clazz_code = API_CLAZZ_TEMPLATE.format(req_methods_code=req_methods_code, rsp_methods_code=rsp_methods_code)

    with open(f"./build_java/EasyAgentTraderApi.java", "w") as jf:
        jf.write(api_clazz_code)


SPI_CLAZZ_TEMPLATE = """
package com.nxapp.tora.trader;

import io.crossbar.autobahn.wamp.Session;

public class EasyAgentTraderSpi {{

    protected EasyAgentTraderApi api = null;

    protected Session session = null;

    public EasyAgentTraderSpi(EasyAgentTraderApi api) {{
        this.api = api;
        this.session = api.getSession();
    }}
    {methods_code}
}}
"""

RSP_METHOD_TEMPLATE = """
    public void {method_name}({method_args}) {{ }}
"""

def build_spi_rsp_methods():
    methods_code = ""
    for method_name, method_obj in traderapi.CTORATstpTraderSpi.__dict__.items():
        if method_name[0:2] == "On":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            method_args = []
            for arg_name in args:
                if arg_name[0:1] == "p":
                    method_args.append("com.nxapp.tora.trader.CTORATstp" + arg_name[1:] + ("" if arg_name[-5:] == "Field" else "Field") + " " + arg_name)
                elif arg_name[0:1] == "n":
                    method_args.append("int " + arg_name)
                elif arg_name[0:1] == "b":
                    method_args.append("boolean " + arg_name)

            method_args = ", ".join(method_args)
            rsp_method = RSP_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
            methods_code += rsp_method

    spi_clazz_code = SPI_CLAZZ_TEMPLATE.format(methods_code=methods_code)
    with open(f"./build_java/EasyAgentTraderSpi.java", "w") as jf:
        jf.write(spi_clazz_code)

FIELD_CLAZZ_TEMPLATE = """
package com.nxapp.tora.trader;

import java.util.HashMap;
import java.util.Map;

public class {field_clazz_name} {{
    public String _module_ = "traderapi";
    public String _clazz_ = "{field_clazz_name}";
    {attrs_def_code}
}}
"""

ATTR_DEF_TEMPLATE = """
    public {attr_type} {attr_name} = {attr_value};
"""

def build_api_fields():
    for field_clazz_name, clazz_obj in traderapi.__dict__.items():
        if field_clazz_name[-5:] == "Field":
            obj = clazz_obj()
            attrs_def_code = ""
            attrs_put_code = ""
            for attr_name in clazz_obj.__swig_setmethods__.keys():
                attr_value = obj.__getattr__(attr_name)
                if isinstance(attr_value, str):
                    attrs_def_code += ATTR_DEF_TEMPLATE.format(attr_type="String", attr_name=attr_name, attr_value="\"\"")
                elif isinstance(attr_value, int):
                    attrs_def_code += ATTR_DEF_TEMPLATE.format(attr_type="int", attr_name=attr_name, attr_value=0)
                elif isinstance(attr_value, float):
                    attrs_def_code += ATTR_DEF_TEMPLATE.format(attr_type="double", attr_name=attr_name, attr_value=0)
                else:
                    print(f"{field_clazz_name} {attr_name} undefined type")

            field_clazz_code = FIELD_CLAZZ_TEMPLATE.format(field_clazz_name=field_clazz_name, attrs_def_code=attrs_def_code)

            with open(f"./build_java/{field_clazz_name}.java", "w") as jf:
                jf.write(field_clazz_code)

CONSTANTS_FILE_TEMPLATE = """package com.nxapp.tora.trader;

public class ToraConstants {{
{constants_code}
}}
"""

CONSTANT_CODE_TEMPLATE = """    public static {constant_clazz_name} {constant_name} = {constant_value};
"""

def build_constants():
    constants_code = ""
    for constant_name, constant_value in traderapi.__dict__.items():
        if constant_name[0:5] == "TORA_":
            constant_clazz_name = "String"
            if isinstance(constant_value, str):
                constant_value = f"\"{constant_value}\""
            elif isinstance(constant_value, int):
                constant_clazz_name = "int"
            elif isinstance(constant_value, float):
                constant_clazz_name = "double"
            constants_code += CONSTANT_CODE_TEMPLATE.format(constant_clazz_name=constant_clazz_name, constant_name=constant_name, constant_value=constant_value)
        
    constants_file_code = CONSTANTS_FILE_TEMPLATE.format(constants_code=constants_code)
    with open(f"./build_java/ToraConstants.java", "w") as jf:
        jf.write(constants_file_code)

if __name__ == "__main__":
    build_api_methods()
    build_api_fields()
    build_spi_rsp_methods()
    build_constants()

