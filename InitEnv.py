#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## InitEnv.py

import os
from GlobalVariable import curDir, conf_dir, rules_dir
from GlobalVariable import *

## check dir
def checkDir():
    ll = os.listdir(curDir)
    if "conf" not in ll:
        try:
            print "mkdir conf"
            os.mkdir(curDir+os.sep+"conf")
        except Exception,e:
            print e
            return False
        
    if "rules" not in ll:
        try:
            print "mkdir rules"
            os.mkdir(curDir+os.sep+"rules")
            
        except Exception,e:
            print e
            return False

    res = os.listdir(rules_dir)
    if (None==res) or (0==len(res)):
        print "There has no rule files in rules dir."
        return False

    print "Sucess to init enviroment."
    return True
        


if __name__=="__main__":
    checkDir()
