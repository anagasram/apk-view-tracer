#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## SoloInterface.py

import logging, time
import Logger
from DeviceManagement.Device import Device
from ViewManagement.ViewTree import ViewTree
from ViewController.EventController import EventController
from cookielib import reach
from tarfile import LENGTH_LINK

class SoloInterface():
    '''
    Solo Interface for Automated Testing
    '''
        
    Android_Class_Name_Dict = { "Button":  "android.widget.Button",
                                "CheckBox": "android.widget.CheckBox",
                                "EditText" : "android.widget.EditText",
                                "ImageButton": "android.widget.ImageButton",
                                "ImageVIew": "android.widget.ImageView",
                                "RadioButton": "android.widget.RadioButton",
                                "TextView": "android.widget.TextView",
                                "View": "android.view.View"}
          
    def __init__(self, device_name="emulator-5554", device_port=5554, device_address="127.0.0.1"):
        self.class_name = "SoloInterface"
        self.m_logger = Logger.InitLog("solo-interface.log", logging.getLogger("solo-interface.thread"))
        
        self.device_name = device_name
        self.device_port = device_port
        self.device_address = device_address
        
        # object of Device
        self.device = Device(self.m_logger, self.device_name)        
        # init device
        self.device.open()
        
        # build View Tree
        self.vt = ViewTree(self.m_logger)
        
        # object of View Controller 
        self.event_controller = EventController(self.m_logger)
        # init event controller
        self.event_controller.open()
    
    def setUp(self):
        data = self.device.getDumpData()
        # key point        
        self.tree_nodes_list = vt.build(data)
        
        
    def tearDown(self):
        pass    

    def close(self):
        # release socket connect with Monkey Server
        self.event_controller.close()       
        # release socket connect with Android View Server
        self.device.close()
        
#------------------------------------------------------------------------------ 
    def searchForViewClassName(self, class_name):
        for node in self.tree_nodes_list:
            if class_name == node.mClassName:
                return node
            
        return None
    
    def searchForText(self, text):
        for node in self.tree_nodes_list:
            if text == node.mText:
                return node
        
        return True
    
    def searchForViewID(self, id):
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return node
            
        return None
    
    def getCurrentViewClassName(self):
        return self.device.view_console.getFocusViewClassName()
    
    def existViewByClassName(self, class_name):
        for node in self.tree_nodes_list:
            if class_name == node.mClassName:
                return True
            
        return False
    
    def existViewByText(self, text):
        for node in self.tree_nodes_list:
            if text == node.mText:
                return True
            
        return False
    
    def existViewById(self, id):
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return True
        
        return False
    
    def isVisibleById(self, id):
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return node.mVisible
            
        return False
    
    
    def clickViewById(self, id):
        if 0==len(id):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return self.event_controller.tap(node.mLocation.x, node.mLocation.y)
            
        return False
    
    def clickViewByText(self, text):
        if 0==len(text):
            return False
        
        for node in self.tree_nodes_list:
            if text == node.mText:
                return self.event_controller.tap(node.mLocation.x, node.mLocation.y)
            
    def getTextById(self, id):
        if 0==len(id):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return node.mText
            
        return None
    
    
    def clearEditTextById(self, id):
        if 0==len(id):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                length = len(node.mText)
                while 0<length:
                    self.event_controller.press("del")
                    length-=1
            
        return False
    
    def setEditTextById(self, id, text):
        if 0==len(id) or 0==len(text):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                length = len(node.mText)
                while 0<length:
                    self.event_controller.press("del")
                    length-=1
                                
                return self.event_controller.type(text)
            
        return False
    
    def appendEditTextById(self, id, text):
        if 0==len(id) or 0==len(text):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return self.event_controller.type(text)
            
#------------------------------------------------------------------------------ 
# Physical Button Operations
    def longPressHome(self):
        return self.event_controller.longPressByKeyCode("home")
    
    def callMenu(self):
        return self.event_controller.press("menu")
    
    def goBack(self):
        return self.event_controller.press("back")
    
    def callDelete(self):
        return self.event_controller.press("del")
    
    def callLeft(self):
        return self.event_controller.press("dpad_left")
    
    def callRight(self):
        return self.event_controller.press("dpad_right")
    
    def callTop(self):
        return self.event_controller.press("dpad_top")
    
    def callDown(self):
        return self.event_controller.press("dpad_down")
    
    def callNotification(self):
        return self.event_controller.drag(100, 20, 100, 500)    
    
##------------------------------------------------------------------------------ 
#    def assertCurrentActivity(self, expectedClassName):
#        try:
#            curActivityClassName = self.getCurrentViewClassName()
#            if curActivityClassName == expectedClassName:
#                return True
#            else:
#                return False
#        except Exception, e:
#            msg = "[%s] Failed to assert current activity [%s]" %(self.class_name, str(e))
#            self.m_logger.error(msg)
#            return None
#        
#    def assertCurrentActivityNewInstance(self, expectedClassName, oldHashCode):
#        try:
#            curActivityClassName = self.getCurrentViewClassName()
#            curActivityHashCode = self.device.view_console.getFocusViewHashCode()
#            if (curActivityClassName == expectedClassName) and (curActivityHashCode != oldHashCode):
#                return True
#            else:
#                return False
#        except Exception, e:
#            msg = "[%s] Failed to assert current activity new instance [%s]" %(self.class_name, str(e))
#            self.m_logger.error(msg)
#            return None
#    
#    def clickInList(self, objList, iIndex):
#        pass
#    
#    def clickLongInList(self, objList, iIndex):
#        pass
#    
#    def longClickByText(self, str_text): 
#        pass
#    
#    def clickOnToggleButton(self, str_name):
#        pass
#    
#    def clickOnViewById(self, view_id):
#        try:
#            self.easy_device.touchById(view_id)
#            return True
#        except Exception, e:
#            print "[%s] Failed to click on view by id [%s]" %(self.class_name, str(e))
#            return False
#    
#    def clickOnViewByLocation(self, x, y):
#        try:
#            self.monkey_runner.touch(x, y, "DOWN_AND_UP")
#            return True
#        except Exception, e:
#            print "[%s] Failed to click on view by location [%s]" %(self.class_name, str(e))
#            return False
#    
#    def drag(self, fromX, fromY, toX, toY, iSteps):
#        pass
#    
#    def enterText(self, str_msg, objText):
#        try:
#            self.monkey_runner.typeText(str_msg)
#            return True
#        except Exception, e:
#            print "[%s] Failed to enter text [%s]" %(self.class_name, str(e))
#            return False
#    
#
#    
#    def getCurrentActivity(self):
#        pass
#    
#    def isCheckBoxChecked(self, param):
#        if isinstance(param, int):
#            index = param
#        elif isinstance(param, str):
#            text = param
#        else:
#            pass
#        
#    def isRadioButtonChecked(self, param):
#        if isinstance(param, int):
#            index = param
#        elif isinstance(param, str):
#            text = param
#        else:
#            pass
#        
#    def isSpinnerTextSelected(self, param):
#        if isinstance(param, int):
#            index = param
#        elif isinstance(param, str):
#            text = param
#        else:
#            pass
#    
#    def isToggleButtonChecked(self, param):
#        if isinstance(param, int):
#            index = param
#        elif isinstance(param, str):
#            text = param
#        else:
#            pass
#        
#    def pressMenuItem(self):
#        pass
#    
#    def pressSpinnerItem(self):
#        pass
#    
#    def scrollDown(self):
#        pass
#    
#    def scrollDownList(self):
#        pass
#    
#    def scrollToSide(self):
#        pass
#    
#    def scrollUp(self):
#        pass
#    
#    def scrollUpList(self):
#        pass
    
           
if __name__=="__main__":
    print "test OK"
            
        
        
    
