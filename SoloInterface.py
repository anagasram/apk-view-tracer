#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## SoloInterface.py

import logging, time
import Logger
from DeviceManagement.Device import Device
from ViewManagement.ViewTree import ViewTree
from ViewManagement import ParseElement
from ViewController.EventController import EventController
from SystemComponent import Notification, ProgressBar, GroupView, PopupView

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
                                "View": "android.view.View",
                                "ProgressBar": "android.widget.ProgressBar",
                                "ScrollView": "android.widget.ScrollView"}
          
    def __init__(self, device_name="emulator-5554", device_port=5554, device_address="127.0.0.1"):
        '''
        Constructor
        '''
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
        
        self.tree_nodes_list = None
        
        # object of View Controller 
        self.event_controller = EventController(self.m_logger, self.device_name)
        # init event controller
        self.event_controller.open()
        
        self.device_display_width = int(self.event_controller.getDisplayWidth())
        self.device_display_height = int(self.event_controller.getDisplayHeight())
        # to 480*800 display
        # Notification (y: 0-37  / x: 8-471 )
        self.notification_height = 37
    
    def setUp(self):
        data = self.device.getDumpData()
        # key point
        if None!=self.tree_nodes_list and 0!=len(self.tree_nodes_list):
            del self.tree_nodes_list     
        self.tree_nodes_list = self.vt.build(data)        
        
    def tearDown(self):
        # do nothing
        pass

    def close(self):
        # release socket connect with Monkey Server
        self.event_controller.close()       
        # release socket connect with Android View Server
        self.device.close()
        
        
#'''adb shell command'''------------------------------------------------------------------------------ 

    def installPackage(self, package_name):
        return self.device.adb_console.installPkg(package_name)
    
    def removePackage(self, package_name):
        return self.device.adb_console.removePkg(package_name)
    
    def shell(self, command):
        return self.device.adb_console.shell(command)
    
    def shellForResult(self, command):
        return self.device.adb_console.shell(command, True)
    
    def startActivity(self, uri=None, action=None, data=None, mimetype=None, categories_list=None, component=None, flags_list=None, extras_list=None):
        self.device.adb_console.startActivity(uri, action, data, mimetype, categories_list, component, flags_list, extras_list)            
        time.sleep(1)
        self.setUp()
        
    def pushFile(self, local_path, device_path):
        return self.device.adb_console.pushFile(local_path, device_path)
    
    def pullFile(self, device_path, local_path):
        return self.device.adb_console.pullFile(device_path, local_path)

#Basic Operation------------------------------------------------------------------------------ 
    def searchForViewClassName(self, class_name):
        for node in self.tree_nodes_list:
            if class_name == node.mClassName:
                return True
            
        return False
    
    def searchForText(self, text, partial_matching=True):
        if partial_matching:
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (node.mText.find(text)>=0):
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to find sub string: [%s] " %e)
                    continue
        else:            
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (text == node.mText):
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to match string: [%s] " %e)
                    continue        
        return False
    
    def searchForViewID(self, id):
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return True            
        return False
    
    def getCurrentViewClassName(self):
        return self.device.view_console.getFocusViewClassName()
    
    def existViewByClassName(self, class_name):
        for node in self.tree_nodes_list:
            if class_name == node.mClassName:
                return True            
        return False
    
    def existViewByText(self, text, partial_matching=True):
        if partial_matching:
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (node.mText.find(text)>=0):
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to find sub string: [%s] " %e)
                    continue
        else:
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (text == node.mText):
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to match string: [%s] " %e)
                    continue
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
    
    
    def clickViewById(self, id, ReDump=True):
        if 0==len(id):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                self.event_controller.tap(node.mLocation.x, node.mLocation.y)
                if ReDump:
                    time.sleep(2)
                    self.setUp()
                return True
            
        return False
    
    def clickViewByText(self, text, partial_matching=True):
        if 0==len(text):
            return False
        
        if partial_matching:
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (node.mText.find(text)>=0):
                        self.event_controller.tap(node.mLocation.x, node.mLocation.y)
                        self.setUp()
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to find sub string: [%s] " %e)
                    continue
        else:
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (text == node.mText):
                        self.event_controller.tap(node.mLocation.x, node.mLocation.y)
                        self.setUp()
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to match string: [%s] " %e)
                    continue
            
        return False
            
    def getTextById(self, id):
        if 0==len(id):
            return None
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                return node.mText
            
        return None
    
    
    def clearEditTextById(self, id):
        if 0==len(id):
            return False
        
        # make the cursor can focus at this edit text
        self.clickViewById(id, False)
        self.goBack(False)
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                length = len(node.mText)
                while 0<length:
                    self.event_controller.press("del")
                    length-=1
                
                self.setUp()
                return True
            
        return False
    
    def setEditTextById(self, id, text):
        if 0==len(id) or 0==len(text):
            return False
        
        # make the cursor can focus at this edit text
        self.clickViewById(id, False)
        self.goBack(False)
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                length = len(node.mText)
                while 0<length:
                    self.event_controller.press("del")
                    length-=1
                                
                self.event_controller.type(text)
                self.setUp()
                return True
            
        return False
    
    def appendEditTextById(self, id, text):
        if 0==len(id) or 0==len(text):
            return False
        
        # make the cursor can focus at this edit text
        self.clickViewById(id, False)
        self.goBack(False)
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                self.event_controller.type(text)
                self.setUp()
                return True
        
        return False
    
    '''
    this method for simple Checkbox or RadioButton
    android.widget.RadioButton
    android.widget.CheckBox
    '''
    def isCheckedById(self, id):
        view_name_list = ["android.widget.RadioButton", "android.widget.CheckBox"]
        if 0==len(id):
            return False
        
        real_id = "id/"+id
        for node in self.tree_nodes_list:
            if self.isViewType(node.mClassName, view_name_list) and (real_id==node.mId):
                element_parser = ParseElement.ParseElement(node.mElement)
                element_parser.parseElmentData() 
                return element_parser.getBoolean("isChecked()", False)
        
        return False
    
    def isCheckedByText(self, text, partial_matching=True):
        view_name_list = ["android.widget.RadioButton", "android.widget.CheckBox"]
        if 0==len(text):
            return False
        
        if partial_matching:
            for node in self.tree_nodes_list:
                try:
                    if self.isViewType(node.mClassName, view_name_list) and (node.mText != None) and (node.mText.find(text)>=0):
                        element_parser = ParseElement.ParseElement(node.mElement)
                        element_parser.parseElmentData()
                        return element_parser.getBoolean("isChecked()", False)
                except Exception, e:
                    self.m_logger.error("Current text fail to find sub string: [%s] " %e)
                    continue
        else:
            for node in self.tree_nodes_list:
                try:
                    if self.isViewType(node.mClassName, view_name_list) and (node.mText != None) and (text==node.mText):
                        element_parser = ParseElement.ParseElement(node.mElement)
                        element_parser.parseElmentData() 
                        return element_parser.getBoolean("isChecked()", False)
                except Exception, e:
                    self.m_logger.error("Current text fail to match string: [%s] " %e)
                    continue
        return False

#internal interface------------------------------------------------------------------------------ 
    '''
    judge whether class name belongs to view_name_list
    @param param: node.mClassName
                 list of views name
    @return: True or False
    '''
    def isViewType(self, class_name, view_name_list):
        for name in view_name_list:
            if name == class_name:
                return True
        return False
    
#Physical Button Operations------------------------------------------------------------------------------ 

    def longPressHome(self):
        self.event_controller.longPressByKeyCode("home")
        self.setUp()
        return True
    
    def pressHome(self):
        self.event_controller.press("home")
        self.setUp()
        return True
    
    def callMenu(self):
        self.event_controller.press("menu")
        self.setUp()
        return True
    
    def goBack(self, ReDump=True):
        self.event_controller.press("back")
        if ReDump:
            self.setUp()
        return True
    
    def callDelete(self, reDump=False):
        self.event_controller.press("del")
        if reDump:
            self.setUp()
    
    def callLeft(self, reDump=False):
        self.event_controller.press("dpad_left")
        if reDump:
            self.setUp()
    
    def callRight(self, reDump=False):
        self.event_controller.press("dpad_right")
        if reDump:
            self.setUp()
    
    def callUp(self, reDump=False):
        self.event_controller.press("dpad_up")
        if reDump:
            self.setUp()
    
    def callDown(self, reDump=False):
        self.event_controller.press("dpad_down")
        if reDump:
            self.setUp()

#Operation with Notification------------------------------------------------------------------------------ 
    def callNotification(self):
        self.event_controller.drag(100, 20, 100, 500)
        self.setUp()
        return True
    
    def clearAllNotifications(self, reDump=False):
        notifies = Notification.Notification(self.tree_nodes_list)
        location = notifies.getClearButtonLocation()
        self.event_controller.tap(location.x, location.y)
        if reDump:
            self.setUp()        
        return True
    
    def clickNotificationItemByText(self, text, partial_matching=True):
        if 0==len(text):
            return False
        
        notifies = Notification.Notification(self.tree_nodes_list)
        notifies.loadAllItems()
        
        if partial_matching:            
            location = notifies.getLocationByKeyWord(text)
        else:
            location = notifies.getLocationByText(text)
            
        self.event_controller.tap(location.x, location.y)
        self.setUp()
        return True       

#Operation with ProgressBar------------------------------------------------------------------------------  
    def getCurrentProgress(self):
        progress_bar = ProgressBar.ProgressBar(self.tree_nodes_list)
        return progress_bar.getCurrentProgress()
   
    def getProgressById(self, id):
        progress_bar = ProgressBar.ProgressBar(self.tree_nodes_list)
        return progress_bar.getProgressById(id)
    
    def getProgressByText(self, text, partial_matching=True):
        progress_bar = ProgressBar.ProgressBar(self.tree_nodes_list)
        if partial_matching:
            return progress_bar.getProgressByKeyWord(text)
        else:
            return progress_bar.getProgressByText(text)
    
#------------------------------------------------------------------------------ 
    def assertCurrentActivity(self, expectedClassName):
        try:
            curActivityClassName = self.getCurrentViewClassName()
            if curActivityClassName == expectedClassName:
                return True
            else:
                return False
        except Exception, e:
            msg = "[%s] Failed to assert current activity [%s]" %(self.class_name, str(e))
            self.m_logger.error(msg)
            return None
        
    def assertCurrentActivityNewInstance(self, expectedClassName, oldHashCode):
        try:
            curActivityClassName = self.getCurrentViewClassName()
            curActivityHashCode = self.device.view_console.getFocusViewHashCode()
            if (curActivityClassName == expectedClassName) and (curActivityHashCode != oldHashCode):
                return True
            else:
                return False
        except Exception, e:
            msg = "[%s] Failed to assert current activity new instance [%s]" %(self.class_name, str(e))
            self.m_logger.error(msg)
            return None
   
    def longPressByText(self, text, partial_matching=True):
        if 0==len(text):
            return False
        
        if partial_matching: 
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (node.mText.find(text)>=0):
                        location = node.mLocation
                        self.event_controller.longPressByLocation(location.x, location.y) 
                        time.sleep(1)       
                        self.setUp()
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to find sub string: [%s] " %e)
                    continue
        else:
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (text == node.mText):
                        location = node.mLocation
                        self.event_controller.longPressByLocation(location.x, location.y)   
                        time.sleep(1)     
                        self.setUp()
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to match string: [%s] " %e)
                    continue       
        return False

#Operation with View Group such as ListView, ScrollView, GridView, etc.------------------------------------------------------------------------------ 
    def getItemsNumber(self, groupview_id, groupview_classname=None):
        if None==groupview_id or 0==len(groupview_id):
            return None
        
        real_id = "id/" + groupview_id
        for node in self.tree_nodes_list:
            if real_id==node.mId:
                if None!=groupview_classname and 0!=len(groupview_classname):
                    if groupview_classname==node.mClassName:
                        return len(node.mChildNodes)
                else:
                    return len(node.mChildNodes)
            
        return None
            

    def clickItemByIndex(self, groupview_id, index=0):
        if None==groupview_id or 0==len(groupview_id):
            return False
        
        if None==index or (not isinstance(index, int)):
            return False
        
        real_id = "id/" + groupview_id
        for node in self.tree_nodes_list:
            if real_id==node.mId:
                groupview = GroupView.GroupView(node)
                groupview.loadAllItems()
                item = groupview.items_list[index]
                break
        
        for location in item.properties_dict["mLocation"]:
            if self.event_controller.tap(location.x, location.y):
                self.setUp()
                return True
            
        return False
    
    def clickItemByText(self, groupview_id, text, partial_matching=True):
        if None==groupview_id or 0==len(groupview_id):
            return False
        
        if None==text or 0==len(text):
            return False
        
        groupview = None
        real_id = "id/" + groupview_id
        for node in self.tree_nodes_list:
            if real_id==node.mId:
                groupview = GroupView.GroupView(node)
                groupview.loadAllItems()
                break
                
        if not partial_matching:
            for item in groupview.items_list:
                if text in item.properties_dict["mText"]:
                    # click this item
                    for location in item.properties_dict["mLocation"]:
                        if self.event_controller.tap(location.x, location.y):
                            self.setUp()
                            return True
        else:
            for item in groupview.items_list:                
                for msg in item.properties_dict["mText"]:
                    try:
                        if (None!=msg) and (msg.find(text)>=0):
                            # click this item
                            for location in item.properties_dict["mLocation"]:
                                if self.event_controller.tap(location.x, location.y):
                                    self.setUp()
                                    return True
                    except Exception, e:
                        self.m_logger.error("Current text fail to match string: [%s] " %e)
                        continue  
                              
        return False
    
    def isItemCheckedByIndex(self, groupview_id, index=0):
        if None==groupview_id or 0==len(groupview_id):
            return False
        
        if None==index or 0==len(index):
            return False
        
        real_id = "id/" + groupview_id
        for node in self.tree_nodes_list:
            if real_id==node.mId:
                groupview = GroupView.GroupView(node)
                groupview.loadAllItems()
                item = groupview.items_list[index]
                break
            
        return item.properties["isChecked"]
    
    def isItemCheckedByText(self, groupview_id, text, partial_matching=True):
        if None==groupview_id or 0==len(groupview_id):
            return False
        
        if None==text or 0==len(text):
            return False
        
        groupview = None
        real_id = "id/" + groupview_id
        for node in self.tree_nodes_list:
            if real_id==node.mId:
                groupview = GroupView.GroupView(node)
                groupview.loadAllItems()
                break
            
        if not partial_matching:
            for item in groupview.items_list:
                if text in item.properties_dict["mText"]:
                    return item.properties_dict["isChecked"]
        else:
            for item in groupview.items_list:
                for msg in item.properties_dict["mText"]:
                    try:
                        if (None!=msg) and (msg.find(text)>=0):
                            return item.properties_dict["isChecked"]
                    except Exception, e:
                        self.m_logger.error("Current text fail to match string: [%s] " %e)
                        continue
                                        
        return False            

#Popup View Operations------------------------------------------------------------------------------ 
    def typeInPopupByIndex(self, text, index=0):
        if None == text or 0 == len(text):
            return False
             
        if None==index:
            return False
        
        popup = PopupView.PopupView(self.tree_nodes_list, self.event_controller, self.device_display_width, self.device_display_height)
        popup.loadProperties()
        if popup.typeTextByIndex(text, index):
            time.sleep(1)
            self.setUp()
            return True
        
        return False
           
    def clickInPopupById(self, id):
        if None == id or 0==len(id):
            return False
        
        popup = PopupView.PopupView(self.tree_nodes_list, self.event_controller, self.device_display_width, self.device_display_height)
        popup.loadProperties()
        if popup.clickViewById(id):
            time.sleep(1)
            self.setUp()
            return True
        else:
            return False
    
    def clickInPopupByText(self, text, partial_matching=True):
        if None == text or 0 == len(text):
            return False
        
        popup = PopupView.PopupView(self.tree_nodes_list, self.event_controller, self.device_display_width, self.device_display_height)
        popup.loadProperties()
        if popup.clickViewByText(text, partial_matching):
            time.sleep(1)
            self.setUp()
            return True
        else:
            return False
        
    def selectInVerticalPopupByText(self, text, partial_matching=True):
        if None == text or 0 == len(text):
            return False
        
        popup = PopupView.PopupView(self.tree_nodes_list, self.event_controller, self.device_display_width, self.device_display_height)
        popup.loadProperties()
        
        if popup.focusViewByText(text, partial_matching, first_direction="dpad_down"):
            if self.event_controller.press("enter"):
                time.sleep(1)
                self.setUp()
                return True 

    def selectInHorizontalPopupByText(self, text, partial_matching=True):
        if None == text or 0 == len(text):
            return False
        
        popup = PopupView.PopupView(self.tree_nodes_list, self.event_controller, self.device_display_width, self.device_display_height)
        popup.loadProperties()
        
        if popup.focusViewByText(text, partial_matching, first_direction="dpad_right"):
            if self.event_controller.press("enter"):
                time.sleep(1)
                self.setUp()
                return True 
        

    
#Menu Item Operation------------------------------------------------------------------------------
    def clickMenuItemById(self, id):
        if 0==len(id):
            return False
        
        real_id = "id/"+id
        view_height = self.tree_nodes_list[0].mAbsoluteRect.mBottom - self.tree_nodes_list[0].mAbsoluteRect.mTop
        for node in self.tree_nodes_list:
            if real_id == node.mId:
                realX = node.mLocation.x                
                realY = (self.device_display_height - view_height) + node.mLocation.y
                self.m_logger.info("realX: %s   realY: %s" %(realX, realY))
                self.event_controller.tap(realX, realY)

                time.sleep(1)
                self.setUp()
                return True
            
        return False
    
    def clickMenuItemByText(self, text, partial_matching=True): 
        if 0==len(text):
            return False
        
        if partial_matching:
            view_height = self.tree_nodes_list[0].mAbsoluteRect.mBottom - self.tree_nodes_list[0].mAbsoluteRect.mTop
            for node in self.tree_nodes_list:
                try:
                    if (node.mText != None) and (node.mText.find(text)>=0):
                        realX = node.mLocation.x
                        realY = (self.device_display_height - view_height) + node.mLocation.y
                        self.m_logger.info("realX: %s   realY: %s" %(realX, realY))
                        self.event_controller.tap(realX, realY)
                        
                        time.sleep(1)
                        self.setUp()
                        return True
                except Exception, e:
                    self.m_logger.error("Current text fail to match string: [%s] " %e)
                    continue
        else:
            view_height = self.tree_nodes_list[0].mAbsoluteRect.mBottom - self.tree_nodes_list[0].mAbsoluteRect.mTop
            for node in self.tree_nodes_list:
                if (node.mText != None) and (text == node.mText):
                    realX = node.mLocation.x
                    realY = (self.device_display_height - view_height) + node.mLocation.y
                    self.m_logger.info("realX: %s   realY: %s" %(realX, realY))
                    self.event_controller.tap(realX, realY)
                    
                    time.sleep(1)
                    self.setUp()
                    return True
            
        return False

#Scroll Operation------------------------------------------------------------------------------ 
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
    solo = SoloInterface(device_name="016eb881")
    solo.setUp()

#------------------------------------------------------------------------------ 
#    solo.clickViewById("btn_signin")
#    for node in solo.tree_nodes_list:
#        print node.mId
#        print node.mText
#        print "----------------"
#    solo.setEditTextById("account", "mk@126.com")
#    solo.setEditTextById("password", "11111111")
#    solo.clickViewById("cb_eula")
#    solo.clickViewById("sign_in")
#------------------------------------------------------------------------------ 
    
#    solo.event_controller.touchDown(300, 600)
#    solo.event_controller.touchMove(300, 600)
#    solo.event_controller.touchMove(300, 400)
#    solo.event_controller.touchMove(300, 200)
#    solo.event_controller.touchUp(300, 200)   
    
#    solo.event_controller.drag(300, 600, 300, 200)
#    
#    solo.setUp()
#    
#    solo.clickViewByText("Scan Now", True)
#------------------------------------------------------------------------------ 

#    solo.clickViewByText("Mobile Security")

#------------------------------------------------------------------------------
#    solo.event_controller.press("dpad_down")
#    
#    time.sleep(2)
#    solo.event_controller.press("dpad_down")
#
#    time.sleep(2)
#    solo.event_controller.press("dpad_down")
#    
#    solo.event_controller.press("enter")
#------------------------------------------------------------------------------ 
#    solo.clickItemInVerticalPopupByIndex(2)

#------------------------------------------------------------------------------ 
#    solo.clickMenuItemByText("More")
#------------------------------------------------------------------------------ 

#    solo.callMenu()
#    solo.clickMenuItemByText("Add")
#    solo.typeInPopupByIndex("renren", 0)
#    solo.typeInPopupByIndex("http://www.renren.com", 1)
#    solo.clickInPopupByText("Save", False)
#    
#    solo.longPressByText("renren", False)
#    solo.clickInPopupByText("Delete", False)
#------------------------------------------------------------------------------ 
    


    solo.clickItemByIndex("phone_malware_list", 0)  #scan_result_installmal
    solo.clickViewById("cancel_button")
    solo.clickItemByText("phone_malware_list", "Threat", True)

    
    solo.close()
    print"success to end"
        
        
    
