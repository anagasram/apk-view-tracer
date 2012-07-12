#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## Device.py

import socket
import telnetlib
import os

class Device():
    '''
    Device
    '''
    
    def __init__(self, logger, device_port=5554, device_ip="127.0.0.1", view_server_port=4939):
        self.m_logger = logger
        self.device_port = device_port
        self.device_ip = device_ip
        self.view_server_port = view_server_port
        
    def hasService(self):
        ## check whether this device has IWindowServer service
        check_cmd = "adb shell getprop ro.secure"
        out=os.popen(check_cmd) ## return "0\r\n" or "1\r\n"
        res = out.read()
        out.close()
        if (None==res) or (0==len(res)):
            msg = "Please check whether your device or emulator is running?"
            self.m_logger.error(msg)
            return False
        
        elif '1' == res[0]:
            msg = "Your device might not have android IWindowManger service!"
            self.m_logger.error(msg)
            return False
        elif '0' == res[0]:
            self.m_logger.info("Device has IWindowService!")
            return True
        else:
            self.m_logger.error("Failed to check whether device has IWindowService: other errors")
            return False
        
    def stopService(self):
        ## stop window service first
        stopWinService_cmd = "adb shell service call window 2 i32 %s" %self.view_server_port
        out = os.popen(stopWinService_cmd)
        print out.read()
        out.close()
    
    def startService(self):
        ## start window service then
        startWinService_cmd = "adb shell service call window 1 i32 %s" %self.view_server_port
        out = os.popen(startWinService_cmd)
        print out.read()
        out.close()
    
    def init_device(self):        
        ## set port forwarding
        setPortForwarding_cmd = "adb forward tcp:%s tcp:%s" %(self.view_server_port, self.view_server_port)
        out = os.popen(setPortForwarding_cmd)
        out.close()    
        return True
    
    def isServiceRunning(self):        
        viewServer_running_flag = "Result: Parcel(00000000 00000001   '........')"
        viewServer_not_running_flag = "Result: Parcel(00000000 00000000   '........')"
        
        check_command = "adb shell service call window 3 i32 %s" %self.view_server_port
        
        try:
            out = os.popen(check_command)
            res = out.read()
            out.close()
        except Exception, e:
            self.m_logger.error("Failed to check isRunning of IWindowServer service: [%s]" %str(e))
            return False
        
        if viewServer_not_running_flag == res:
            return False
        elif viewServer_running_flag == res:
            return True
        else:
            return False
        
    def open(self):
        try:
            if not self.hasService():
                return False
            
            if not self.isServiceRunning():
                self.startService()
                
            self.init_device()
            return True
        except Exception, e:
            self.m_logger.error("Faild to open device: [%s]" %str(e))
            return False
        
    def close(self):
        if self.isServiceRunning():
            self.stopService()
            
    def getDumpData(self, command="DUMP -1"):
        return self.getInfosByTelnet(command)

    #===============================================================================
    # # method 1 : send command by socket
    # # can not find the end flag?????
    #===============================================================================
    def getInfosBySocket(self, command="DUMP -1"):   
        host = self.device_ip
        port = self.view_server_port
        ## connect the service with a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        try:
            s.connect((host,port))
        except Exception,e:
            print e   
    
        s.send(command+'\n')
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
    
        s.close()
        return data


    #===============================================================================
    # # method 2 : send command by telnet
    #===============================================================================
    def getInfosByTelnet(self, command="DUMP -1"):
        host = self.device_ip
        port = self.view_server_port
        #time_out = config.getServerTimeOut()
        #tn = telnetlib.Telnet(host=host, port=port, timeout=time_out) # this telnetlib is from python lib
        tn = telnetlib.Telnet(host=host, port=port) # this telnetlib is from jython.jar lib
        tn.write(command + "\n")
        data = tn.read_until("DONE")    
        tn.close()
        return data
    
    
    
