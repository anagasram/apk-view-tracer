#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ViewClient.py

import telnetlib
import DeviceCommand

class ViewClient():
    '''
    View Client Class which communicate with View Server in Android System
    source code location of view server in Android System
    $android-source/frameworks/base/services/java/com/android/server/wm
    $android-source/frameworks/base/core/java/android/view
    '''
    
    def __init__(self, socket, server_host, server_port):
        self.class_name = "ViewClient"
        self.device_cmd = DeviceCommand.DeviceCommand()
        self.socket = socket    #telnetlib
        self.server_host = "localhost"
        self.server_port = "4939"
    
    def dump_view(self, view_id="-1"):
        return self.device_cmd.dumpInfosByID(view_id)
                
    def list_view(self):
        list_cmd = "LIST"
        return 
    
    def getFocusedWindowInfo(self):
        cmd = "GET_FOCUS"
        return 
    
    def getServerVersion(self):
        pass
    
    def getProtocalVersion(self):
        pass
    
    
if __name__=="__main__":
    view_client = ViewClient()
    
    