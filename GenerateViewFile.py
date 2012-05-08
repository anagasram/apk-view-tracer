#! python2.7
## -*- coding: utf-8 -*-

## kun for apk view tracing
## GenerateViewFile.py

from BuildTree import build
import os
from toolkit import getViewFileDir

class GenerateViewFile():
    ## class variables
    ## Action List and Map which ensure action sequence
    click_action_list=[]
    touch_action_list=[]
    drag_action_list=[]
    Action_Sequence_Map = {"click": click_action_list,
                           "touch": touch_action_list,
                           "drag": drag_action_list}
    def __init__(self):
        pass 

    def getViewCenterPoint(self, node):
        width = node.mAbsoluteRect.mRight - node.mAbsoluteRect.mLeft
        height = node.mAbsoluteRect.mBottom - node.mAbsoluteRect.mTop
        pointX = node.mAbsoluteRect.mLeft + width/2
        pointY = node.mAbsoluteRect.mTop + height/2    
        return pointX,pointY
    
    
    def generateViewPointList(self, tree_nodes_list):
        view_point_list=[]
        
        for node in tree_nodes_list:
            if node.mActive:
                view_point_list.append(self.getViewCenterPoint(node))
                
        print view_point_list
        return view_point_list


    ## generate view file named "***.vf"
    ## not implement yet
    def generateViewFile(self, view_point_list, file_name):
        view_file_dir = getViewFileDir()
        view_file_path = view_file_dir + os.sep + file_name
        view_file = open(view_file_path, "w")
        
        ## click events sequence
        for view_point in view_point_list:
            view_file.write(str(view_point[0])+"|"+str(view_point[1])+"\n")
            
        try:
            view_file.close()
        except Exception,e:
            print "Failed to close the view file! [Error] %s " %str(e)

    ## return list in memory
    def generateActionList(self, view_point_list):
        action_sequence_list=[]
    
        return action_sequence_list
    

def main():
    tree_nodes_list = build()
    viewFile_generator = GenerateViewFile()
    view_point_list = viewFile_generator.generateViewPointList(tree_nodes_list)
    #viewFile_generator.generateActionList(view_point_list)
    viewFile_generator.generateViewFile(view_point_list, "demo.vf")


if __name__=="__main__":
    main()
