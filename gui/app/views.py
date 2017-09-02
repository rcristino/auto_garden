from flask import render_template
from app import app
import time

@app.route('/')
@app.route('/index')
def index():
    title = {'title': 'Auto-Garden'}
    cdate = {'cdate': time.strftime("%c")}
    current = {'pump': False, 'moisture': 567}
    records = [ 
        { 
            'moisture': 123, 
            'timestamp': time.strftime("%c") 
        },
        { 
            'moisture': 321, 
            'timestamp': time.strftime("%c")
        },
    ]
    return render_template("index.html",
                           title=title,
                           cdate=cdate,
                           current=current,
                           records=records)

@app.route("/pump")
def button_click():
    title = {'title': 'Auto Garden'}
    cdate = {'cdate': time.strftime("%c")}
    current = {'pump': True, 'moisture': 567}
    records = [ 
        { 
            'moisture': 123, 
            'timestamp': time.strftime("%c") 
        },
        { 
            'moisture': 321, 
            'timestamp': time.strftime("%c")
        },
    ]
    return render_template("index.html",
                           title=title,
                           cdate=cdate,
                           current=current,
                           records=records)