# velaHelp bootscript
from xmlrpc.client import ServerProxy
from mod_framework.get_service_entry import get_service

server = get_service()

print(server.call("boot"))