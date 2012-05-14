#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## IChimpDeviceImpl.py

import os, sys
curDir = os.getcwd()
sys.path.append(curDir)
from com.android.monkeyrunner import MonkeyRunner
from MonkeyRunnerImpl import MonkeyRunnerImpl

class IChimpDevice():
    def __init__(self, monkey_runner_impl):
        self.ichimp_device = monkey_runner_impl.device.getImpl()
        self.action_type_dict = {"DOWN": MonkeyRunner.DOWN,
                                 "UP": MonkeyRunner.UP,
                                 "DOWN_AND_UP": MonkeyRunner.DOWN_AND_UP
                                 }
        
    def installPkg(self, str_package_name):
        return self.ichimp_device.installPackage(str_package_name)
    
    def removePkg(self, str_package_name):
        return self.ichimp_device.removePackage(str_package_name)
        
    def getFocusedWindowClassName(self):
        HV = self.ichimp_device.getHierarchyViewer()
        return HV.getFocusedWindowName()
    
    def press(self, str_key_code, action_type="DOWN_AND_UP"):
        self.ichimp_device.press(str_key_code, self.action_type_dict[action_type])
        
    def touch(self, intX, intY, action_type="DOWN_AND_UP"):
        self.ichimp_device.touch(intX, intY, self.action_type_dict[action_type])
        
    def drag(self, int_fromX, int_fromY, int_toX, int_toY, int_duration, long_steps):
        self.ichimp_device.drag(int_fromX, int_fromY, int_toX, int_toY, int_duration, long_steps)
        
    def typeOnFocusedWindow(self, str_msg):
        self.ichimp_device.type(str_msg)
        
    def shell(self, str_shell_cmd):
        self.ichimp_device.shell(str_shell_cmd)
    
if __name__ == "__main__":
    monkey_runner_impl = MonkeyRunnerImpl()
    ichimp_device = IChimpDevice(monkey_runner_impl)
    ichimp_device.getFocusedWindowClassName()