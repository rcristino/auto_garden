from flask import request, render_template
from gui import gui
import time
import json

@gui.route('/')
@gui.route('/index')
def index():
    addr = {'ip': get_ip(), 'port': 5000}
    title = {'title': 'Auto-Garden'}
    cdate = {'cdate': time.strftime("%c")} 
    current = {'pump': False, 'moisture': 567}
   
    return render_template("index.html",
                           addr=addr,
                           title=title,
                           cdate=cdate,
                           current=current)

@gui.route("/pump")
def button_click():
    addr = {'ip': get_ip(), 'port': 5000}
    title = {'title': 'Auto Garden'}
    cdate = {'cdate': time.strftime("%c")}
    current = {'pump': True, 'moisture': 567}
   
    return render_template("index.html",
                           addr=addr,
                           title=title,
                           cdate=cdate,
                           current=current)

def get_ip():
    import socket
    import os
    
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    return ipaddr