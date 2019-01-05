import socket
import sys

class portscan:
    pass

def scan(host):

    mas = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 
           80, 110, 115, 123, 137, 138, 139, 143, 
           161, 179, 443, 445, 514, 515, 993, 995, 
           1080, 1194, 1433, 1702, 1723, 3128, 3268, 
           3306, 3389, 5432, 5060, 5900, 5938, 8080, 
           10000, 20000]
    res = []
    counter = 0

    print("port checking is initialized successfully.")
    print("read information below attentivly:")
    print ("#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#")
    
    for port in mas:
        s = socket.socket()
        s.settimeout(1)

        if port > 445:
            break

        print("#" + str(counter) + " port " + str(port) + " is checking...")
        counter = counter + 1

        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            s.close
            print (host + ": " + str(port) + " is opened (!!!!!)")
            res.append(str(port))
    print ("#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#")

    return res
   