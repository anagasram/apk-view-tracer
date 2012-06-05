#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## GetViewState.py

import copy
from ParseElement import ParseElement


class GetViewState():
    def __init__(self):
        self.element_parser = ParseElement()
        self.ViewGroup_ClassName_list = ["android.widget.ListView", 
                                         "android.widget.GridView", 
                                         "android.widget.RadioGroup",
                                         "android.widget.Spinner",
                                         "android.widget.Gallery"]
    
    ## The Visible state of parent node decide the Visible state of child node
    ## 应该是遍历所有的父节点的，但是下面的setNodeValue()函数是从root node开始，从上往下填值的，所以可以只判断自己和直接父节点的状态即可
    def getVisibleState(self, node):
        if None == node.mParentNode:
            return self.element_parser.getVisible(node.mElement)
        else:
            return (self.element_parser.getVisible(node.mElement) and self.element_parser.getVisible(node.mParentNode.mElement))
    
    # 遍历所有父节点的方法
    # What does this method can do?  
    def getVisibleState_All(self, node):
        bResult = None
        temp_node = copy.deepcopy(node)
        while (None != temp_node.mParentNode):
            bResult = self.element_parser.getVisible(temp_node.mElement) and self.element_parser.getVisible(temp_node.mParentNode.mElement)
            temp_node = temp_node.mParentNode
        return bResult
    
    ## Some Views 本身的 isClickable()=false, but its parent node 的 isClickable()=true
    ## so, these Views should be clickable
    ## for example, ListView, GridView,  etc. container View
    ## 但是如果，RadioGroup下包含了TextView和一些RadioButton,这个TextView是不可点击的吗？ 
    def getClickableState(self, node):
        parent_node = node.mParentNode
        parent_ClassName = self.element_parser.getClassName(parent_node.mElement)
        print parent_ClassName
        if parent_ClassName in self.ViewGroup_ClassName_list:
            return self.element_parser.getClickable(parent_node.mElement)
        else:
            return self.element_parser.getClickable(node.mElement)        
            
    
    ## mActive = False means it can not handle events
    ## mActive = True means it can handle events
    def getActiveState(self, node):
        element = node.mElement
        try:
            if self.element_parser.getWillNotDraw(element):
                print "Will Not Draw!"
                return False
            if not self.getVisibleState(node):
                print "Not Visible!"
                return False
            if not self.getClickableState(node):
                print "Not Clickable!"
                return False
            if not self.element_parser.getDRAWN(element):
                print "Not Drawn!"
                return False
            else:
                return True
        except Exception,e:
            print "Failed to get Active State of Element! %s" %str(e)
            return False

