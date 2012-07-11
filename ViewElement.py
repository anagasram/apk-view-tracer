#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
#===============================================================================

class ViewElement():
    '''
    View Element
    '''
    
    # init attributes
    def __init__(self, element):
        self.mClassName = element.mClassName
        self.mText = element.mText
        self.mIsClickable = False
        self.mIsVisible = False
    
    # set attribute
    def setter(self):
        pass
    
    # get attribute
    def getter(self):
        pass
        
    # operate view element
    def operate(self):
        pass
    
    def click(self):
        pass
    
    def touch(self):
        pass
    
    def longClick(self):
        pass
    