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
from ViewManagement.ViewTree import ViewTree
import logging
import Logger

def testMenu():
    m_logger = Logger.InitLog("testMenu.log", logging.getLogger("testMenu.thread"))
    vt = ViewTree(m_logger)
    tree_nodes_list = vt.build()
    menu = Menu(tree_nodes_list)
    elements_list = menu.getElementList()
    
    for element in elements_list:
        print element.mText
    
    
        
if __name__ == "__main__":    
    testMenu()