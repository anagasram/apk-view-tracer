#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## InitDevice.py

import os
from GetConfigInfo import ConfigGetter

#===============================================================================
# init service and check
#===============================================================================
def init_service():
    config = ConfigGetter()
    port = config.getServerPort()
    ## check
    check_cmd = "adb shell getprop ro.secure"
    out=os.popen(check_cmd) ## return "0\r\n" or "1\r\n"
    res = out.read()
    if (None==res) or (0==len(res)):
        print "Please check whether your device or emulator is running?"
        out.close()
        return False
    elif '1'==res[0]:
        print "Your device might not have this service!"
        return False
    out.close()
    ## stop window service first
    stopWinService_cmd = "adb shell service call window 2 i32 %s" %port
    out = os.popen(stopWinService_cmd)
    print out.read()
    out.close()
    ## start window service then
    startWinService_cmd = "adb shell service call window 1 i32 %s" %port
    out = os.popen(startWinService_cmd)
    print out.read()
    out.close()
    ## set port forwarding
    setPortForwarding_cmd = "adb forward tcp:%s tcp:%s" %(port, port)
    out = os.popen(setPortForwarding_cmd)
    print out.read()
    out.close()

    return True
