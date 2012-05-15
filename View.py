#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## View.py

class View():
    '''
    View Class which describe View Object of Android System w python
    '''
    def __init__(self, device):
        self.device = device
    
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