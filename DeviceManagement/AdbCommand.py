#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## AdbCommand.py

import os

class AdbCommand():
    '''
    Adb Command : it use adb command
    '''
    __ClassName = "CommandConsole"
    
    def __init__(self, logger, device_name, device_port):
        self.device_port = device_port
        self.device_name = device_name
        self.m_logger = logger
        
    def executeCommand(self, cmd):
        try:
            os.system(cmd)
            return True
        except Exception, e:
            msg = "[%s] Failed execute cmd [%s]: [%s]" %(self.class_name, cmd, str(e))
            print msg
            self.m_logger.error(msg)
            return False
        
    def installPkg(self, package_name):
        installPkgCmd = "adb -s %s install %s" %(self.device_name, package_name)
        return self.executeCommand(installPkgCmd)
    
    def removePkg(self, package_name):
        removePkgCmd = "adb -s %s uninstall %s" %(self.device_name, package_name)
        return self.executeCommand(removePkgCmd)
    
    ## for example:
    ## To start the Settings application: # am start -n com.android.settings/.Settings
    ##                                    # am start -n com.android.settings/com.android.settings.Settings
    ## To start the Browser: # am start -n com.android.browser/.BrowserActivity
    ##                       # am start -n com.android.browser/com.android.browser.BrowserActivity
    ## To start the Calculator # am start -n com.android.calculator2/.Calculator
    ##                         # am start -n com.android.calculator2/com.android.calculator2.Calculator
    def startActivity(self, package_name, activity_name):
        # -W must be before -n
        # -W is "start" command option, and -n is <INTENT> option
        startActivityCmd = "adb -s %s shell am start -W -n %s/.%s" %(self.device_name, package_name, activity_name)
        return self.executeCommand(startActivityCmd)
    
    ## To start the phone dialer: # am start tel:210-385-0098
    def startPhoneDialer(self, phone_number):
        startPhoneDialerCmd = "adb -s %s shell am start tel:%s" %(self.device_name, str(phone_number))
        return self.executeCommand(startPhoneDialerCmd)
    
    def startService(self, service_name):
        startServiceCmd = "adb -s %s shell am startservice %s" %(self.device_name, service_name)
        return self.executeCommand(startServiceCmd)
        
    def sendBroadcastIntent(self, broadcast_name):
        sendIntentCmd = "adb -s %s shell am broadcast %s" %(self.device_name, broadcast_name)
        return self.executeCommand(sendIntentCmd)
    
    def startInstrumentation(self, component_name):
        startInstrumentationCmd = "adb -s %s shell am instrument -w %s" %(self.device_name, component_name)
        return self.executeCommand(startInstrumentationCmd)
    
    def pushFile(self, local_path, emulator_path):
        pushFileCmd = "adb -s %s push %s %s" %(self.device_name, local_path, emulator_path)
        return self.executeCommand(pushFileCmd)
    
    def pullFile(self, emulator_path, local_path):
        pullFileCmd = "adb -s %s pull %s %s" %(self.device_name, emulator_path, local_path)
        return self.executeCommand(pullFileCmd)
        
    def phoneCall(self):
        pass
    
    def sendSMS(self):
        pass
    
    def browseWebPage(self):
        pass
    
    