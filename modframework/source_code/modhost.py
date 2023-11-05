import os
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import json
# ModHost For VelaIDE
# (C) 2023, CoraTechWorkspace.
# Apache 2.0 License

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

def get():
    with open("/utils/source/mods.json", "r") as a:
        global mod_list
        mod_list = json.load(a)
    global mods, scripts, utils
    mods = {}
    scripts = {}
    utils = {}
    for i in mod_list:
        with open("/utils/source/{}/mod.json".format(i), "r") as b:
            mods[i] = json.load(b)
        mod_path = "/utils/source/{}".format(i)
        if "scripts" in mods[i].keys():
            for s in mods[i]["scripts"].keys():
                path = mods[i]["scripts"][s]
                if "{mod_path}" in path:
                    path = path.replace("{mod_path}", mod_path)
                    print(path)
                scripts[s] = path
        if "utils" in mods[i].keys():
            for s in mods[i]["utils"].keys():
                path = mods[i]["utils"][s]
                if "{mod_path}" in path:
                    path = path.replace("{mod_path}", mod_path)
                    print(path)
                utils[s] = path
    global sysvalues
    with open("/utils/SystemValues.json", "r", encoding="utf-8") as d:
        sysvalues = json.load(d)
    with open("/utils/port", "w") as r:
        r.write(str(sysvalues["mod_host_port"]))
    return 0
    

def get_mod_list():
    return mod_list

def get_scripts():
    return scripts

def get_mods():
    return mods

def call_scripts(name: str):
    result = os.popen(scripts[name]).readlines()
    print(result)
    ret = ""
    for i in result:
        ret+="{}".format(i)
        print(i)
    return ret

def get_util_content(name: str):
    with open(utils[name], "r", encoding="utf-8") as a:
        content = a.read()
    return content

def get_sys_value(name: str):
    return sysvalues[name]

if __name__ == "__main__":
    get()
    server = ThreadXMLRPCServer(('localhost', sysvalues["mod_host_port"]))
    server.register_function(get_mod_list, 'get_modlist')
    server.register_function(get_mods, 'get_mods')
    server.register_function(get_scripts, 'get_scripts')
    server.register_function(call_scripts, 'call')
    server.register_function(get_sys_value, 'getsysval')
    server.register_function(get_util_content, 'get_util')
    server.register_function(get, 'reload')
    server.serve_forever()

