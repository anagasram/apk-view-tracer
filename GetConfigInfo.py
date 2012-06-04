#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## GetConfigInfo.py

import os
import ConfigParser
from toolkit import getConfDir

class ConfigGetter():
    '''
    ConfigGetter Class can get configuration info from configure files
    '''
    
    __ClassName = "ConfigGetter" # class private variable
    
    def __init__(self):
        self.ConfigFilePath = os.path.abspath(getConfDir() + os.path.sep + "Basic.conf")
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.ConfigFilePath)
        
    def getConfigInfo(self, section, option):
        return self.config.get(section, option)
    
    def getServerHost(self):
        return self.config.get("AndroidViewServer", "host")

    def getServerPort(self):
        return self.config.getint("AndroidViewServer", "port")
    
    def getServerTimeOut(self):
        return self.config.getint("AndroidViewServer", "time_out")

