#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracking
## BuildTree.py

import copy
from TreeType import CRect,CTreeNode
from DeviceCommand.DeviceConnection import getInfosByTelnet
from ParseElement import ParseElement
from GetViewState import GetViewState

class ViewTree():
    '''
    View Tree
    '''
    
    def __init__(self):
        pass
    
    
    def getStructure(self, dump_data):
        list_data = dump_data.split("\n")
        print "length of list: %s" %len(list_data)
    
        # pop the last element "DONE"
        list_data.remove("DONE")
        print "length of list: %s" %len(list_data)
    
        elements_list=[]
        blanks_list=[]
        for element in list_data:        
            index = 0
            count = 0
            while " " == element[index]:
                index = index + 1
                count = count + 1   
            #===================================================================
            # # another method which can get blanks count in head of element
            # tag_list = element.split(" ")
            # head_tag = tag_list[0]
            # while (0 == len(head_tag)):
            #     count += 1
            #===================================================================
            
            blanks_list.append(count)
            elements_list.append(element)
        
        return elements_list,blanks_list

    def buildTree(self, elements_list, blanks_list):
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
            ## set node depth in this tree
            node.mTreeDepth = blanks_count 
            
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
                    ## current node is a child node of last node
                    node.mParentNode = tree_nodes_list[pre_index]
                    tree_nodes_list.append(node)
                elif (0 == delta_depth):
                    ## 等深度， 取上一个的父节点作为自己的父节点
                    ## these two nodes have same depth, so that they have same parent node
                    node.mParentNode = tree_nodes_list[pre_index].mParentNode
                    tree_nodes_list.append(node)
                elif (0 > delta_depth):
                    ## 向上递归寻找和自己等深度的节点
                    ## Recurse down to up, seek the node which has same depth
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
    def getAbsoluteRect(self, node):
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
    
    def setNodeValue(self, node):
        element = node.mElement
        if None == element:
            print "Failed to set Node Value because Error in Node!"
            return False
        
        element_parser = ParseElement(node.mElement)
        element_parser.parseElmentData()
        node.mClassName = element_parser.getClassName()
        node.mId = element_parser.getID()
        node.mText = element_parser.getText()
        node.mRect = element_parser.getRectArea()
        active_state = GetViewState(node)
        node.mActive = active_state.getActiveState()
        node.mAbsoluteRect = self.getAbsoluteRect(node)
    
    ## not implement yet
    def getChildNodesList(self, tree_nodes_list, tree_node):    
        for node in tree_nodes_list:
            print node
            pass
    
    
def build():
    data = getInfosByTelnet("DUMP -1")
    vt = ViewTree()
    elements_list, blanks_list = vt.getStructure(data)    
    
    tree_nodes_list = vt.buildTree(elements_list, blanks_list)

    for node in tree_nodes_list:
        ## set node value from root node to child node
        vt.setNodeValue(node)
        print "*************************************************************************"  
        print "mClassName: %s" %node.mClassName
        print "mTreeDepth: %s" %node.mTreeDepth
        print "mId: %s " %node.mId
        print "mText: %s" %node.mText
        print "mActive: %s" %node.mActive
        print "mRect.(mTop, mBottom, mLeft, mRight): %s %s %s %s" %(node.mRect.mTop, node.mRect.mBottom, node.mRect.mLeft, node.mRect.mRight)
        print "mAbsoluteRect: %s %s %s %s" %(node.mAbsoluteRect.mTop, node.mAbsoluteRect.mBottom, node.mAbsoluteRect.mLeft, node.mAbsoluteRect.mRight)
        print "*************************************************************************"

    return tree_nodes_list

if __name__=="__main__":
    build()

