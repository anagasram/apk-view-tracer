#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracking
## BuildTree.py

import os
import copy
from GlobalVariable import *
from toolkit import *
from DeviceConnection import getInfosByTelnet
from ParseElement import *
from GetViewState import *


def buildTree(elements_list, blanks_list):
    tree_nodes_list=[]
    
    root_node= CTreeNode()
    root_node.mParentNode=None
    

    total_count = len(blanks_list)

    depth = 0
    pre_depth = depth-1
    for x in range(total_count):
        index = x        
        blanks_count = blanks_list[index]
        depth = blanks_count
        node = CTreeNode()
        
        if 0 == blanks_count:
            root_node.mElement = elements_list[index]
            root_node.mDepth = 0
            tree_nodes_list.append(root_node)
            
        else:
            pre_index = x-1
            pre_depth = blanks_list[pre_index]
            pre_depth = tree_nodes_list[pre_index].mDepth
            
            node.mElement = elements_list[index]
            node.mDepth = blanks_count

            delta_depth = (depth - pre_depth)
            if (1 == delta_depth):
                ## 本节点是上一个节点的子节点
                node.mParentNode = tree_nodes_list[pre_index]
                tree_nodes_list.append(node)
            elif (0 == delta_depth):
                ## 等深度， 取上一个的父节点作为自己的父节点
                node.mParentNode = tree_nodes_list[pre_index].mParentNode
                tree_nodes_list.append(node)
            elif (0 > delta_depth):
                ## 向上递归寻找和自己等深度的节点
                new_delta_depth = delta_depth
                new_pre_depth = pre_depth
                new_pre_index = pre_index
                while True:
                    if 0==new_delta_depth:
                        node.mParentNode = tree_nodes_list[new_pre_index].mParentNode
                        tree_nodes_list.append(node)
                        break
                    else:
                        new_pre_index -= 1
                        new_pre_depth = tree_nodes_list[new_pre_index].mDepth
                        new_delta_depth = depth - new_pre_depth
            else:
                raise Exception, "Raise an Exception when Build Elements Tree!"
                break
           

    return tree_nodes_list


## Left: newLeft = (Root Node)->mLeft + (ParentNode)->mLeft + ... + self->mLeft
## Right: newRight = newLeft + (self->mRight - self->mLeft)
## Top : newTop = (Root Node)->mTop + (ParentNode)->mTop + ... + self->mTop
## Bottom: newBottom = newTop + (self->mBottom - self->mTop)
def getAbsoluteRect(node):
    absoluteRect = CRect()
    
    temp_rect = CRect()    
    current_node = CTreeNode()
    current_node = copy.deepcopy(node)
    temp_rect=current_node.mRect

##    print "/////////////////begin trace ////////////////////////////////"
##    print node.mRect.mTop, node.mRect.mBottom, node.mRect.mLeft, node.mRect.mRight
    while True:        
        parent_node = CTreeNode()        
        
        if None == current_node.mParentNode:
            break
        else:
##            print "before [Top] %s [Left] %s" %(str(temp_rect.mTop),str(temp_rect.mLeft))
            parent_node = current_node.mParentNode
            temp_rect.mLeft+=parent_node.mRect.mLeft
            temp_rect.mTop+=parent_node.mRect.mTop            
            current_node = parent_node
##            print "after [Top] %s [Left] %s" %(str(temp_rect.mTop),str(temp_rect.mLeft))

    temp_rect.mRight=temp_rect.mLeft+(node.mRect.mRight-node.mRect.mLeft)
    temp_rect.mBottom=temp_rect.mTop+(node.mRect.mBottom-node.mRect.mTop)    
    absoluteRect=temp_rect
##    print node.mRect.mTop, node.mRect.mBottom, node.mRect.mLeft, node.mRect.mRight
##    print "///////////////// end trace  ///////////////////////////////"
    return absoluteRect

def setNodeValue(node):
    element = node.mElement
    if None == element:
        print "Failed to set Node Value because Error in Node!"
        return False

    node.mId = parse_ID(element)
    node.mText = parse_Text(element)
    node.mRect = getRectArea(element)
    node.mActive = getActiveState(node)
    node.mAbsoluteRect = getAbsoluteRect(node)


## not implement yet
def getChildNodesList(tree_nodes_list, tree_node):

    for node in tree_nodes_list:
        pass


def build():
    data = getInfosByTelnet(dump_view_cmd)
    elements_list, blanks_list = parse_structure(data)
    tree_nodes_list = buildTree(elements_list, blanks_list)

    for node in tree_nodes_list:
        ## set node value from root node to child node
        setNodeValue(node)
        print "*************************************************************************"
        print node.mRect.mTop, node.mRect.mBottom, node.mRect.mLeft, node.mRect.mRight
        print node.mId
        print node.mText
        print node.mActive
        print node.mAbsoluteRect.mTop, node.mAbsoluteRect.mBottom, node.mAbsoluteRect.mLeft, node.mAbsoluteRect.mRight
        print "*************************************************************************"

    return tree_nodes_list

if __name__=="__main__":
    build()

