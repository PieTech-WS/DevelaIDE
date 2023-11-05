import os, webbrowser
import shutil
from xmlrpc.client import ServerProxy

server = ServerProxy("http://localhost:8888")
build = server.getsysval("build")

with open("/home/yakuake/oobe", "r") as status:
    stat = int(status.read())
if stat == 0:
    webbrowser.open("https://github.com/PieTech-WS/DevelaIDE/blob/main/README.md")
    print("Open README on GitHub or open https://github.com/PieTech-WS/DevelaIDE/blob/main/README.md")

if os.path.isdir("/home/yakuake/temp"):
    shutil.rmtree("/home/yakuake/temp")
os.mkdir("/home/yakuake/temp")

os.system("figlet ARE U OK")

print("""
欢迎使用DevelaOS by Yakuake!
构建版本:{}
输入aiot-ide以打开AIoT-IDE
输入velaHelp查看帮助文档(需要联网)
""".format(build))
