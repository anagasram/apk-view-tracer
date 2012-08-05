#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
#===============================================================================

class PopupView():
    '''
    Popup View
    '''
    
    def __init__(self, node, device_width, device_height, notification_height):
        self.device_width = device_width
        self.device_height = device_height
        self.notification_height = notification_height # this is not sure
        
        self.tree_nodes_list = None
        
        self.view_height = self.tree_nodes_list[0].mAbsoluteRect.mBottom - self.tree_nodes_list[0].mAbsoluteRect.mTop
        
        
    
    def getRealLocation(self, x, y):
        realX = x # this is not sure
        
        deltaY = (self.device_height - self.notification_height - self.view_height) / 2
        
        realY = self.notification_height + deltaY + y
        
        return realX, realY
             
        
        
    def clickViewById(self, id):
        pass
    
    def clickViewByText(self, text, partical_matching=True):
        pass
    
    
        