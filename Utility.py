#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## Utility.py
import os

def str2int(s):
    return int(s,10)

## "0x20" --> 32 (dec)
def hexstr2int(s):
    return int(s,16)

## "020"  --> 16 (dec)
def octstr2int(s):
    return int(s,8)


#===============================================================================
# # get parent directory
#===============================================================================
def getParDir():
    return os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))

def getConfDir():
    return os.getcwd() + os.path.sep + "conf"

def getRuleDir():
    return os.getcwd() + os.path.sep + "rule"

def getToolsDir():
    return os.getcwd() + os.path.sep + "tools"

def getPlatformToolsDir():
    return os.getcwd() + os.path.sep + "platform-tools"

def getViewFileDir():
    return os.getcwd() + os.path.sep + "view_file"