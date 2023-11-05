from colorama import init, Fore

class log:
    def __init__(self):
        init(autoreset = True)
    
    def process(self, content: str):
        print(":: {}".format(content))
    
    def child_process(self, content: str):
        print("=> "+content)
    
    def tip(self, content: str):
        print(":: "+Fore.LIGHTYELLOW_EX+content)
    
    def warn(self, content: str):
        print(":: "+Fore.LIGHTYELLOW_EX+"警告 "+content)
    
    def error(self, content: str):
        print(":: "+Fore.LIGHTRED_EX+"错误 "+content)