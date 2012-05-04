#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## GetViewState.py

from ParseElement import ParseElement


class GetViewState():
    def __init__(self):
        self.element_parser = ParseElement()
    
    ## The Visible state of parent node decide the Visible state of child node
    ## 应该是遍历所有的父节点的，但是下面的setNodeValue()函数是从root node开始，从上往下填值的，所以可以只判断自己和直接父节点的状态即可
    def getVisibleState(self, node):
        if None == node.mParentNode:
            return self.element_parser.parse_Visible(node.mElement)
        else:
            return (self.element_parser.parse_Visible(node.mElement) and self.element_parser.parse_Visible(node.mParentNode.mElement))
    
    ## 遍历所有父节点的方法
    def getVisibleState_2(self, node):
        pass
    
    ## Some Views 本身的 isClickable()=false, but its parent node 的 isClickable()=true
    ## so, these Views should be clickable
    ## for example, ListView is
    def getClickableState(self, node):
        parent_node = node.mParentNode
        parent_ClassName = self.element_parser.parse_ClassName(parent_node.mElement)
        print parent_ClassName
        if "android.widget.ListView" == parent_ClassName:
            return self.element_parser.parse_Clickable(parent_node.mElement)
        else:
            return self.element_parser.parse_Clickable(node.mElement)        
            
    
    ## mActive = False means it can not handle events
    ## mActive = True means it can handle events
    def getActiveState(self, node):
        element = node.mElement
        try:
            if self.element_parser.parse_WillNotDraw(element):
                print "Will Not Draw!"
                return False
            if not self.getVisibleState(node):
                print "Not Visible!"
                return False
            if not self.getClickableState(node):
                print "Not Clickable!"
                return False
            if not self.element_parser.parse_DRAWN(element):
                print "Not Drawn!"
                return False
            else:
                return True
        except Exception,e:
            print "Failed to get Active State of Element! %s" %str(e)
            return False

