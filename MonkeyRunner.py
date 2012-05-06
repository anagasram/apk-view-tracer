#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## MonkeyRunner.py

## run mode
## java -jar $(jython.jar file path) $(python script file)

## adb shell monkey <...>

## start monkey server
## adb forward tcp:1080 tcp:1080
## adb shell monkey --port 1080

import os
import sys
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.recorder import MonkeyRecorder

class MonkeyRunner():
    def __init__(self):
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

    def action(self, device, key_code, action_type):
        device.press(key_code, action_type)
    
    def click(self, device, key_code):
        device.press(key_code, "DOWN_AND_UP")
    
    def clickHomeButton(self, device):
        device.press("KEYCODE_HOME", "DOWN_AND_UP")
    
    def clickMenuButton(self, device):
        device.press("KEYCODE_MENU", "DOWN_AND_UP")
    
    def clickBackButton(self, device):
        device.press("KEYCODE_BACK", "DOWN_AND_UP")
    
    def clickSearchButton(self, device):
        device.press("KEYCODE_SEARCH", "DOWN_AND_UP")
    
    
    def sleep(self, time_sec):
        MonkeyRunner.sleep(time_sec)
    
    def dragEvent(self, device):
        pass

    #def drag_Down(self, device):
    #    cd = ChangeData
    #    log = Logs()
    #    list = cd.coordinate()
    #    if len(list) > 0:
    #        startX = list[0]
    #        startY = list[1]
    #        endX = list[2]
    #        endY = list[3]
    #        device.drag((startX,startY),(endX,endY),3,2)
    #        log.writeLog('device.drag(('+str(startX)+','+str(startY)+'),('+str(endX)+','+str(endY)+'),'+str(3)+','+str(2)+')')
    #    else:
    #       log.writeLog('List is null') 
    
    
    def touchEvent(self, device):
        pass
    
    def snapShot(self, device):
        result = device.takeSnapshot()
        return result
    
    def saveShot(self, result, degree):
        result.writeToFile("./shot"+str(degree)+".png", "png")
    
    def typeText(self, device):
        pass
    
    def installPkg(self, device):
        pass
    
    def startActivity(self, device):
        pass


## Left: newLeft = (Root Node)->mLeft + (ParentNode)->mLeft + ... + self->mLeft
## Right: newRight = newLeft + (self->mRight - self->mLeft)
## Top : newTop = (Root Node)->mTop + (ParentNode)->mTop + ... + self->mTop
## Bottom: newBottom = newTop + (self->mBottom - self->mTop)
def clickEvent_Point(device):
    print "begin"
    device.touch(59, 406, "DOWN_AND_UP")
    print "end"
    
    MonkeyRunner.sleep(2)

    ## Notification (y: 0-37  / x: 8-471 )
    print "begin"
    device.touch(471, 37, "DOWN_AND_UP")
    print "end"

    ## calculate (digit 7 : 80/370)

    MonkeyRunner.sleep(2)
    device.press("KEYCODE_MENU", "DOWN_AND_UP");

    MonkeyRunner.sleep(2)
    device.press("KEYCODE_BACK", "DOWN_AND_UP");


if __name__=="__main__":
    device = MonkeyRunner.waitForConnection()
    #clickEvent(device)
    clickEvent_Point(device)

