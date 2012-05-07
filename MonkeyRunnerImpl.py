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
from com.android.monkeyrunner.recorder import MonkeyRecorder

class MonkeyRunnerImpl():
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
        
        self.device = MonkeyRunner.waitForConnection()

    def action(self, key_code, action_type):
        self.device.press(key_code, action_type)
    
    def clickByKeyCode(self, key_code, action_type):
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
    
    def drag(self, fromX, fromY, toX, toY):
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
        
    def typeText(self):
        pass
    
    def installPkg(self, local_apk_path):
        self.device.installPackage(local_apk_path)
    
    def startActivity(self, package_name, activity_name):
        runComponent = package_name + "/" + activity_name
        self.device.startActivity(component = runComponent)
        


#===============================================================================
# 
#===============================================================================
def testClickEvent(device):

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
    
    monkey_runner_impl.clickByKeyCode("KEYCODE_MENU", "DOWN_AND_UP");
    monkey_runner_impl.sleep(1)
    
    monkey_runner_impl.clickByKeyCode("KEYCODE_BACK", "DOWN_AND_UP");

def process_ViewFile(view_file):
    pass

def process_ViewPointList(view_point_list,monkey_runner_impl):
    for view_point in view_point_list:
        monkey_runner_impl.touch(view_point[0],view_point[1],"DOWN_AND_UP")
        MonkeyRunner.sleep(2)

def main():
    monkey_runner_impl = MonkeyRunnerImpl()
    view_file = open(os.getcwd()+os.sep+"demo.vf","r")
    view_point_list=[]
    for eachline in view_file:
        l = eachline.strip("\n").split("|")
        t = (int(l[0],10),int(l[1],10))
        view_point_list.append(t)
            
    #clickEvent(device)    
    clickEvent_Point(monkey_runner_impl) ## this is just for testing

    process_ViewPointList(view_point_list,monkey_runner_impl)


if __name__ == "__main__":
    main()
    