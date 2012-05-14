#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## EasyDeviceImpl.py


import os, sys
curDir = os.getcwd()
sys.path.append(curDir)
from com.android.monkeyrunner.easy import By, EasyMonkeyDevice
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from MonkeyRunnerImpl import MonkeyRunnerImpl

class EasyDevice():
    def __init__(self, monkey_runner_impl):
        self.easy_device = EasyMonkeyDevice(monkey_runner_impl.device)
        self.action_type_dict = {"DOWN_AND_UP": MonkeyDevice.DOWN_AND_UP,
                                 "DOWN": MonkeyDevice.DOWN,
                                 "UP": MonkeyDevice.UP}
        
    def getFocusedWindowClassName(self):
        return self.easy_device.getFocusedWindowId()
    
    def getVisibleById(self, str_id):
        return self.easy_device.visible(By.id("id/" + str_id))
    
    def getLocationById(self, str_id):
        return self.easy_device.locate(By.id("id/" + str_id))
    
    def getTextById(self, str_id):
        return self.easy_device.getText(By.id("id/" + str_id))
    
    def getElementCenterById(self, str_id):
        return self.easy_device.getElementCenter(By.id("id/" + str_id))
    
    def getExistById(self, str_id):
        return self.easy_device.exists(By.id("id/" + str_id))
            
    def touchById(self, str_id, action_type="DOWN_AND_UP"):
        return self.easy_device.touch(By.id("id/" + str_id), self.action_type_dict[action_type])
    
    def typeInViewById(self, str_id, str_msg):
        self.easy_device.type(By.id("id/" + str_id), str_msg)
        
    
    
if __name__ == "__main__":
    # testing
    monkey_runner_impl = MonkeyRunnerImpl()
    easy_device = EasyDevice(monkey_runner_impl)
    print easy_device.getVisibleById("del")
    print easy_device.getLocationById("del")
    print easy_device.touchById("del")