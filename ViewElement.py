#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
#===============================================================================

from ViewController.Controller import Controller

class ViewElement():
    '''
    View Element
    '''
    
    # init attributes
    def __init__(self, element):
        self.m_controller = Controller()
        
        self.mClassName = element.mClassName
        self.mText = element.mText
        #self.mIsClickable = False
        self.mIsVisible = element.mVisible
    
    # get attribute
    def getter(self):
        pass
    
    def getVisible(self):
        return self.mIsVisible
        
    # view's behaviors    
    def click(self):
        pass
    
    def touch(self):
        pass
    
    def longClick(self):
        pass
    