#! python2.7
## -*- coding: utf-8 -*-

#===============================================================================
# @author: kun
# @date: 2012-07-02
#===============================================================================

import os,sys
current_path = os.getcwd()
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if current_path not in sys.path:
    sys.path.append(current_path)
if parent_path not in sys.path:
    sys.path.append(parent_path)
    
from SystemComponent.Menu import Menu
from DeviceManagement.Device import Device
from ViewManagement.ViewTree import ViewTree
from ViewElement import ViewElement
import logging
import Logger

def testMenu():
    m_logger = Logger.InitLog("testMenu.log", logging.getLogger("testMenu.thread"))
    device = Device(m_logger)
    device.open()
    data = device.getInfosByTelnet()
    vt = ViewTree(m_logger)
    tree_nodes_list = vt.build(data)
    menu = Menu(tree_nodes_list)
    elements_list = menu.getElementList()
    
    for element in elements_list:
        print "begin deal with [%s]" %element.mText
        view_elemnet = ViewElement(element)
    
        
if __name__ == "__main__":    
    testMenu()