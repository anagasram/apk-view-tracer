#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## DeviceConnection.py

import socket
import telnetlib
from GetConfigInfo import GetViewServerInfo
from InitDevice import init_service


#===============================================================================
# # method 1 : send command by socket
# # can not find the end flag?????
#===============================================================================
def getInfosBySocket(cmd):   
    config = GetViewServerInfo()
    host = config.getServerHost()
    port = config.getServerPort()
    ## connect the service with a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    try:
        s.connect((host,port))
    except Exception,e:
        print e   

    s.send(cmd+'\n')
    print "sucess to send command"
    buf_size = 65565
    data=""
    end_flag = "DONE"
    while True:
        res = s.recv(buf_size)
        data+=res
        if  0 <= res.find(end_flag, -5):
            print "read the end flag: 'DONE' "
            break            
                        
    print "sucess to get receive data"
    s.close()
    print data   
    return data


#===============================================================================
# # method 2 : send command by telnet
#===============================================================================
def getInfosByTelnet(command):
    config = GetViewServerInfo()
    host = config.getServerHost()
    port = config.getServerPort()
    time_out = config.getServerTimeOut() 
    tn = telnetlib.Telnet(host, port, time_out)
    tn.write(command + "\n")
    data = tn.read_until("DONE")    
    tn.close()
    print data
    return data

if __name__ == "__main__":
    if False == init_service():
        print "failed to init service!"
        raise Exception
    
    getInfosBySocket("DUMP -1")
    getInfosByTelnet("DUMP -1")
