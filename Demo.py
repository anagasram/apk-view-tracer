#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## Demo.py

## run mode
## java -jar $(jython.jar file path) $(python script file)

## adb shell monkey <...>

## start monkey server
## adb forward tcp:1080 tcp:1080
## adb shell monkey --port 1080

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.recorder import MonkeyRecorder

import os

PhysicalButton={"HOME": "KEYCODE_HOME", 
              "SEARCH": "KEYCODE_SEARCH", 
              "MENU": "KEYCODE_MENU", 
              "BACK": "KEYCODE_BACK", 
              "DPAD_UP": "DPAD_UP", 
              "DPAD_DOWN": "DPAD_DOWN", 
              "DPAD_LEFT": "DPAD_LEFT", 
              "DPAD_RIGHT": "DPAD_RIGHT", 
              "DPAD_CENTER": "DPAD_CENTER", 
              "ENTER": "enter"}

def clickEvent(device):

    device.press("KEYCODE_1", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    device.press("KEYCODE_2", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    device.press("KEYCODE_9", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    device.press("KEYCODE_CLEAR", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    device.press("KEYCODE_MENU", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    device.press("KEYCODE_BACK", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    device.press("KEYCODE_SEARCH", "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    #device.press("KEYCODE_HOME", "DOWN_AND_UP")

def dragEvent(device):
    pass

#def drag_Down(device):
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


def snapShot(device):
    result = device.takeSnapshot()
    return result

def saveShot(result, degree):
    result.writeToFile("./shot"+str(degree)+".png", "png")

def typeText(device):
    pass

def installPkg(device):
    pass

def startActivity(device):
    pass


#===============================================================================
# # Left: newLeft = (Root Node)->mLeft + (ParentNode)->mLeft + ... + self->mLeft
# # Right: newRight = newLeft + (self->mRight - self->mLeft)
# # Top : newTop = (Root Node)->mTop + (ParentNode)->mTop + ... + self->mTop
# # Bottom: newBottom = newTop + (self->mBottom - self->mTop)
#===============================================================================
def clickEvent_Point(device):
    ## calculate (digit 7 : 80/370)
    print "begin"
    device.touch(59, 406, "DOWN_AND_UP")
    device.touch(59, 277, "DOWN_AND_UP")
    print "end"
    
    MonkeyRunner.sleep(2)

    
    ## Notification (y: 0-37  / x: 8-471 )
    print "begin"
    device.touch(471, 37, "DOWN_AND_UP")
    print "end"    

    MonkeyRunner.sleep(2)
    device.press("KEYCODE_MENU", "DOWN_AND_UP");

    MonkeyRunner.sleep(2)
    device.press("KEYCODE_BACK", "DOWN_AND_UP");


def process_ViewFile(view_file):
    pass

def process_ViewPointList(view_point_list,device):
    for view_point in view_point_list:
        device.touch(view_point[0],view_point[1],"DOWN_AND_UP")
        MonkeyRunner.sleep(2)

def main():
    view_file = open(os.getcwd()+os.sep+"demo.vf","r")
    view_point_list=[]
    for eachline in view_file:
        l = eachline.strip("\n").split("|")
        t = (int(l[0],10),int(l[1],10))
        view_point_list.append(t)
    device = MonkeyRunner.waitForConnection()
    
    #clickEvent(device)    
#    clickEvent_Point(device) ## this is just for testing

    process_ViewPointList(view_point_list,device)

if __name__=="__main__":
    main()

