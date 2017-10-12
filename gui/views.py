from flask import request, render_template
from gui import gui
import time
import json

@gui.route('/')
@gui.route('/index')
def index():
    title = {'title': 'Auto-Garden'}
    cdate = {'cdate': time.strftime("%c")} 
    current = {'pump': False, 'moisture': 567}
   
    return render_template("index.html",
                           title=title,
                           cdate=cdate,
                           current=current)

@gui.route("/pump")
def button_click():
    title = {'title': 'Auto Garden'}
    cdate = {'cdate': time.strftime("%c")}
    current = {'pump': True, 'moisture': 567}
   
    return render_template("index.html",
                           title=title,
                           cdate=cdate,
                           current=current)