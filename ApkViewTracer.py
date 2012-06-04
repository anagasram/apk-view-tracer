#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ApkViewTracer.py

import platform,sys,os
from InitEnv import InitEnvironment
from InitDevice import init_service

class ApkViewTracer():
    def __init__(self, script_file_name="MonkeyRunnerImpl.py"):
        self.curDir = os.getcwd()+os.sep
        self.script_file = self.curDir + script_file_name
        
    def prepare(self):
        tree_nodes_list = build()
        viewFile_generator = GenerateViewFile()
        view_point_list = viewFile_generator.generateViewPointList(tree_nodes_list)
        #viewFile_generator.generateActionList(view_point_list)
        viewFile_generator.generateViewFile(view_point_list, "click.vf")

    def run(self, script_file):       
        curOS=platform.system()
        if "Windows" == curOS:
            os.system(self.curDir+"Run.bat %s" %script_file)
        elif "Linux" == curOS:
            os.system(self.curDir+"Run.sh %s" %script_file)
        else:
            print "Current OS is not Windows or Linux!"
            raise Exception

def main():
    if False == init_service():
        print "failed to init service!"
        raise Exception
    
    deviceCmd = DeviceCommand()
    data = deviceCmd.getCurrentViewInfo()
    element_parser = ParseElement()
    element_parser.getStructure(data)
    
    apk_view_tracer = ApkViewTracer(script_file_name="testMonkeyRunnerImpl.py")
    
    apk_view_tracer.prepare()
    
    script_file=""
    if None == sys.argv or 2>len(sys.argv):
        script_file = apk_view_tracer.script_file
    else:
        script_file = sys.argv[1]
        
    apk_view_tracer.run(script_file)

if __name__=="__main__":
    init_env = InitEnvironment()
    init_env.run()
    from DeviceCommand import DeviceCommand
    from ParseElement import ParseElement
    from BuildTree import build
    from GenerateViewFile import GenerateViewFile
    main()
