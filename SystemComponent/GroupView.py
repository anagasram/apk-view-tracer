#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
#===============================================================================

import os,sys
current_path = os.getcwd()
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if current_path not in sys.path:
    sys.path.append(current_path)
if parent_path not in sys.path:
    sys.path.append(parent_path)
    
from ViewManagement.TreeType import CPoint
from ViewManagement.TreeType import CTreeNode

class Item():
    '''
    item of Group View
    '''
    
    def __init__(self, node, index):
        self.class_name = "Item"
        self.node = node
        self.index = index
        
        self.text_list = []
        self.click_location_list = []   
        self.isChecked = False
        
        self.properties_dict = {}
        
    def loadProperties(self):
        # has no child
        if None==self.node.mChildNodes or 0==len(self.node.mChildNodes):
            self.text_list.append(self.node.mText)
            self.click_location_list.append(self.node.mLocation)
            # isChecked 
            return True
        
        # has child
        for child in self.node.mChildNodes:
            pass
            
    
    
#------------------------------------------------------------------------------ 
#        
#------------------------------------------------------------------------------ 
class GroupView():
    '''
    GroupView, include ListView, GripView, RadioGroup, etc.
    '''
    
    def __init__(self, node):
        self.class_name = "ViewGroup"
        self.node = node   
        self.items_list = []
        
    def loadAllItems(self):
        if None==self.node.mChildNodes or 0==len(self.node.mChildNodes):
            return False
        
        index = 0
        for item_node in self.node.mChildNodes:
            item = Item(item_node, index)
            item.loadProperties()
            self.items_list.append(item)
            
            index += 1
        
        return True

     
if __name__=="__main__":
    pass       
                    
    