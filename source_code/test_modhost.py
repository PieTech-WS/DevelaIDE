from xmlrpc.client import ServerProxy, Fault
import sys
from mod_framework.get_service_entry import get_service


if __name__ == '__main__':
    try:
        print("ModHost实时调试台.\n输入q或使用快捷键Ctrl+C以退出")
        server = get_service()
        while True:
            res = input("modtest>")
            if res == "reload":
                res = server.reload()
            elif "call" in res:
                res = res.replace("call","")
                print(server.call(res))
            elif res == "getmods":
                print(server.get_mods())
            elif "getu" in res:
                res = res.replace("getu","")
                print(server.get_util(res))
            elif "getsv" in res:
                res = res.replace("getsv","")
                print(server.getsysval(res))
            elif res == "q":
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()
    except Fault:
        print(":: 错误的操作")