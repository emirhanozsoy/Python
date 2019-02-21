from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
from torrequest import TorRequest
import time, socks, socket
from stem import Signal
from stem.control import Controller


ua = UserAgent()


with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password = 'YourPasswordHere')
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket   

    controller.signal(Signal.NEWNYM)
    if controller.is_newnym_available() == False:
        print("Waitting time for Tor to change IP: "+ str(controller.get_newnym_wait()) +" seconds")
        time.sleep(controller.get_newnym_wait())
    req = Request(url)
    req.add_header('User-Agent', ua.random)
    req_doc= urlopen(req)#.read().decode('utf8')
    print(req_doc)