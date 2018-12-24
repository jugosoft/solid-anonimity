"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from anonymity import app
from anonymity import utils

checklist = {"lang" : False,
             "header" : False,
             "opened_ports" : False,
             "host_name" : False,
             "timestamp" : False,
             "tor" : False,
             "flash" : False,
             "dns_leak" : False,
             "doublesided_ping" : False,
             "provider" : False,
             "vpn" : False,
             "webrtc" : False,
             "user_agent" : False
    }

http_headers = ["HTTP_VIA",                 "HTTP_X_FORWARDED_FOR", 
                "HTTP_FORWARDED_FOR",       "HTTP_X_FORWARDED", 
                "HTTP_FORWARDED",           "HTTP_CLIENT_IP", 
                "HTTP_FORWARDED_FOR_IP",    "VIA",
                "FORWARDED_FOR",            "X_FORWARDED", 
                "FORWARDED", "CLIENT_IP",   "FORWARDED_FOR_IP",
                "HTTP_PROXY_CONNECTION",    "X_FORWARDED_FOR"]


@app.route('/')
@app.route('/home')
def home():
    str_tmp = request.headers
    proxies = utils.map(str_tmp, http_headers)
    print("Are proxies enabled - " + str(proxies))
    print(str_tmp)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
