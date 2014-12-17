# -*- coding: utf-8 -*-
from socket import timeout
import urllib.request,re
class xmlfacebook:
    def __init__(self,id):
        #get rss link
        response = urllib.request.urlopen(id, timeout=10).read().decode("utf-8")
        self.get_it(response)
    def get_it(self,response):
        titles = re.findall(r"<title>(.*?)</title>",response)
        links = re.findall(r"<link>(.*?)</link>",response)
        self.link = links[1].replace("&amp;","&")
        self.title = re.sub("<!\[CDATA\[(.*?)\]\]>|<.*?>", lambda m: m.group(1) or '', titles[1], flags=re.DOTALL)
    def get_title(self):
        return self.title
    def get_link(self):
        return self.link
