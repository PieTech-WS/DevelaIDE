# ModFramework Preinstall Environment
# (C) 2023, CoraTech Workspace.
# Apache-2.0 License


class env:
    def __init__(self):
        self.log_session = log()
        self.check_lock()
        self.get_service()
        self.log_session.process("获取ModCreate存储库地址中...")
        self.repo = self.service.getsysval("mod_release")[self.service.getsysval("region")]
        self.check_index()
        self.get_index()
    
    def check_index(self):
        if not os.path.isfile("/utils/cache/index.json"):
            self.log_session.tip("未检测到Index文件.正在获取中...")
            self.refresh_index()

    def check_lock(self):
        if not os.path.isfile("/utils/modpe.lock"):
            self.log_session.process("创建modpe.lock锁 位于/utils/modpe.lock")
            with open("/utils/modpe.lock", "w") as a:
                a.write("1")
            self.log_session.child_process("写入:/utils/modpe.lock")
        else:
            self.log_session.error("存在锁modpe.lock.在锁消失前, modpe无法再次运行.")
            sys.exit()
    
    def get_service(self):
        self.service = get_service()

    def refresh_index(self):
        self.log_session.process("获取Index中...")
        self.log_session.child_process("下载index.json到/utils/cache/index.json")
        wget.download("{}index.json".format(self.repo), "/utils/cache/index.json")
    
    def get_index(self):
        self.log_session.process("读取ModCreate索引列表")
        with open("/utils/cache/index.json", "r", encoding="utf-8") as d:
            self.index = json.load(d)
    
    def select_mod(self, expression: str):
        try:
            exp = expression.split("@")
            self.name = exp[0]
            version = exp[1]
            self.filename = self.index[self.name][version]["filename"]
            self.author = self.index[self.name][version]["author"]
            self.hash = self.index[self.name][version]["hash"]
            self.log_session.process("命中软件包: {}@{}<author:{}>".format(self.name, version, self.author))
        except KeyError:
            self.log_session.error("没有这个软件包或者没有该软件包的此版本")
    
    def select_mod_rmv(self, expression: str):
        self.name = expression

    def check_before_ins(self):
        self.service.reload()
        mods = self.service.get_mods()
        if self.name in mods:
            self.log_session.tip("已安装此软件包, 但它可能不是最新的.")
            i = input(":: 已安装此软件包,是否重新安装/更新?(y/n)")
            if i == "y" or i == "Y":
                shutil.rmtree("/utils/source/{}".format(self.name))
            else:
                self.log_session.process("已拒绝.")

    def dl(self):
        self.check_before_ins()
        self.log_session.child_process("命中软件包: {}.开始下载,从 ".format(self.name)+"{}{}".format(self.repo, self.filename))
        self.random_int = str(random.randint(0,9))+str(random.randint(10, 90))
        self.log_session.child_process("生成随机文件名中")
        self.cache_filename = hashlib.md5(bytes("{}{}".format(self.filename,self.random_int), "utf-8")).hexdigest()
        self.log_session.child_process("使用wget下载{}".format(self.name))
        wget.download("{}{}".format(self.repo, self.filename), "/utils/cache/{}".format(self.cache_filename))
        with open("/utils/cache/{}".format(self.cache_filename), "b+r") as byt:
            byte = byt.read()
        hash = hashlib.md5(byte).hexdigest()
        if hash != self.hash:
            self.log_session.error("无法验证此软件包.(MD5验证失败验证)")
        else:
            self.ins()


    def ins(self):
        self.log_session.process("开始安装:{}".format(self.name))
        self.log_session.child_process("使用tar解压文件")
        os.system("tar -xvf /utils/cache/{} -C /utils/source".format(self.cache_filename))
        self.log_session.child_process("更新已安装mod列表")
        with open("/utils/source/mods.json", "r") as a:
            oringin: list = json.load(a)
            oringin.append(self.name)
        with open("/utils/source/mods.json", "w") as a:
            json.dump(oringin, a)
        self.log_session.child_process("正在告知ModHost以刷新Host缓存...")
        self.service.reload()
        self.log_session.child_process("完成.")

    def rmv(self):
        self.service.reload()
        mods = self.service.get_mods()
        if self.name in mods:
            shutil.rmtree("/utils/source/{}".format(self.name))
            with open("/utils/source/mods.json", "r") as a:
                oringin: list = json.load(a)
                oringin.remove(self.name)
            with open("/utils/source/mods.json", "w") as a:
                json.dump(oringin, a)
            self.log_session.child_process("正在告知ModHost以刷新Host缓存...")
            self.service.reload()
            self.log_session.child_process("完成.")
        else:
            self.log_session.tip("你还没有安装此软件包..")
            self.log_session.process("今日无事可做")

    def exit(self):
        os.remove("/utils/modpe.lock")
        sys.exit()

if __name__ == "__main__":
    ev = env()
    ev.log_session.process("Mod预安装环境初始化完成")
    ev.log_session.process("版本0.2.1 (C)2023, CoraTech Workspace")
    try:
        while True:
            inter = input("\nmodPE@modhost>")
            ev.log_session.process("操作: "+inter)
            if " " in inter:
                inters = inter.split(" ")
                head = inters[0]
                if head == "install":
                    ev.select_mod(inters[1])
                    ev.dl()
                elif head == "remove":
                    ev.select_mod_rmv(inters[1])
                    ev.rmv()
            else:
                if inter == 'exit':
                    ev.exit()
                
                elif inter == "clean":
                    exec(ev.service.get_util("mod_clean"))
    except KeyboardInterrupt:
        ev.exit()
