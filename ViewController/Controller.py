#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
#===============================================================================

from MonkeyRunnerImpl import MonkeyRunnerImpl
from IChimpDeviceImpl import IChimpDevice
from HierarchyViewerImpl import HierarchyViewer
from EasyDeviceImpl import EasyDevice

class Controller():
    '''
    Controller
    '''
    
    def __init__(self, logger, device_name):
        self.m_logger = logger
        self.device_name = device_name
        
        self.monkeyrunner_device = MonkeyRunnerImpl(self.m_logger, self.device_name)
        self.chimp_device = IChimpDevice(self.m_logger, self.monkeyrunner_device)
        self.hierarchy_viewer = HierarchyViewer(self.m_logger, self.monkeyrunner_device)
        self.easy_device = EasyDevice(self.m_logger, self.monkeyrunner_device)
    
    def clickByID(self, view_id):
        pass
    
    def clickByText(self, text):
        pass
    
    def clickByIndex(self, index):
        pass   

#------------------------------------------------------------------------------ 
#    Physical Buttons
#------------------------------------------------------------------------------     
    def longClickHome(self):
        pass
    
    def goBack(self):
        self.monkeyrunner_device.clickBackButton()
    
    def callMenu(self):
        self.monkeyrunner_device.clickMenuButton()
    
    def down(self):
        pass
    
    def up(self):
        pass
    
    def left(self):
        pass
    
    def right(self):
        pass
    
    