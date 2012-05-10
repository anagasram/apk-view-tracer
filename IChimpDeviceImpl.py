#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## IChimpDeviceImpl.py

class IChimpDevice():
    def __init__(self, monkey_runner_impl):
        self.ichimp_device = monkey_runner_impl.device.getImpl()
        
    def getFocusedWindowClassName(self):
        HV = self.ichimp_device.getHierarchyViewer()
        return HV.getFocusedWindowName()