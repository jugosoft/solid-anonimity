import socket
import random
import os

class utils(object):
    """description of class"""
    pass

def map(dictionary, substrings):
    """
        Custom mapper for proxies
    """
    proxy = False
    for elem in substrings:
        if dictionary.get(elem) is not None:
            proxy = True
    return proxy

def trace(ip):
    dest_addr = ip #socket.gethostbyname(dest_name) 
    port = 54321 
    max_hops = 40 
    icmp = socket.getprotobyname('icmp') 
    udp = socket.getprotobyname('udp') 
    ttl = 1 
    while True: 
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) 
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp) 
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl) 
        recv_socket.bind(("", port)) 
        send_socket.sendto("", (dest_addr, port)) 
        curr_addr = None 
        curr_name = None 
        try: 
            _, curr_addr = recv_socket.recvfrom(512) 
            curr_addr = curr_addr[0] 
            try: 
                curr_name = socket.gethostbyaddr(curr_addr)[0] 
            except socket.error: 
                curr_name = curr_addr 
        except socket.error: 
            pass 
        finally: 
            send_socket.close() 
            recv_socket.close() 
        if curr_addr is not None: 
            curr_host = "%s (%s)" % (curr_name, curr_addr) 
        else: 
            curr_host = "*" 
            print("%d\t%s" % (ttl, curr_host) )
            ttl += 1 
        if curr_addr == dest_addr or ttl > max_hops: 
            break 