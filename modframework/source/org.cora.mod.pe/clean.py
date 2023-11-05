import os
import shutil


if os.path.isdir("/utils/cache"):
    shutil.rmtree("/utils/cache")
os.mkdir("/utils/cache")
os.system("chmod 777 /utils/cache")