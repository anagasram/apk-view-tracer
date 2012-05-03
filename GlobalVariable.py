#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## GlobalVariable.py

import os


## ------------------------------------------
## Android Windows View Server Info
## ------------------------------------------
host = 'localhost'
port = 4939
time_out = 60

list_view_cmd = "LIST"
dump_view_cmd = "DUMP -1"

## -------------------------------------------
## dir path
## -------------------------------------------
curDir = os.getcwd()
conf_dir = curDir + os.sep + "conf" + os.sep
rules_dir = curDir + os.sep + "rules" + os.sep



## -----------------------------------------
## data structures
## -----------------------------------------

##rect_dict = {"left": "mLeft",
##             "right": "mRight",
##             "top": "mTop",
##             "bottom": "mBottom"}
##
#### a tree node is a dict type
##type_tree_node={"id": "mId",
##		"text": "mText",
##		"rect": rect_dict,
##                "element": "element_data",
##		"parent_node": {},
##		"child_nodes": [],
##                "depth": 0}

class CRect(object):
    mLeft = 0
    mRight = 0
    mTop = 0
    mBottom = 0

class CTreeNode(object):
    mId = "mId"
    mText = "mText"
    mAbsoluteRect=CRect()
    mRect = CRect()
    mElement = "element_data"
    mParentNode = {}
    mChildNodes = []
    mDepth = 0
    mActive = False ## currently, I get this value from (DRAWN, Visiable, Clickable)


## Action List and Map which ensure action sequence
click_action_list=[]
touch_action_list=[]
drag_action_list=[]
Action_Sequence_Map = {"click": click_action_list,
                       "touch": touch_action_list,
                       "drag": drag_action_list}

## View Map 
class CViewMapElement(object):
    mHashCode = "12345678"              ## hex string <Hash Code of WindowState Object>
    mTriggerHashCode = "12345678"       ## same as above
    mNextElementHashCode= "12345678"    ## same as above    


## global variables for store
g_bReDump = False  ## re dump view if it was True
g_sPreFocusedViewHashCode = "0"  ## set this value 
g_sCurFocusedViewHashCode = "0"  ## set this value after dump
g_lsPreViewsList = []   ## set this value 
g_lsCurViewsList = []   ## set this value
