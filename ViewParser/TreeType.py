#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## TreeType.py

#===============================================================================
# # data structures
#===============================================================================
class CRect(object):
    mLeft = 0
    mRight = 0
    mTop = 0
    mBottom = 0

class CTreeNode(object):
    mClassName = "mClassName"
    mId = "mId"
    mText = "mText"
    mAbsoluteRect=CRect()
    mRect = CRect()
    mElement = "element_data" ## just init, it was string data which was dumped from telnet
    mParentNode = {} ## just init, but it also was CTreeNode object
    mChildNodes = []
    mDepth = 0
    mTreeDepth = 0 ## its depth in this view tree
    mActive = False ## currently, I get this value from (DRAWN, Visiable, Clickable)