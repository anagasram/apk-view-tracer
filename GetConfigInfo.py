#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## GetConfigInfo.py

import os
import ConfigParser
from toolkit import getConfDir

class GetViewServerInfo():
    def __init__(self):
        self.ConfigFile = os.path.abspath(getConfDir() + os.sep + "Basic.conf")
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.ConfigFile)
    
    def getServerHost(self):
        return self.config.get("AndroidViewServer", "host")

    def getServerPort(self):
        return self.config.getint("AndroidViewServer", "port")
    
    def getServerTimeOut(self):
        return self.config.getint("AndroidViewServer", "time_out")

