#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## AutomatedTestingInterface.py

import os, time, sys

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
    
    Android_Class_Name_Dict = { "Button":  "android.widget.Button",
                                "CheckBox": "android.widget.CheckBox",
                                "EditText" : "android.widget.EditText",
                                "ImageButton": "android.widget.ImageButton",
                                "ImageVIew": "android.widget.ImageView",
                                "RadioButton": "android.widget.RadioButton",
                                "TextView": "android.widget.TextView",
                                "View": "android.view.View"}
          
    def __init__(self):
        self.class_name = "AutomatedTestingInterface"
        # init device 
        if False == init_service():
            print "[%s] Failed to init service of Android View Server!" %(self.class_name)
            raise Exception
        
        # object of DeviceCommand
        self.device_cmd = DeviceCommand()
        
        # object of Monkey Device 
        self.monkey_runner = MonkeyRunnerImpl()
        self.easy_device = EasyDevice()
        
        # View Monitor Object which can control Views
        self.ViewMonitor = None        
        
    def __del__(self):
        # release socket connect with Monkey Server
        del self.monkey_runner           
        # release socket connect with Android View Server
        del self.device_cmd
    
    def close(self):
        pass
    
    def assertCurrentActivity(self, expectedClassName):
        try:
            curActivityClassName = self.easy_device.getFocusedWindowClassName()
            if curActivityClassName == expectedClassName:
                return True
            else:
                return False
        except Exception, e:
            print "[%s] Failed to assert current activity [%s]" %(self.class_name, str(e))
            return None
        
    def assertCurrentActivityNewInstance(self, expectedClassName, oldHashCode):
        try:
            curActivityClassName = self.easy_device.getFocusedWindowClassName()
            curActivityHashCode = self.device_cmd.getFocusViewHashCode()
            if (curActivityClassName == expectedClassName) and (curActivityHashCode != oldHashCode):
                return True
            else:
                return False
        except Exception, e:
            print "[%s] Failed to assert current activity new instance [%s]" %(self.class_name, str(e))
            return None
    
    def clearEditTextById(self, EditTextId):
        try:
            self.easy_device.typeInViewById(EidtTextId, "")
            return True
        except Exception, e:
            print "[%s] Failed to click edit text by id [%s]" %(self.class_name, str(e))
            return False
    
    def clickOnScreen(self, x, y):
        try:
            self.monkey_runner.touch(x, y, "DOWN_AND_UP")
            return True
        except Exception, e:
            print "[%s] Failed to click on screen [%s]" %(self.class_name, str(e))
            return False
    
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
    
    def clickOnViewById(self, view_id):
        try:
            self.easy_device.touchById(view_id)
            return True
        except Exception, e:
            print "[%s] Failed to click on view by id [%s]" %(self.class_name, str(e))
            return False
    
    def clickOnViewByLocation(self, x, y):
        try:
            self.monkey_runner.touch(x, y, "DOWN_AND_UP")
            return True
        except Exception, e:
            print "[%s] Failed to click on view by location [%s]" %(self.class_name, str(e))
            return False
    
    # could not implement now
    # it's a problem
    def drag(self, fromX, fromY, toX, toY, iSteps):
        pass
    
    def enterText(self, str_msg, objText):
        try:
            self.monkey_runner.typeText(str_msg)
            return True
        except Exception, e:
            print "[%s] Failed to enter text [%s]" %(self.class_name, str(e))
            return False
    
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
    
    def getViewClassName(self):
        pass
    
    def getViews(self):
        pass
    
    def getText(self):
        pass
    
    def goBack(self):
        try:
            self.monkey_runner.clickBackButton()
            return True
        except Exception, e:
            print e
            return False
    
    def goBackToView(self, view_name):
        pass
    
    def goBackToActivity(self, activity_name):
        pass        
        
    def findButton(self, text, onlyVisible=True):
        pass
    
    def findEditText(self, text):
        pass
    
    def findText(self, text, onlyVisible=True):
        pass
    
    def findToggleButtonById(self):
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
        try:
            self.monkey_runner.sleep(sec)
            return True
        except Exception, e:
            print e
            return False
    
    ## not implement yet    
    def waitForText(self, str_text, time_out_sec):
        if isinstance(str_text, str):
            raise Exception
        if isinstance(time_out_sec, int):
            raise Exception
        now_time = time.time()
        end_time = now_time + time_out_sec
        while ((?) and (now_time < end_time)):
            now_time = time.time()
        
        if (now_time < end_time):
            return True
        else:
            return False
            
        
    def waitForView(self, view_class_name, time_out_sec):
        if not isinstance(view_class_name, str):
            raise Exception
        if not isinstance(time_out_sec, int):
            raise Exception
        now_time = time.time()
        end_time = now_time + time_out_sec
        while ((self.easy_device.getFocusedWindowClassName() != view_class_name) and (now_time < end_time)):
            now_time = time.time()
            
        if (now_time < end_time):
            return True
        else:
            return False
        
if __name__=="__main__":
    print "test OK"
            
        
        
    
