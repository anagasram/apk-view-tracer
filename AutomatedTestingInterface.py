#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## AutomatedTestingInterface.py

import os
from InitDevice import init_service
from DeviceCommand import DeviceCommand
from MonkeyRunnerImpl import MonkeyRunnerImpl
from HierarchyViewerImpl import HierarchyViewer
from EasyDeviceImpl import EasyDevice
from IChimpDeviceImpl import IChimpDevice

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
        # init device 
        if False == init_service():
            print "Failed to init service of Android View Server!"
            raise Exception
        
        # object of DeviceCommand
        self.device_cmd = DeviceCommand()
        
        # object of Monkey Device 
        self.monkey_runner = MonkeyRunnerImpl()
        
        # View Monitor Object which can control Views
        self.ViewMonitor = None
        
    def __del__(self):
        # release socket connect with Monkey Server
        del self.monkey_runner           
        # release socket connect with Android View Server
        del self.device_cmd
    
    def close(self):
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
    
    def clickOnViewByLocation(self, x, y):
        self.monkey_runner.touch(x, y, "DOWN_AND_UP")
    
    def drag(self, fromX, fromY, toX, toY, iSteps):
        pass
    
    def enterText(self, str_msg, objText):
        self.monkey_runner.typeText(str_msg)
    
    def getViewMonitor(self):
        return self.ViewMonitor
    
    def getCurrentActivity(self):
        pass
    
    def getButton(self):
        pass
    
    def getEditText(self):
        pass
    
    def getImage(self):
        pass
    
    def getImageButton(self):
        pass
    
    def getView(self):
        pass
    
    def getViews(self):
        pass
    
    def getText(self):
        pass
    
    def goBack(self):
        pass
    
    def goBackToView(self, view_name):
        pass
    
    def findButton(self, text, onlyVisible=True):
        pass
    
    def findEditText(self, text):
        pass
    
    def findText(self, text, onlyVisible=True):
        pass
    
    def findToggleButton(self):
        pass
    
    def isCheckBoxChecked(self, param):
        if isinstance(param, int):
            index = param
        elif isinstance(param, str):
            text = param
        else:
            pass
        
    def isRadioButtonChecked(self, param):
        if isinstance(param, int):
            index = param
        elif isinstance(param, str):
            text = param
        else:
            pass
        
    def isSpinnerTextSelected(self, param):
        if isinstance(param, int):
            index = param
        elif isinstance(param, str):
            text = param
        else:
            pass
        
    def isTextChecked(self, str_text):
        pass
    
    def isToggleButtonChecked(self, param):
        if isinstance(param, int):
            index = param
        elif isinstance(param, str):
            text = param
        else:
            pass
        
    def pressMenuItem(self):
        pass
    
    def pressSpinnerItem(self):
        pass
    
    def scrollDown(self):
        pass
    
    def scrollDownList(self):
        pass
    
    def scrollToSide(self):
        pass
    
    def scrollUp(self):
        pass
    
    def scrollUpList(self):
        pass   
    
    def sleep(self, sec):
        pass
    