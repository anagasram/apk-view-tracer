#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## GetConfigInfo.py

import os
import ConfigParser
from Utility import getConfDir

class ConfigGetter():
    '''
    ConfigGetter Class can get configuration info from configure files
    '''
    
    __ClassName = "ConfigGetter" # class private variable
    
    def __init__(self):

        self.ConfigFilePath = os.path.abspath(getConfDir() + os.path.sep + "Basic.conf")
        self.config = ConfigParser.ConfigParser()
        try:
            self.config.read(self.ConfigFilePath)
        except Exception, e:
            print "[%s] Failed to read configuration file: [%s]" %(ConfigGetter.__ClassName, str(e))
        
    def getConfigInfo(self, section, option):
        return self.config.get(section, option)
    
    def getServerTimeOut(self):
        return self.config.getint("AndroidViewServer", "time_out")

