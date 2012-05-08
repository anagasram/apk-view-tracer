#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## InitEnv.py

import os
from toolkit import getRuleDir,getConfDir,getToolsDir,getPlatformToolsDir

class InitEnvironment():
    def __init__(self):
        pass
    
    ## check dir
    def checkDir(self):
        dir_list = os.listdir(os.getcwd())
        if "conf" not in dir_list:
            print "It needs 'conf' dir here! "
            return False            
        if "rule" not in dir_list:
            print "It needs 'rule' dir here! "
            return False        
        if "tools" not in dir_list:
            print "It needs android sdk tools dir here! "
            return False        
        if "platform-tools" not in dir_list:
            print "It needs android sdk platform-tools dir here! "
            return False
        if "view_file" not in dir_list:
            print "It needs view_file dir here! "
        return True

    ## check file
    def checkFile(self):
        rule_file_list = os.listdir(getRuleDir())
        if (None==rule_file_list) or (0==len(rule_file_list)):
            print "There is no rule files in rule dir! "
            return False
        conf_files_list = os.listdir(getConfDir())
        if (None==conf_files_list) or (0==len(conf_files_list)):
            print "There is no conf files in conf dir! "
            return False
        android_tool_file_list = os.listdir(getToolsDir())
        if (None==android_tool_file_list) or (0==len(android_tool_file_list)):
            print "There is no files in android sdk tools dir! "
            return False
        android_platform_tools_file_list = os.listdir(getPlatformToolsDir())
        if (None==android_platform_tools_file_list) or (0==len(android_platform_tools_file_list)):
            print "There is no files in android sdk platform-tools dir! "
            return False               
        return True
        
    def init_env(self):
        if self.checkDir() and self.checkFile():
            print "Sucess to init enviroment! "
            return True
        else:
            return False
        
if __name__=="__main__":
    InitEnv = InitEnvironment()
    InitEnv.init_env()
