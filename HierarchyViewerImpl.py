#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## HierarchyViewerImpl.py

       
        
class HierarchyViewer():
    def __init__(self, monkey_runner_impl):
        self.hierarchy_viewer = monkey_runner_impl.device.getHierarchyViewer()
    
    def getFocusedWindowClassName(self):
        return self.hierarchy_viewer.getFocusedWindowName()