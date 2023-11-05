print("""
欢迎使用Xiaomi Vela集成开发环境!
By Yakuake at Bilibili
基于Ubuntu 20.04
这里是其帮助程序.Ctrl+C退出.
""")

if os.path.isfile("/cache/content.json"):
    os.remove("/cache/content.json")
wget.download("https://testground-distribution-1301360149.cos.ap-nanjing.myqcloud.com/content.json","/cache/content.json")
with open("/cache/content.json","r",encoding="utf-8") as j:
    cont = json.load(j)
while True:
    try:
        promp = input("\nhelp>")
        print(cont[promp])
    except KeyboardInterrupt:
        sys.exit()
