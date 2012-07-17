#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
#===============================================================================

import telnetlib
import os, sys
curDir = os.getcwd()
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if curDir not in sys.path:
    sys.path.append(curDir)
if parent_path not in sys.path:
    sys.path.append(parent_path)
import Logger
import logging
import threading
import time


#------------------------------------------------------------------------------ 
class SocketBinder(threading.Thread):
    '''
    Socket Binder
    '''
    
    def __init__(self, monkey_server_port):
        threading.Thread.__init__(self)
        self.port = monkey_server_port
        
    def run(self):
        # bind monkey server to port
        # then monkey server listen this port
        bind_command = "adb shell monkey --port %s" %self.port
        os.system(bind_command)
        
        
#------------------------------------------------------------------------------ 
class EventController():
    '''
    Event Sender
    '''
    
    key_code_dict = {"home": "home",
                     "back": "back",
                     "menu": "menu",
                     "power": "power",
                     "search": "search",
                     "enter": "enter",
                     "dpad_up": "dpad_up",
                     "dpad_down": "dpad_down",
                     "dpad_left": "dpad_left",
                     "dpad_right": "dpad_right",
                     "dpad_center": "dpad_center"}
    
    def __init__(self, logger, device_address="127.0.0.1", monkey_server_port=12345):
        self.class_name = "EventSender"
        self.m_logger = logger
        
        self.device_address = device_address
        self.monkey_server_port = monkey_server_port
        
    
    def initService(self):
        try:
            out = os.popen("adb devices")
            res = out.read()
            out.close()
            if 0>res.find("List of devices attached"):
                msg = "[%s] There might not has devices running." %self.class_name
                self.m_logger.error(msg)
                return False
            
            # create forward port: port
            forward_command = "adb forward tcp:%s tcp:%s" %(self.monkey_server_port, self.monkey_server_port)
            os.system(forward_command)
            
            # bind monkey server to port
            binder_thread = SocketBinder(self.monkey_server_port)
            binder_thread.start()           
            time.sleep(2) # sleep 2 seconds
            
            return True
        except Exception, e:
            msg = "[%s] Failed to init service: [%s]" %(self.class_name, str(e))
            self.m_logger.error(msg)
            return False
    
    def open(self):
        if self.initService():
            #time_out = config.getServerTimeOut()
            #tn = telnetlib.Telnet(host=host, port=port, timeout=time_out) # this telnetlib is from python lib
            self.tn = telnetlib.Telnet(host=self.device_address, port=self.monkey_server_port) # this telnetlib is from jython.jar lib
            return True
        else:
            msg = "[%s] Failed to open Event Controller" %self.class_name
            self.m_logger.error(msg)
            return False
        
    def sendEventByTelnet(self, command):
        try:   
            self.tn.write(command + "\n")
            return True
        except Exception, e:
            msg = "[%s] Failed to send event `%s`: [%s] " %(self.class_name, command, str(e))
            self.m_logger.error(msg)
            return False

    def close(self):
        self.quit()
        self.tn.close()

#------------------------------------------------------------------------------ 
# basic event
#------------------------------------------------------------------------------
    # it send message that wil close current socket binding 
    def quit(self):
        return self.sendEventByTelnet("quit")
    
    # close current session, but it will not close socket binding
    def done(self):
        return self.sendEventByTelnet("done")
    
    def wake(self):
        return self.sendEventByTelnet("wake")

    def press(self, name):
        command = "press %s" %name
        return self.sendEventByTelnet(command)
    
    def keyDown(self, name):
        command = "key down %s" %name
        return self.sendEventByTelnet(command)
    
    def keyUp(self, name):
        command = "key up %s" %name
        return self.sendEventByTelnet(command)
    
    def touch(self, x, y):
        command = "tap %s %s" %(x, y)
        return self.sendEventByTelnet(command)
    
    def tap(self, x, y):
        command = "tap %s %s" %(x, y)
        return self.sendEventByTelnet(command)
    
    def touchDown(self, x, y):
        command = "touch down %s %s" %(x, y)
        return self.sendEventByTelnet(command)
    
    def touchUp(self, x, y):
        command = "touch up %s %s" %(x, y)
        return self.sendEventByTelnet(command)
    
    def touchMove(self, x, y):
        command = "touch move %s %s" %(x, y)
        return self.sendEventByTelnet(command)
    
    def type(self, text):
        command = "type %s" %text
        self.sendEventByTelnet(command)
        # there has a problem
        if True:
            self.press("enter")
            return True
        else:
            return
 
#------------------------------------------------------------------------------ 
# complex commands with combination of basic commands 
    def longClickByKeyCode(self, key_code):        
        self.keyDown(key_code)
        time.sleep(2)
        self.keyUp(key_code)
        
    def longClickByLocation(self, x, y):
        self.touchDown(x, y)
        time.sleep(2)
        self.touchUp(x, y)
        
    def drag(self, fromX, fromY, toX, toY):
        self.touchDown(fromX, fromY)
        self.touchMove(toX, toY)
        self.touchUp(toX, toY)
    

if __name__=="__main__":
    logger = Logger.InitLog("test.log", logging.getLogger("test.thread"))
    sender = EventController(logger)
    if sender.open():        
        sender.longClickByKeyCode("home")
        time.sleep(3)
        sender.press("back")
        
        time.sleep(1)
        sender.drag(100, 20, 100, 500)
        
    sender.close()
    
    