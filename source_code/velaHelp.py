# util bootscript
import wget, json, sys, os
from mod_framework.get_service_entry import get_service

server = get_service()

exec(server.get_util("vhelp"))