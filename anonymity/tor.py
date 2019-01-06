from urllib.request import urlopen
import csv

def check(ip):
    url = "https://torstatus.blutmagie.de/ip_list_all.php/Tor_ip_list_ALL.csv"      
    response = urlopen(url)

    #bytes object
    data = response.read()      
    text = data.decode('utf-8') 

    if ip in text:
        return True

    return False