#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## HierarchyViewerImpl.py

from MonkeyRunnerImpl import MonkeyRunnerImpl      
        
class HierarchyViewer():
    def __init__(self, monkey_runner_impl):
        self.class_name = "HierarchyViewer"
        try:
            self.hierarchy_viewer = monkey_runner_impl.device.getHierarchyViewer()
            return True
        except Exception, e:
            print "[%s] Failed to init [%s]" %(self.class_name, str(e))
            return False
    
    def getFocusedWindowClassName(self):
        return self.hierarchy_viewer.getFocusedWindowName()
    
    def getTextById(self, str_id):
        view_node = self.hierarchy_viewer.findViewById(str_id)
        return self.hierarchy_viewer.getText(view_node)
    
    def getVisibleById(self, str_id):
        view_node = self.hierarchy_viewer.findViewById(str_id)
        return self.hierarchy_viewer.visible(view_node)
    
    def getAbsolutePositionOfViewById(self, str_id):
        view_node = self.hierarchy_viewer.findViewById(str_id)
        return self.hierarchy_viewer.getAbsolutePositionOfView(view_node)
    
    def getAbsoluteCenterOfViewById(self, str_id):
        view_node = self.hierarchy_viewer.findViewById(str_id)
        return self.hierarchy_viewer.getAbsoluteCenterOfView(view_node)    
        
if __name__ == "__main__":
    monkey_runner_impl = MonkeyRunnerImpl()
    hierarchy_viewer = HierarchyViewer(monkey_runner_impl)
    print hierarchy_viewer.getFocusedWindowClassName()