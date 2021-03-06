import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import render_template
from flask import request
from anonymity import app
from anonymity import utils
from anonymity import portscan


checklist = {"lang" : True,
             "header" : True,
             "opened_ports" : False,
             "host_name" : False,
             "timestamp" : False,
             "tor" : False,
             "flash" : False,
             "dns_leak" : False,
             "doublesided_ping" : False,
             "provider" : False,
             "vpn" : False,
             "webrtc" : True,
             "user_agent" : True
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
    request.headers.environ["X_FORWARDED_FOR"] = "54.39.138.153"
    proxies = utils.map(request.headers.environ, http_headers)
    print(request.headers.environ.get("HTTP_USER_AGENT"))  
    print("Are proxies enabled - " + str(proxies))
    print(request.headers)
    opened_ports = portscan.scan(request.headers.environ.get("REMOTE_ADDR"))
    return render_template(
        'index.html',
        using_proxies = proxies,
        user_agent = request.headers.environ.get("HTTP_USER_AGENT"),      
        language = request.headers.environ.get("HTTP_ACCEPT_LANGUAGE"),
        opened_ports = opened_ports,
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
