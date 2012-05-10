#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## MonkeyRunnerImpl.py

## run mode
## java -jar $(jython.jar file path) $(python script file)

## adb shell monkey <...>

## start monkey server
## adb forward tcp:1080 tcp:1080
## adb shell monkey --port 1080

import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import By, EasyMonkeyDevice 
from com.android.monkeyrunner.recorder import MonkeyRecorder

class MonkeyRunnerImpl():
    def __init__(self, serial=None):
        ## command map
        self.CMD_MAP = {"TOUCH": lambda dev, arg: dev.touch(**arg),
                        "DRAG": lambda dev, arg: dev.drag(**arg),
                        "PRESS": lambda dev, arg: dev.press(**arg),
                        "TYPE": lambda dev, arg: dev.type(**arg),
                        "SLEEP": lambda dev, arg: MonkeyRunner.sleep(**arg)
                        }

        self.PhysicalButton={"HOME": "KEYCODE_HOME", 
                             "SEARCH": "KEYCODE_SEARCH", 
                              "MENU": "KEYCODE_MENU", 
                              "BACK": "KEYCODE_BACK", 
                              "DPAD_UP": "DPAD_UP", 
                              "DPAD_DOWN": "DPAD_DOWN", 
                              "DPAD_LEFT": "DPAD_LEFT", 
                              "DPAD_RIGHT": "DPAD_RIGHT", 
                              "DPAD_CENTER": "DPAD_CENTER", 
                              "ENTER": "enter"
                            }
        self.action_type_list=["DOWN", "UP", "DOWN_AND_UP"]
        self.action_down = "DOWN"
        self.action_up = "UP"
        self.action_down_and_up = "DOWN_AND_UP"
        
        if None!=serial:
            self.device = MonkeyRunner.waitForConnection(deviceId=serial)
        else:
            self.device = MonkeyRunner.waitForConnection()
           
    def press(self, key_code, action_type):
        self.device.press(key_code, action_type)
    
    def clickHomeButton(self):
        self.device.press("KEYCODE_HOME", "DOWN_AND_UP")
    
    def clickMenuButton(self):
        self.device.press("KEYCODE_MENU", "DOWN_AND_UP")
    
    def clickBackButton(self):
        self.device.press("KEYCODE_BACK", "DOWN_AND_UP")
    
    def clickSearchButton(self):
        self.device.press("KEYCODE_SEARCH", "DOWN_AND_UP")    
    
    def sleep(self, time_sec):
        MonkeyRunner.sleep(time_sec)
    
    #- Simulates a drag gesture (touch, hold, and move) on this device's screen.
    def drag(self, fromX, fromY, toX, toY, duration=0.1, steps=2):
        self.device.drag((fromX, fromY), (toX, toY), duration, steps)
    
    def touch(self, targetX, targetY, action_type):
        self.device.touch(targetX, targetY, action_type)
    
    def snapShot(self, file_dir, file_name):
        try:
            result = self.device.takeSnapshot()
            file_path = file_dir + os.sep + file_name + ".png"
            result.writeToFile(file_path, "png")
            return True
        except Exception,e:
            print e
            return False 
            
    def sameAs(self, otherImage, percent):
        try:
            result = self.device.takeSnapshot()
            return result.sameAs(otherImage, percent) # otherImage should be a MonkeyImage type
        except Exception,e:
            print e
            return None
    
    #===========================================================================
    # Sends the characters contained in message to this device, 
    # as if they had been typed on the device's keyboard. 
    # This is equivalent to calling press() for each keycode in message 
    # using the key event type DOWN_AND_UP.    
    #===========================================================================
    def typeText(self, message):
        self.device.type(message)
    
    def installPkg(self, local_apk_path):
        self.device.installPackage(local_apk_path)
    
    def startActivity(self, package_name, activity_name):
        runComponent = package_name + "/" + activity_name
        self.device.startActivity(component = runComponent)
     
    # Deletes the specified package from this device, including its data and cache.
    def removePkg(self, package_name):
        self.device.removePackage(package_name)
    
    # Wakes the screen of this device.
    def wake(self):
        self.device.wake()


class EasyDevice():
    def __init__(self):
        self.monkey_runner_impl = MonkeyRunnerImpl()
        self.easy_device = EasyMonkeyDevice(self.monkey_runner_impl.device)
        
    def getFocusedWindowClassName(self):
        return self.easy_device.getFocusedWindowId()

class IChimpDevice():
    def __init__(self):
        self.monkey_runner_impl = MonkeyRunnerImpl()
        self.ichimp_device = self.monkey_runner_impl.device.getImpl()
        
    def getFocusedWindowClassName(self):
        HV = self.ichimp_device.getHierarchyViewer()
        return HV.getFocusedWindowName()
        
        
class HierarchyViewer():
    def __init__(self):
        self.monkey_runner_impl = MonkeyRunnerImpl()
        self.hierarchy_viewer = self.monkey_runner_impl.device.getHierarchyViewer()
    
    def getFocusedWindowClassName(self):
        return self.hierarchy_viewer.getFocusedWindowName()
        
#===============================================================================
# # Left: newLeft = (Root Node)->mLeft + (ParentNode)->mLeft + ... + self->mLeft
# # Right: newRight = newLeft + (self->mRight - self->mLeft)
# # Top : newTop = (Root Node)->mTop + (ParentNode)->mTop + ... + self->mTop
# # Bottom: newBottom = newTop + (self->mBottom - self->mTop)
#===============================================================================
def clickEvent_Point(monkey_runner_impl):
    ## calculate (digit 7 : 80/370)
    print "begin"
    monkey_runner_impl.touch(59, 406, "DOWN_AND_UP")
    monkey_runner_impl.touch(59, 277, "DOWN_AND_UP")
    print "end"        
    monkey_runner_impl.sleep(1)

    ## Notification (y: 0-37  / x: 8-471 )
    print "begin"
    monkey_runner_impl.touch(471, 37, "DOWN_AND_UP")
    print "end"
    MonkeyRunner.sleep(1)
    
    monkey_runner_impl.press("KEYCODE_MENU", "DOWN_AND_UP");
    monkey_runner_impl.sleep(1)
    
    monkey_runner_impl.press("KEYCODE_BACK", "DOWN_AND_UP");

def touchEventByViewFile(view_file_name, monkey_runner_impl):
    pass

def touchEventByViewPointList(view_point_list,monkey_runner_impl):
    for view_point in view_point_list:
        monkey_runner_impl.touch(view_point[0],view_point[1],"DOWN_AND_UP")
        MonkeyRunner.sleep(0.7)

def dragEventByViewFile(view_file):
    pass

def dragEventByViewPointList(view_point_list, monkey_runner_impl):
    print str(monkey_runner_impl.device.getProperty('display.width'))
    print str(monkey_runner_impl.device.getProperty('display.height'))
    monkey_runner_impl.drag(350, 370, 50, 370)
    

def main():
    monkey_runner_impl = MonkeyRunnerImpl()
    view_file_dir = os.getcwd() + os.sep + "view_file"
    view_file_path = view_file_dir + os.sep + "click.vf"
    view_file = open(view_file_path, "r")
    view_point_list=[]
    for eachline in view_file:
        l = eachline.strip("\n").split("|")
        t = (int(l[0],10),int(l[1],10))
        view_point_list.append(t)
      
    clickEvent_Point(monkey_runner_impl) ## this is just for testing

    touchEventByViewPointList(view_point_list,monkey_runner_impl)
    
    dragEventByViewPointList(view_point_list, monkey_runner_impl)


if __name__ == "__main__":
    main()
    