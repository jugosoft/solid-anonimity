from urllib.request import urlopen

import json

#describes one concrete hop
    #in tracert's path
class Hop:
  def __init__(self, number, hostname, ip, rtt):
      self.number = number
      self.hostname = hostname
      self.ip = ip
      self.rtt = rtt
#end of class

#class for tracing
#agregates list of Hops
class TraceRouteAPI:    
    domain      = None
    api_key     = None    
    output_type = None
    json_result = None

    q = 'https://api.viewdns.info/traceroute/?'

    def __init__(self, domain, api_key = '1a1a2ab50499e745c675461a53601d10fc5ff550', output_type = 'json'):
        self.domain = domain
        self.api_key = api_key
        self.output_type = output_type

    def parse_json(self):
        j = json.loads(self.json_result)['response']['hops']
        self.json_result = list()

        for elem in j:
            self.json_result.append(Hop(number = elem['number'], ip = elem['ip'], rtt = elem['rtt'], hostname = elem['hostname']))

        return self.json_result

    def check(self):
        url = self.q + '&' + self.domain + '&' + self.api_key + '&' + self.output_type  
        self.json_result = '{"query" : {"tool" : "traceroute_PRO","domain" : "128.68.79.25"},"response" : {"hops" : [{ "number" : "1", "hostname" : "obfuscated.internal.network.com", "ip" : "0.0.0.0", "rtt" : "0.000"},{ "number" : "2", "hostname" : "obfuscated.internal.network.com", "ip" : "0.0.0.0", "rtt" : "1.000"},{ "number" : "3", "hostname" : "nyc2-brdr-02.inet.qwest.net", "ip" : "205.171.134.90", "rtt" : "29.775"},{ "number" : "4", "hostname" : "63.146.27.2", "ip" : "63.146.27.2", "rtt" : "30.360"},{ "number" : "5", "hostname" : "et4-0-2.franco71.fra.seabone.net", "ip" : "195.22.211.193", "rtt" : "103.884"},{ "number" : "6", "hostname" : "ojsc-vimpelcom.franco71.fra.seabone.net", "ip" : "89.221.34.113", "rtt" : "125.386"},{ "number" : "7", "hostname" : "pe02.Saratov.gldn.net", "ip" : "79.104.239.243", "rtt" : "168.906"},{ "number" : "8", "hostname" : "62.231.18.154", "ip" : "62.231.18.154", "rtt" : "174.059"},{ "number" : "9", "hostname" : "10.2.243.105", "ip" : "10.2.243.105", "rtt" : "171.001"},{ "number" : "10", "hostname" : "89.179.17.247", "ip" : "89.179.17.247", "rtt" : "168.523"},{ "number" : "11", "hostname" : "*", "ip" : "89.179.17.247", "rtt" : "(89.179.17.247)"},{ "number" : "12", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "13", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "14", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "15", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "16", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "17", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "18", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "19", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "20", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "21", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "22", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "23", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "24", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "25", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "26", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "27", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "28", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "29", "hostname" : "*", "ip" : "*", "rtt" : "*"},{ "number" : "30", "hostname" : "*", "ip" : "*", "rtt" : "*"}]}}'
        #self.json_result = urlopen(url)
        return self.parse_json()


#starts tracert via someone's
#API
def start(domain):
    tr = TraceRouteAPI(domain = domain)
    return tr.check()
