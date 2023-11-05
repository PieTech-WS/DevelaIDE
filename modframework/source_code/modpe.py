# util bootstrap
import os, wget, sys, json, random, hashlib
import shutil
from mod_framework.get_service_entry import get_service
from mod_framework.essentials.log_ import log

server = get_service()

exec(server.get_util("modpe"))