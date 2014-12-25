#!/usr/bin/python3
# -*- coding: utf-8 -*-
#can yalcin https://github.com/cyweb

import notify2,webbrowser,time,threading,os.path
from gi.repository import Gtk
from rss import facebookrss

def hyperlink(notif_object,action_name,link):
    webbrowser.open(link)
    n.close()

def noti(title,link):
    n = notify2.Notification("Bildirim",title,"facebook")
    n.set_urgency(notify2.URGENCY_CRITICAL)
    n.set_category("device")
    n.add_action(link,"Gözat",hyperlink,link)
    n.show()

def rss():
    identifity = open(current+"/id", "r").readline() #read first line something like https://www.facebook.com/feeds/notifications.php?id=******&viewer=******&key=******&format=rss20
    x=facebookrss.xmlfacebook(identifity)
    title=x.get_title() # find last notification title
    link=x.get_link()   # find last notification facebook url
    date=x.get_date()   # find date
    compare(date,link,title) # check sent notification before !!!!
def compare(date,link,title):
    if os.path.isfile(current+"/last"):
        f=open(current+"/last", "r")
        last=f.readline()
        f.close()
    else:
        last="*"
    if date!=last:
        f=open(current+"/last", "w")
        f.write(date)
        f.close()
        noti(title,link)
def loop():
    while True:
        try:
            rss()
            time.sleep(5)
        except:
            time.sleep(10)
if __name__ == '__main__':
    global n
    global current
    notify2.init("Facebook", mainloop='glib')
    current = os.path.dirname(os.path.realpath(__file__))
    t=threading.Thread(target=loop)
    t.daemon = True
    t.start()
    Gtk.main()
