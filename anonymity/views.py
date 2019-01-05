from datetime import datetime
from flask import render_template
from flask import request
from anonymity import app
from anonymity import utils
from anonymity import portscan
from anonymity import dnsleak

#to do list
checklist = {"lang" : True,
             "header" : True,
             "opened_ports" : False,
             "timestamp" : False,
             "tor" : False,
             "flash" : False,
             "dns_leak" : True,
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
    #testing proxies detection
    #detects usage proxies according to the HTTP headers 
    #watch %http_headers% variable
    request.headers.environ["X_FORWARDED_FOR"] = "54.39.138.153"
    proxies = utils.map(request.headers.environ, http_headers)
    print(request.headers.environ.get("HTTP_USER_AGENT"))  
    print("Are proxies enabled - " + str(proxies))

    #just for development usability
    print(request.headers)

    #getting info about dns leaks
    dns_info = dnsleak.get_dns_leak()

    #False means to check the most popular ports
    #but True provides long and complete check for whole ports range
    opened_ports = portscan.scan(request.headers.environ.get("REMOTE_ADDR"), False)

    #renders page with current data
    return render_template(
        'index.html',
        using_proxies = proxies,
        user_agent = request.headers.environ.get("HTTP_USER_AGENT"),      
        language = request.headers.environ.get("HTTP_ACCEPT_LANGUAGE"),
        dns = dns_info,
        opened_ports = opened_ports,
        title='Anonymity checker',
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
