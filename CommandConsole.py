#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## CommandConsole.py

import os

class CommandConsole():
    def __init__(self):
        self.startActivityCmd = ""
        self.sendIntentCmd = ""
        
    def installPkg(self):
        pass
    
    def removePkg(self):
        pass
    
    def startActivity(self):
        try:
            os.system(self.startActivityCmd)
            return True
        except Exception,e:
            print e
            return False
        
    def sendIntent(self):
        try:
            os.system(self.sendIntentCmd)
            return True
        except Exception,e:
            print e
            return False
        
    def phoneCall(self):
        pass
    
    def sendSMS(self):
        pass
    
    def browseWebPage(self):
        pass
    
    