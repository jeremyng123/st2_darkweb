import socks
import socket
import requests
from bs4 import BeautifulSoup
import pandas as pd

# configuring SOCKS to use TOR
from urllib.request import urlopen

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket


# it is necessary to use TOR for DNS resolution of Onion websites
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (args[0], args[1]))]


socket.getaddrinfo = getaddrinfo


# using requests package to read in the Hidden Wiki onion website on the darknet
def getRequest(url):
    return requests.get(url)


# using bs4 to get the website content into a nice format
def getSoup(res):
    return BeautifulSoup(res.content, "html.parser")


if __name__ == "__main__":
    res = getRequest("http://wikitjerrta4qgz4.onion")
    soup = getSoup(res)
