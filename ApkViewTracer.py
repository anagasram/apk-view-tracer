#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## ApkViewTracer.py

import platform,sys,os
from InitEnv import InitEnvironment
from InitDevice import init_service
import logging
import Logger

class ApkViewTracer():
    '''
    ApkViewTracer class is the main entry.
    '''
    
    __ClassName = "ApkViewTracer"
    
    def __init__(self, script_file_name="MonkeyRunnerImpl.py"):
        self.curDir = os.getcwd()+os.sep
        self.script_file = self.curDir + script_file_name
        self.m_logger = Logger.InitLog("apk-view-tracer.log", logging.getLogger("apk-view-tracer.thread"))
        
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
            self.m_logger.error("Current OS is not Windows or Linux!")
            raise Exception

def main(script_file_name):
    if False == init_service():
        print "[Error]Failed to init service!"
        raise Exception
    
    deviceCmd = DeviceCommand()
    data = deviceCmd.getCurrentViewInfo()
    element_parser = ParseElement()
    element_parser.getStructure(data)
    
    apk_view_tracer = ApkViewTracer(script_file_name)
    
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
    from DeviceCommand.DeviceCommand import DeviceCommand
    from ViewParser.ParseElement import ParseElement
    from ViewParser.BuildTree import build
    from ViewParser.GenerateViewFile import GenerateViewFile
    
    script_file_name="TestScripts/testMonkeyRunnerImpl.py"
    script_file_name="TestScripts/testNotification.py"
    script_file_name="TestScripts/testHome.py"
    main(script_file_name)
    
