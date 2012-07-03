#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracking
## ParseElement.py

from DeviceCommand.DeviceConnection import getInfosByTelnet
from TreeType import CRect
from Utility import str2int

#===============================================================================
# # global variable
#===============================================================================
element_dict={"class_name": "com.android.**",
              "id_address": "40ff1234",
              "depth": 0,
              }
elements_list=[]

class ParseElement():
    def __init__(self):
        self.class_name = ""
        self.hash_code = ""
        self.properties_dict = {}
    
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
    
#            #parse element
#            self.getID(element)
#            print self.getText(element)
#            self.getClickable(element)
#            self.getVisible(element)
#            print self.getRectArea(element)
#            print self.getRectMidPoint(element)
        
        return elements_list,blanks_list
    
    def getInt(self, string, integer):
        try:
            return int(self.properties_dict[string])
        except:
            return integer
        
    def getBoolean(self, string, boolean):
        try:
            if "false" == self.properties_dict[string]:
                return False
            elif "true" == self.properties_dict[string]:
                return True
            else:
                return boolean
        except:
            return boolean
    
    def loadProperties(self, data):
        i = 0
        data_length =len(data)
        print "sub string length: %s" %data_length
        
        while True:
            print i
            if i >= data_length:
                break
            key_sep_index = data.index("=", i)
            
            key = data[i : key_sep_index]
            
            value_length_sep_index = data.index(",", key_sep_index+1)
            value_length = int(data[key_sep_index+1 : value_length_sep_index])
            
            i = value_length_sep_index + 1 + value_length
            
            value = data[value_length_sep_index+1 : value_length_sep_index+1+value_length]
            
            self.properties_dict[key] = value
            
            i += 1
                
        self.id = self.properties_dict["mID"]
        
        if "mLeft" in self.properties_dict.keys():
            self.left = self.getInt("mLeft", 0)
        else:
            self.left = self.getInt("layout:mLeft", 0)
            
        if "mRight" in self.properties_dict.keys():
            self.right = self.getInt("mRight", 0)
        else:
            self.right = self.getInt("layout:mRight", 0)
        
        if "mTop" in self.properties_dict.keys():
            self.top = self.getInt("mTop", 0)
        else:
            self.top = self.getInt("layout:mTop", 0)
        
        if "mBottom" in self.properties_dict.keys():
            self.bottom = self.getInt("mBottom", 0)
        else:
            self.bottom = self.getInt("layout:mBottom", 0)
        
        if "getWidth()" in self.properties_dict.keys():
            self.width = self.getInt("getWidth()", 0)
        else:
            self.width = self.getInt("layout:getWidth()", 0)
            
        if "getHeight()" in self.properties_dict.keys():
            self.height = self.getInt("getHeight()", 0)
        else:
            self.height = self.getInt("layout:getHeight()", 0)
            
        if "mScrollX" in self.properties_dict.keys():
            self.scrollX = self.getInt("mScrollX", 0)
        else:
            self.scrollX = self.getInt("scrolling:mScrollX", 0)
            
        if "mScrollY" in self.properties_dict.keys():
            self.scrollY = self.getInt("mScrollY", 0)
        else:
            self.scrollY = self.getInt("scrolling:mScrollY", 0)
            
        if "mPaddingLeft" in self.properties_dict.keys():
            self.paddingLeft = self.getInt("mPaddingLeft", 0)
        else:
            self.paddingLeft = self.getInt("padding:mPaddingLeft", 0)
            
        if "mPaddingRight" in self.properties_dict.keys():
            self.paddingRight = self.getInt("mPaddingRight", 0)
        else:
            self.paddingRight = self.getInt("padding:mPaddingRight", 0)
            
        if "mPaddingTop" in self.properties_dict.keys():
            self.paddingTop = self.getInt("mPaddingTop", 0)
        else:
            self.paddingTop = self.getInt("padding:mPaddingTop", 0)
            
        if "mPaddingBottom" in self.properties_dict.keys():
            self.paddingBottom = self.getInt("mPaddingBottom", 0)
        else:
            self.paddingBottom = self.getInt("padding:mPaddingBottom", 0)
        
        if "layout_leftMargin" in self.properties_dict.keys():
            self.marginLeft = self.getInt("layout_leftMargin", -2147483648)
        else:
            self.marginLeft = self.getInt("layout:layout_leftMargin", -2147483648)
            
        if "layout_rightMargin" in self.properties_dict.keys():
            self.marginRight = self.getInt("layout_rightMargin", -2147483648)
        else:
            self.marginRight = self.getInt("layout:layout_rightMargin", -2147483648)    
            
        if "layout_topMargin" in self.properties_dict.keys():
            self.marginTop = self.getInt("layout_topMargin", -2147483648)
        else:
            self.marginTop = self.getInt("layout:layout_topMargin", -2147483648)
            
        if "layout_bottomMargin" in self.properties_dict.keys():
            self.marginBottom = self.getInt("layout_bottomMargin", -2147483648)
        else:
            self.marginBottom = self.getInt("layout:layout_bottomMargin", -2147483648)
            
        if "getBaseline()" in self.properties_dict.keys():
            self.baseline = self.getInt("getBaseline()", 0)
        else:
            self.baseline = self.getInt("layout:getBaseline()", 0)
            
        if "willNotDraw()" in self.properties_dict.keys():
            self.willNotDraw = self.getBoolean("willNotDraw()", False)
        else:
            self.willNotDraw = self.getBoolean("drawing:willNotDraw()", False)
            
        if "hasFocus()" in self.properties_dict.keys():
            self.hasFocus = self.getBoolean("hasFocus()", False)
        else:
            self.hasFocus = self.getBoolean("focus:hasFocus()", False)
            

        self.hasMargins = ((self.marginLeft != -2147483648) and (self.marginRight != -2147483648)  
                       and (self.marginTop != -2147483648) and (self.marginBottom != -2147483648))
    
    
    def parseElmentData(self, element_data):
        data = element_data.lstrip(" ")
        
        sep_index = data.index("@")
        self.class_name = data[0 : sep_index]
        
        sub_string = data[sep_index+1 : ]
        
        sep_index = sub_string.index(" ")
        self.hash_code = sub_string[0 : sep_index]
        
        sub_string = sub_string[sep_index+1 : ]
        
        self.loadProperties(sub_string)
        

    #===============================================================================
    # # get Class Name of View and its Instance Storage Address's Hash Code
    # # android.widget.ListView@44ed6480
    # # android.widget.TextView@44ed7e08
    #===============================================================================
    def getClassName(self, element):
        # split element by blank
        # so there will have some null string in head of tag list, as '', its length is 0
        tag_list = element.split(" ")
        head_tag = tag_list[0]
        while (0 == len(head_tag)):
            tag_list.remove(head_tag)
            head_tag = tag_list[0]
            
        l = head_tag.split("@")
        class_name = l[0]
        #return class_name
        return self.class_name
    
    #===========================================================================
    # # get Hash Code
    #===========================================================================
    def getHashCode(self, element):
        # split element by blank
        # so there will have some null string in head of tag list, as '', its length is 0
        tag_list = element.split(" ")
        head_tag = tag_list[0]
        while (0 == len(head_tag)):
            tag_list.remove(head_tag)
            head_tag = tag_list[0]       
    
        l = head_tag.split("@")
        hash_code = l[1]
        #return hash_code
        return self.hash_code
                    

    #===============================================================================
    # # etc. mID=7,id/sqrt
    #===============================================================================
    def getID(self, element):
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
    def getVisible(self, element):
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
    def getClickable(self, element):
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
    def getEnable(self, element):
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
    def getWillNotDraw(self, element):
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
    def getDRAWN(self, element):
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
    def getText(self, element):
        tag_list = element.split(" ")
        for tag in tag_list:
            if "mText=" in tag:
                l = tag.split(",")
                #return l[-1]
                
        if "mText" in self.properties_dict.keys():
            return self.properties_dict["mText"]
        else:
            return None
    
    def getEditText(self, element):
        pass       
    
    
    def getRectArea(self, element):
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

    
        #return rect
        rect.mTop = self.top
        rect.mBottom = self.bottom
        rect.mLeft = self.left
        rect.mRight = self.right
        return rect


    #===============================================================================
    # # this method has not used yet.
    #===============================================================================
    def getRectMidPoint(self, element):
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
    data = getInfosByTelnet("DUMP -1")
    element_parser = ParseElement()
    element_parser.getStructure(data)
