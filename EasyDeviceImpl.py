#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## EasyDeviceImpl.py

from com.android.monkeyrunner.easy import By, EasyMonkeyDevice
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

class EasyDevice():
    def __init__(self, monkey_runner_impl):
        self.easy_device = EasyMonkeyDevice(monkey_runner_impl.device)
        self.action_type_dict = {"DOWN_AND_UP": MonkeyDevice.DOWN_AND_UP,
                                 "DOWN": MonkeyDevice.DOWN,
                                 "UP": MonkeyDevice.UP}
        
    def getFocusedWindowClassName(self):
        return self.easy_device.getFocusedWindowId()
    
    def getVisiableByID(self, str_id):
        return self.easy_device.visible(By.id("id/"+str_id))
    
    def getLocationByID(self, str_id):
        return self.easy_device.locate(By.id("id/"+str_id))
    
    def touchByID(self, str_id, action_type="DOWN_AND_UP"):
        return self.easy_device.touch(By.id("id/"+str_id), self.action_type_dict[action_type])
    
    
if __name__ == "__main__":
    # testing
    easy_device = EasyDevice(monkey_runner_impl)
    print easy_device.getVisiableByID("del")
    print easy_device.getLocationByID("del")
    print easy_device.touchByID("del")