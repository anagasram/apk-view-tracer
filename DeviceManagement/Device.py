#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## Device.py

import os
from AdbCommand import AdbCommand
from ViewServerCommand import ViewServerCommand

class Device():
    '''
    Device
    '''
    
    def __init__(self, logger, device_name="emulator-5554", device_port=5554, device_address="127.0.0.1", view_server_port=4939):
        self.m_logger = logger
        self.device_name = device_name
        self.device_port = device_port
        self.device_address = device_address
        self.view_server_port = view_server_port
        
        self.adb_console = AdbCommand(self.m_logger, self.device_name, self.device_port)
        self.view_console = ViewServerCommand(self.m_logger, self.device_address, self.view_server_port)
        
    def hasService(self):
        ## check whether this device has IWindowServer service
        check_cmd = "adb -s %s shell getprop ro.secure" %self.device_name
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
            msg = "Device has IWindowService!"
            return True
        else:
            self.m_logger.error("Failed to check whether device has IWindowService: other errors")
            return False
        
    def stopService(self):
        ## stop window service first
        stopWinService_cmd = "adb -s %s shell service call window 2 i32 %s" %(self.device_name, self.view_server_port)
        out = os.popen(stopWinService_cmd)
        print out.read()
        out.close()
    
    def startService(self):
        ## start window service then
        startWinService_cmd = "adb -s %s shell service call window 1 i32 %s" %(self.device_name, self.view_server_port)
        out = os.popen(startWinService_cmd)
        print out.read()
        out.close()
    
    def initDevice(self):        
        ## set port forwarding
        setPortForwarding_cmd = "adb -s %s forward tcp:%s tcp:%s" %(self.device_name, self.view_server_port, self.view_server_port)
        out = os.popen(setPortForwarding_cmd)
        out.close()    
        return True
    
    def isServiceRunning(self):        
        viewServer_running_flag = "Result: Parcel(00000000 00000001   '........')"
        viewServer_not_running_flag = "Result: Parcel(00000000 00000000   '........')"
        
        check_command = "adb -s %s shell service call window 3 i32 %s" %(self.device_name, self.view_server_port)
        
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
                
            self.initDevice()
            return True
        except Exception, e:
            self.m_logger.error("Faild to open device: [%s]" %str(e))
            return False
        
    def close(self):
        if self.isServiceRunning():
            self.stopService()
            
    def isClosed(self):
        return (not self.isServiceRunning())
    
    
    def getDumpData(self, command="DUMP -1"):
        return self.view_console.getInfosByTelnet(command)
    
    
    
