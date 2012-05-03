#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracking
## ParseElement.py

import os
from DeviceConnection import getInfosByTelnet
from GlobalVariable import *
from toolkit import str2int



#===============================================================================
# # global variable
#===============================================================================
element_dict={"class_name": "com.android.**",
              "id_address": "40ff1234",
              "depth": 0,
              }
elements_list=[]

def parse_structure(data):
    list_data = data.split("\n")
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
        blanks_list.append(count)
        elements_list.append(element)

#        parse element
#        parse_ID(element)
#        print parse_Text(element)
#        parse_Clickable(element)
#        parse_Visible(element)
#        print getRectArea(element)
#        print getRectMidPoint(element)

    #print elements_list
    print blanks_list
    
    return elements_list,blanks_list


#===============================================================================
# # get Class Name of View and its RID (Resource file ID)
# # android.widget.ListView@44ed6480
# # android.widget.TextView@44ed7e08
#===============================================================================
def parse_ClassName(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if ''==tag:
            tag_list.remove(tag)
    for tag in tag_list:
        if ''==tag:
            tag_list.remove(tag)
    for tag in tag_list:
        if ''==tag:
            tag_list.remove(tag)

    string = tag_list[0]
    l = string.split("@")
    class_name = l[0]
##    for tag in tag_list:
##        if "@" in tag:
##            l = tag.split("@")
##            class_name = l[0]
    return class_name

def parse_RID(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if ''==tag:
            tag_list.remove(tag)
    for tag in tag_list:
        if ''==tag:
            tag_list.remove(tag)
    for tag in tag_list:
        if ''==tag:
            tag_list.remove(tag)

    string = tag_list[0]
    l = string.split("@")
    resource_id = l[1]
##    for tag in tag_list:
##        if "@" in tag:
##            l = tag.split("@")
##            resource_id = l[1]
    return resource_id
    

#===============================================================================
# # etc. mID=7,id/sqrt
#===============================================================================
def parse_ID(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if "mID=" in tag:
            l = tag.split(",")
            ## idid mID=14,id/panelswitch
            ##  / 
            return l[-1]


#===============================================================================
# # getVisibility()=n, xxx
# # three states: VISIBLE, GONE, 
#===============================================================================
def parse_Visible(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if "getVisibility()=" in tag:
            l = tag.split(",")
            if "VISIBLE" == l[1]:
                return True
            elif "GONE" == l[1]:
                return False
            elif "INVISIBLE" == l[1]:
                return False
            else:
                return False

#===============================================================================
# # isClickable()=4,true
# # isClickable()=5,false
#===============================================================================
def parse_Clickable(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if "isClickable()=" in tag:
            l = tag.split(",")
            if "true" == l[1]:
                return True
            else:
                return False

#===============================================================================
# # isEnabled()=4,true
#===============================================================================
def parse_Enable(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if "isEnabled()=" in tag:
            l = tag.split(",")
            if "true" == l[1]:
                return True
            else:
                return False
    return False


#===============================================================================
# # willNotDraw()=5,false
# # willNotDraw()=4,true
#===============================================================================
def parse_WillNotDraw(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if "willNotDraw()=" in tag:
            l = tag.split(",")
            if "true" == l[1]:
                return True
            else:
                return False
    return False

#===============================================================================
# #  mPrivateFlags_NOT_DRAWN=3,0x0   false
# #  mPrivateFlags_DRAWN=4,0x20      true
#===============================================================================
def parse_DRAWN(element):
    tag_list = element.split(" ")
    drawn_flag = "mPrivateFlags_DRAWN=4,0x20"
    not_drawn_flag = "mPrivateFlags_NOT_DRAWN=3,0x0"
    if drawn_flag in tag_list:
        return True
    elif not_drawn_flag in tag_list:
        return False
    else:
        print "Failed to get DRAWN Info."
        return False
    
#===============================================================================
# # etc. mText=3,log
# # etc. mText=1,√
#===============================================================================
def parse_Text(element):
    tag_list = element.split(" ")
    for tag in tag_list:
        if "mText=" in tag:
            l = tag.split(",")
            return l[-1]

def parse_EditText(element):
    pass       


def getRectArea(element):
    rect = CRect()

    tag_list = element.split(" ")
    for tag in tag_list:
        if "mTop=" in tag:
            l = tag.split(",")
            rect.mTop = str2int(l[-1])
        elif "mBottom=" in tag:
            l = tag.split(",")
            rect.mBottom = str2int(l[-1])
        elif "mLeft=" in tag:
            l = tag.split(",")
            rect.mLeft = str2int(l[-1])
        elif "mRight" in tag:
            l = tag.split(",")
            rect.mRight = str2int(l[-1])

    return rect


#===============================================================================
# # this method is not used
#===============================================================================
def getRectMidPoint(element):
    mid_point = {"x": None,
                 "y": None}

    rect = {"left": None,
            "right": None,
            "top": None,
            "bottom": None}
    tag_list = element.split(" ")
    for tag in tag_list:
        if "mTop=" in tag:
            l = tag.split(",")
            rect["top"] = l[1]
        elif "mBottom=" in tag:
            l = tag.split(",")
            rect["bottom"] = l[1]
        elif "mLeft=" in tag:
            l = tag.split(",")
            rect["left"] = l[1]
        elif "mRight" in tag:
            l = tag.split(",")
            rect["right"] = l[1]

    if (rect["top"]!=None) and (rect["bottom"]!=None) and (rect["left"]!=None) and (rect["right"]!=None):
        mid_point["x"] = (str2int(rect["right"])-str2int(rect["left"]))/2.0
        mid_point["y"] = (str2int(rect["bottom"])-str2int(rect["top"]))/2.0

    return mid_point


if __name__=="__main__":
    data = getInfosByTelnet(dump_view_cmd)
    parse_structure(data)
