#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ParseRule.py

import os
import ConfigParser
from toolkit import getRuleDir

## for example
## xxx.rule
## depth = 3
## event_type = touch, click, drag
## clickEventsCount=50
## touchEventsCount=50
## dragEventsCount=50
## ......


class ParseRule():
    
    def __init__(self):
        self.rule_file_name = "default.rule"
        self.rule_file_path = getRuleDir() + os.sep + self.rule_file_name
    
    def setRuleFile(self, file_name):
        self.rule_file_name = file_name
        
    def getRuleFile(self):
        return self.rule_file_name
    
    def parseRule(self):
        config = ConfigParser.ConfigParser()
        config.read(self.rule_file_path)
        

## parse rule files to monkey script files
if __name__ == "__main__":
    pass
