import socket
import sys
import string
import json
from urllib.request import urlopen

class BlackListCheckerAPI:
    #fields
    ip = None
    api_key = None    
    output_type = None
    json_result = None

    query = 'https://api.viewdns.info/spamdblookup/?'

    def __init__(self, ip, api_key = '1a1a2ab50499e745c675461a53601d10fc5ff550', output_type = 'json'):
        self.ip = ip
        self.api_key = api_key
        self.output_type = output_type

    def parse_json(self):
        j = json.loads(self.json_result)['response']['dbs']
        self.json_result = dict()

        for elem in j:
            self.json_result.update({ elem['name'] : elem['result'] })

        return self.json_result

    def check(self):
        url = self.query + '&' + self.ip + '&' + self.api_key + '&' + self.output_type  
        self.json_result = '{"query" : {"tool" : "spamdblookup_PRO","ip" : "1.2.3.4"},"response" : { "dbs" : [{ "name" : "b.barracudacentral.org", "result" : "ok"},{ "name" : "bl.deadbeef.com", "result" : "ok"},{ "name" : "bl.emailbasura.org", "result" : "ok"},{ "name" : "bl.spamcop.net", "result" : "ok"},{ "name" : "blacklist.woody.ch", "result" : "ok"},{ "name" : "cbl.abuseat.org", "result" : "ok"},{ "name" : "combined.rbl.msrbl.net", "result" : "ok"},{ "name" : "db.wpbl.info", "result" : "ok"},{ "name" : "dnsbl.cyberlogic.net", "result" : "ok"},{ "name" : "dnsbl.njabl.org", "result" : "ok"},{ "name" : "dnsbl.sorbs.net", "result" : "ok"},{ "name" : "dnsbl-3.uceprotect.net", "result" : "ok"},{ "name" : "drone.abuse.ch", "result" : "ok"},{ "name" : "http.dnsbl.sorbs.net", "result" : "ok"},{ "name" : "httpbl.abuse.ch", "result" : "ok"},{ "name" : "images.rbl.msrbl.net", "result" : "ok"},{ "name" : "ips.backscatterer.org", "result" : "ok"},{ "name" : "nomail.rhsbl.sorbs.net", "result" : "ok"},{ "name" : "pbl.spamhaus.org", "result" : "ok"},{ "name" : "phishing.rbl.msrbl.net", "result" : "ok"},{ "name" : "sbl.spamhaus.org", "result" : "ok"},{ "name" : "smtp.dnsbl.sorbs.net", "result" : "ok"},{ "name" : "socks.dnsbl.sorbs.net", "result" : "ok"},{ "name" : "spam.dnsbl.sorbs.net", "result" : "ok"},{ "name" : "spam.rbl.msrbl.net", "result" : "ok"},{ "name" : "spam.spamrats.com", "result" : "ok"},{ "name" : "ubl.unsubscore.com", "result" : "ok"},{ "name" : "virus.rbl.msrbl.net", "result" : "ok"},{ "name" : "web.dnsbl.sorbs.net", "result" : "ok"},{ "name" : "xbl.spamhaus.org", "result" : "ok"},{ "name" : "zen.spamhaus.org", "result" : "ok"},{ "name" : "zombie.dnsbl.sorbs.net", "result" : "ok"}]}}'
        #self.json_result = urlopen(url)
        return self.parse_json()

def start(ip):
    bl = BlackListCheckerAPI(ip = ip)
    return bl.check()