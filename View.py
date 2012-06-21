#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## View.py

class View():
    '''
    View Class which describe View Object of Android System with python
    '''
    def __init__(self, dump_info):
        self.original_data = dump_info
        self.elements_list = []
    
    def getLocation(self, view):
        pass
    
    def getVisible(self):
        pass
    
    def getClickable(self):
        pass
    
    def getText(self):
        pass
    
    def touch(self):
        pass
    
    def typeText(self):
        pass
    
    def drag(self):
        pass
    
    
if __name__=="__main__":
    view = View()