from xmlrpc.client import ServerProxy

def get_service():
    try:
        with open("/utils/port", "r") as a:
            port = a.read()
        url = "http://127.0.0.1:{}".format(port)
        server = ServerProxy(url)
        return server
    except ConnectionRefusedError:
        print(
            """
连接至URL {} 失败:Connection Refused.
请尝试使用 sudo systemctl start modhost.service 启动ModHost服务后再次尝试
运行 sudo systemctl status modhost.service 查看服务状况
"""
        )
