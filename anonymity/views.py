from datetime import datetime
import anonymity
from flask import render_template
from flask import request
from anonymity import app
from anonymity import utils
from anonymity import portscan
from anonymity import dnsleak
from anonymity import tor
from anonymity import blacklisted as bl
from anonymity import tracert as tr

#list of http headers
#may be a reason for proxies detection
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

    #about using tor
    #dns_info[1] : second element in this list
    #is IP address of user
    used_tor = tor.check(dns_info[1])

    #False means to check the most popular ports
    #but True provides long and complete check for whole ports range
    #opened_ports = portscan.scan(request.headers.environ.get("REMOTE_ADDR"), False)

    #tracing path to the client :-)
    trace_route = tr.start(dns_info[1])

    #get info about blacklisting status of IP
    black_listed = bl.start(dns_info[1])
    
    #renders page with current data
    return render_template(
        'index.html',
        using_proxies       = proxies,
        user_agent          = request.headers.environ.get("HTTP_USER_AGENT"),      
        language            = request.headers.environ.get("HTTP_ACCEPT_LANGUAGE"),
        dns                 = dns_info,
        tor                 = used_tor,
        black               = black_listed,
        trace               = trace_route,
        opened_ports        = 1, #opened_ports,
        title               = 'Anonymity checker',
        year                = datetime.now().year,
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
