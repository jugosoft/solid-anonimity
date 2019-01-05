import os
import subprocess
import json
from random import randint
from platform import system as system_name
from subprocess import call as system_call
from random import randint

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def ping(host):
    fn = open(os.devnull, 'w')
    param = '-n' if system_name().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    retcode = system_call(command, stdout=fn, stderr=subprocess.STDOUT)
    fn.close()
    return retcode == 0

def get_dns_leak():
    leak_id = randint(1000000, 9999999)
    resulting_info = []

    for x in range (0, 10):
        ping('.'.join([str(x), str(leak_id), "bash.ws"]))

    response = urlopen("https://bash.ws/dnsleak/test/" + str(leak_id) + "?json")
    data = response.read().decode("utf-8")
    parsed_data = json.loads(data)

    resulting_info.append("Your IP:")
    print(resulting_info[len(resulting_info) - 1])

    for dns_server in parsed_data:
        if dns_server['type'] == "ip":
            if dns_server['country_name']:
                if dns_server['asn']:
                    resulting_info.append(dns_server['ip'] + " [" + dns_server['country_name'] + ", " + dns_server['asn'] + "]")
                    print(resulting_info[len(resulting_info) - 1])
                else:
                    resulting_info.append(dns_server['ip'] + " ["+dns_server['country_name'] + "]")
                    print(resulting_info[len(resulting_info) - 1])
            else:
                resulting_info.append(dns_server['ip'])
                print(resulting_info[len(resulting_info) - 1])

    servers = 0

    for dns_server in parsed_data:
        if dns_server['type'] == "dns":
            servers = servers + 1

    if servers == 0:
        resulting_info.append("No DNS servers found")
        print(resulting_info[len(resulting_info) - 1])
    else:
        resulting_info.append("You use " + str(servers) + " DNS servers:")
        print(resulting_info[len(resulting_info) - 1])
        for dns_server in parsed_data:
            if dns_server['type'] == "dns":
                if dns_server['country_name']:
                    if dns_server['asn']:
                        resulting_info.append(dns_server['ip'] + " [" + dns_server['country_name'] + ", "+dns_server['asn'] + "]")
                        print(resulting_info[len(resulting_info) - 1])
                    else:
                        resulting_info.append(dns_server['ip'] + " ["+dns_server['country_name'] + "]")
                        print(resulting_info[len(resulting_info) - 1])
                else:
                    resulting_info.append(dns_server['ip'])
                    print(resulting_info[len(resulting_info) - 1])
    
    resulting_info.append("Conclusion:")
    print(resulting_info[len(resulting_info) - 1])

    for dns_server in parsed_data:
        if dns_server['type'] == "conclusion":
            if dns_server['ip']:
                resulting_info.append(dns_server['ip'])
                print(resulting_info[len(resulting_info) - 1])

    return resulting_info