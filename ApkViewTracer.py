#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ApkViewTracer.py

import platform,sys,os
from DeviceCommand import DeviceCommand
from InitDevice import init_service
from ParseElement import ParseElement
from BuildTree import build
from GenerateViewFile import GenerateViewFile

curDir = os.getcwd()+os.sep

def test():
    tree_nodes_list = build()
    viewFile_generator = GenerateViewFile()
    view_point_list = viewFile_generator.generateViewPointList(tree_nodes_list)
    #viewFile_generator.generateActionList(view_point_list)
    viewFile_generator.generateViewFile(view_point_list, "demo.vf")

def run(script_file):
    curOS=platform.system()
    if "Windows" == curOS:
        os.system(curDir+"Run.bat %s" %script_file)
    elif "Linux" == curOS:
        os.system(curDir+"Run.sh %s" %script_file)
    else:
        print "Current OS is not Windows or Linux!"
        return False

def main():
    if False == init_service():
        print "failed to init service!"
        raise Exception
    deviceCmd = DeviceCommand()
    data = deviceCmd.getCurrentViewInfo()
    element_parser = ParseElement()
    element_parser.getStructure(data)
    
    test()
    
    script_file=""
    if None == sys.argv or 2>len(sys.argv):
        script_file=curDir+"Demo.py"
    else:
        script_file = sys.argv[1]
        
    run(script_file)

if __name__=="__main__":
    main()
