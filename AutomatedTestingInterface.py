#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## AutomatedTestingInterface.py

import os

class AutomatedTestingInterface():
    '''
    Interface for Automated Testing
    '''
    
    ## class variables
    OPENED = None
    CLOSED = None
    DELETE = None
    UP = None
    DOWN = None   
          
    def __init__(self):
        pass
    
    def assertCurrentActivity(self, str_msg, str_name):
        pass
    
    def clearEditText(self, editText):
        pass
    
    def clickInList(self, objList, iIndex):
        pass
    
    def clickLongInList(self, objList, iIndex):
        pass
    
    def clickLongOnScreen(self, fX, fY):
        pass
    
    def clickLongOnText(self, str_text): 
        pass
    
    def clickOnToggleButton(self, str_name):
        pass
    
    def clickOnView(self, objView):
        pass
    
    def drag(self, fromX, fromY, toX, toY, iSteps):
        pass
    
    def enterText(self, str_msg, objText):
        pass
    
    def getCurrentActivity(self):
        pass
    
    def getButton(self):
        pass
    
      
    
    