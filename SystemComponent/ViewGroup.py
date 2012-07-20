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

class Item():
    '''
    item of View Group
    '''
    
    def __init__(self):
        self.class_name = "Item"

class ViewGroup():
    '''
    ViewGroup, include ListView, GripView, RadioGroup, etc.
    '''
    
    def __init__(self):
        self.class_name = "ViewGroup"
        self.viewgroup_item_dict = {"android.widget.RadioGroup": "android.widget.RadioButton",
                                    "android.": "android"} 